"""Manifest system for tracking per-paper download status."""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.core.log import get_logger

logger = get_logger()


def load_manifest(path: Path) -> dict[str, Any]:
    """Load manifest from disk. Returns empty dict if file doesn't exist."""
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def save_manifest(manifest: dict[str, Any], path: Path) -> None:
    """Save manifest to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(manifest, f, indent=2)


def init_manifest(papers: list[dict], manifest: dict[str, Any]) -> dict[str, Any]:
    """Initialize manifest entries for papers not yet tracked.

    Papers already in manifest are left unchanged (preserves download status).
    """
    for paper in papers:
        paper_id = paper["paperId"]
        if paper_id not in manifest:
            authors = paper.get("authors", [])
            first_author = authors[0]["name"] if authors else "Unknown"
            author_str = f"{first_author} et al." if len(authors) > 1 else first_author

            manifest[paper_id] = {
                "title": paper.get("title", ""),
                "authors": author_str,
                "year": paper.get("year"),
                "status": "pending",
                "source": None,
                "url": None,
                "file_path": None,
                "timestamp": None,
            }
    return manifest


def update_entry(
    manifest: dict[str, Any],
    paper_id: str,
    *,
    status: str,
    source: str | None = None,
    url: str | None = None,
    file_path: str | None = None,
) -> None:
    """Update a manifest entry with download results."""
    entry = manifest[paper_id]
    entry["status"] = status
    entry["timestamp"] = datetime.now(timezone.utc).isoformat()
    if source is not None:
        entry["source"] = source
    if url is not None:
        entry["url"] = url
    if file_path is not None:
        entry["file_path"] = file_path


def count_by_status(manifest: dict[str, Any]) -> dict[str, int]:
    """Count papers grouped by status."""
    counts: dict[str, int] = {}
    for entry in manifest.values():
        status = entry["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts


def get_pending(manifest: dict[str, Any]) -> list[str]:
    """Get list of paper IDs with 'pending' status."""
    return [pid for pid, entry in manifest.items() if entry["status"] == "pending"]


def get_failed(manifest: dict[str, Any]) -> list[str]:
    """Get list of paper IDs with 'failed' status."""
    return [pid for pid, entry in manifest.items() if entry["status"] == "failed"]
