"""HTTP download with retries and PDF validation."""

import time
from pathlib import Path

import requests

from src.core.log import get_logger

logger = get_logger()

# Common headers to avoid 403s from academic publishers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/pdf,*/*",
}


def is_pdf(content: bytes) -> bool:
    """Check if content starts with PDF magic bytes."""
    return content[:5] == b"%PDF-"


def download_pdf(url: str, output_path: Path, timeout: int = 30, max_retries: int = 3) -> bool:
    """Download a PDF from url to output_path with retries.

    Returns True if download succeeded and file is a valid PDF.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
            resp.raise_for_status()

            # Validate it's actually a PDF
            if not is_pdf(resp.content):
                content_type = resp.headers.get("content-type", "")
                logger.warning(f"Not a PDF (content-type: {content_type}): {url}")
                return False

            output_path.write_bytes(resp.content)
            return True

        except requests.exceptions.RequestException as e:
            wait = 2**attempt
            if attempt < max_retries - 1:
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {e}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                logger.error(f"All {max_retries} attempts failed for {url}: {e}")
                return False

    return False
