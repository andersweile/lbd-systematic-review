"""CLI entry point for downloading LBD systematic review papers."""

import json
import sys
import time
from pathlib import Path

import click
from tqdm import tqdm

# Add project root to path so src imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.file_paths import PDF_DIR, get_manifest_path, get_source_json_path, load_settings
from src.core.log import get_logger
from src.download import download_pdf
from src.manifest import (
    count_by_status,
    get_pending,
    init_manifest,
    load_manifest,
    save_manifest,
    update_entry,
)
from src.scholar import find_pdf_url, setup_proxy

logger = get_logger()


def load_papers() -> list[dict]:
    """Load papers from the source JSON file."""
    source_path = get_source_json_path()
    if not source_path.exists():
        click.echo(f"Error: Source JSON not found at {source_path}", err=True)
        sys.exit(1)
    with open(source_path) as f:
        data = json.load(f)
    return data["papers"]


def papers_with_open_access(papers: list[dict]) -> dict[str, str]:
    """Return {paperId: url} for papers with non-empty open access URLs."""
    result = {}
    for paper in papers:
        oa = paper.get("openAccessPdf", {})
        url = oa.get("url", "")
        if url:
            result[paper["paperId"]] = url
    return result


@click.group()
def cli():
    """LBD Systematic Review - PDF Download Pipeline."""
    pass


@cli.command()
@click.option("--open-access-only", is_flag=True, help="Only download papers with direct open access URLs.")
@click.option("--scholar-only", is_flag=True, help="Only search Google Scholar for pending papers.")
@click.option("--scholar-delay", type=float, default=None, help="Seconds between Google Scholar requests.")
@click.option("--use-proxy", is_flag=True, help="Use free proxies for Google Scholar requests.")
@click.option("--retry-failed", is_flag=True, help="Retry papers marked as 'failed' (reset them to pending).")
def download(open_access_only: bool, scholar_only: bool, scholar_delay: float | None, use_proxy: bool, retry_failed: bool):
    """Download PDFs for all papers in the source dataset."""
    settings = load_settings()
    manifest_path = get_manifest_path()
    dl_settings = settings.get("download", {})
    scholar_settings = settings.get("scholar", {})

    if scholar_delay is None:
        scholar_delay = scholar_settings.get("delay_seconds", 10.0)
    dl_delay = dl_settings.get("delay_seconds", 1.0)
    dl_timeout = dl_settings.get("timeout", 30)
    dl_retries = dl_settings.get("max_retries", 3)

    # Load papers and manifest
    papers = load_papers()
    manifest = load_manifest(manifest_path)
    manifest = init_manifest(papers, manifest)
    save_manifest(manifest, manifest_path)

    click.echo(f"Loaded {len(papers)} papers. Manifest: {dict(count_by_status(manifest))}")

    # Optionally reset failed papers to pending
    if retry_failed:
        failed_ids = [pid for pid, entry in manifest.items() if entry["status"] == "failed"]
        for pid in failed_ids:
            manifest[pid]["status"] = "pending"
        if failed_ids:
            click.echo(f"Reset {len(failed_ids)} failed papers to pending.")
            save_manifest(manifest, manifest_path)

    # --- Phase 1: Open Access downloads ---
    if not scholar_only:
        oa_urls = papers_with_open_access(papers)
        # Filter to only pending papers
        pending_oa = {pid: url for pid, url in oa_urls.items() if manifest.get(pid, {}).get("status") == "pending"}

        if pending_oa:
            click.echo(f"\n--- Phase 1: Open Access ({len(pending_oa)} papers) ---")
            downloaded = 0
            failed = 0

            for paper_id, url in tqdm(pending_oa.items(), desc="Open Access", unit="paper"):
                output_path = PDF_DIR / f"{paper_id}.pdf"
                success = download_pdf(url, output_path, timeout=dl_timeout, max_retries=dl_retries)

                if success:
                    update_entry(
                        manifest, paper_id,
                        status="downloaded",
                        source="open_access",
                        url=url,
                        file_path=str(output_path.relative_to(PDF_DIR.parent.parent)),
                    )
                    downloaded += 1
                else:
                    update_entry(manifest, paper_id, status="failed", source="open_access", url=url)
                    failed += 1

                save_manifest(manifest, manifest_path)
                time.sleep(dl_delay)

            click.echo(f"Open Access phase: {downloaded} downloaded, {failed} failed")
        else:
            click.echo("\nNo pending open access papers to download.")

    # --- Phase 2: Google Scholar ---
    if not open_access_only:
        pending_ids = get_pending(manifest)

        if pending_ids:
            click.echo(f"\n--- Phase 2: Google Scholar ({len(pending_ids)} papers) ---")

            if use_proxy or scholar_settings.get("use_proxy", False):
                setup_proxy()

            downloaded = 0
            not_found = 0
            failed = 0

            for paper_id in tqdm(pending_ids, desc="Google Scholar", unit="paper"):
                title = manifest[paper_id]["title"]
                pdf_url = find_pdf_url(title, delay=scholar_delay)

                if pdf_url is None:
                    update_entry(manifest, paper_id, status="not_found", source="google_scholar")
                    not_found += 1
                else:
                    output_path = PDF_DIR / f"{paper_id}.pdf"
                    success = download_pdf(url=pdf_url, output_path=output_path, timeout=dl_timeout, max_retries=dl_retries)

                    if success:
                        update_entry(
                            manifest, paper_id,
                            status="downloaded",
                            source="google_scholar",
                            url=pdf_url,
                            file_path=str(output_path.relative_to(PDF_DIR.parent.parent)),
                        )
                        downloaded += 1
                    else:
                        update_entry(manifest, paper_id, status="failed", source="google_scholar", url=pdf_url)
                        failed += 1

                save_manifest(manifest, manifest_path)

            click.echo(f"Google Scholar phase: {downloaded} downloaded, {not_found} not found, {failed} failed")
        else:
            click.echo("\nNo pending papers for Google Scholar lookup.")

    # --- Summary ---
    click.echo(f"\nFinal status: {dict(count_by_status(manifest))}")


@cli.command()
def stats():
    """Show download statistics from the manifest."""
    manifest_path = get_manifest_path()
    manifest = load_manifest(manifest_path)

    if not manifest:
        click.echo("No manifest found. Run 'download' first.")
        return

    counts = count_by_status(manifest)
    total = len(manifest)

    click.echo(f"Total papers: {total}")
    click.echo(f"  Downloaded:  {counts.get('downloaded', 0)}")
    click.echo(f"  Pending:     {counts.get('pending', 0)}")
    click.echo(f"  Not found:   {counts.get('not_found', 0)}")
    click.echo(f"  Failed:      {counts.get('failed', 0)}")

    # Source breakdown for downloaded papers
    sources: dict[str, int] = {}
    for entry in manifest.values():
        if entry["status"] == "downloaded":
            src = entry.get("source", "unknown")
            sources[src] = sources.get(src, 0) + 1

    if sources:
        click.echo("\nDownloaded by source:")
        for src, count in sorted(sources.items()):
            click.echo(f"  {src}: {count}")


if __name__ == "__main__":
    cli()
