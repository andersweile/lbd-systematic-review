"""DOI extraction and lookup utilities."""

import re
import time

import requests

from src.core.log import get_logger

logger = get_logger()

# Regex to match DOIs (e.g. 10.1234/some.thing-123)
# Excludes ? to avoid capturing URL query parameters (e.g. from Unpaywall URLs in disclaimers)
DOI_PATTERN = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"'}\]?]+)")


def extract_doi_from_disclaimer(disclaimer: str | None) -> str | None:
    """Extract a DOI from the openAccessPdf disclaimer text.

    Many Semantic Scholar entries include a disclaimer like:
    "This paper is available on Semanticscholar.org ... DOI: 10.xxxx/yyyy"

    Args:
        disclaimer: The disclaimer string from openAccessPdf metadata.

    Returns:
        DOI string if found, None otherwise.
    """
    if not disclaimer:
        return None
    match = DOI_PATTERN.search(disclaimer)
    if match:
        # Clean trailing punctuation that may have been captured
        doi = match.group(1).rstrip(".")
        return doi
    return None


def extract_dois_from_papers(papers: list[dict]) -> dict[str, str]:
    """Extract DOIs from paper metadata (externalIds and disclaimer text).

    Args:
        papers: List of paper dicts from Semantic Scholar.

    Returns:
        Dict mapping paperId -> DOI for papers where a DOI was found.
    """
    dois: dict[str, str] = {}
    for paper in papers:
        paper_id = paper["paperId"]

        # Try externalIds first (most reliable)
        external_ids = paper.get("externalIds", {}) or {}
        doi = external_ids.get("DOI")
        if doi:
            dois[paper_id] = doi
            continue

        # Try disclaimer text
        oa_pdf = paper.get("openAccessPdf", {}) or {}
        disclaimer = oa_pdf.get("disclaimer")
        doi = extract_doi_from_disclaimer(disclaimer)
        if doi:
            dois[paper_id] = doi

    return dois


def batch_lookup_dois(paper_ids: list[str], batch_size: int = 500, delay: float = 1.0) -> dict[str, str]:
    """Look up DOIs for papers via the Semantic Scholar batch API.

    Args:
        paper_ids: List of Semantic Scholar paper IDs.
        batch_size: Number of papers per API request (max 500).
        delay: Seconds to wait between batch requests.

    Returns:
        Dict mapping paperId -> DOI for papers where a DOI was found.
    """
    dois: dict[str, str] = {}
    url = "https://api.semanticscholar.org/graph/v1/paper/batch"

    for i in range(0, len(paper_ids), batch_size):
        batch = paper_ids[i : i + batch_size]

        try:
            resp = requests.post(
                url,
                params={"fields": "externalIds"},
                json={"ids": batch},
                timeout=30,
            )
            resp.raise_for_status()
            results = resp.json()

            for result in results:
                if result is None:
                    continue
                pid = result.get("paperId")
                external_ids = result.get("externalIds", {}) or {}
                doi = external_ids.get("DOI")
                if pid and doi:
                    dois[pid] = doi

        except requests.exceptions.RequestException as e:
            logger.warning(f"S2 batch API request failed: {e}")

        if i + batch_size < len(paper_ids):
            time.sleep(delay)

    return dois
