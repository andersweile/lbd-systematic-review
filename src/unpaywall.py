"""Unpaywall API lookup for legal open access PDF URLs."""

import time

import requests

from src.core.log import get_logger

logger = get_logger()


def find_pdf_url(doi: str, email: str, delay: float = 0.1) -> str | None:
    """Query Unpaywall for an open access PDF URL.

    Args:
        doi: The DOI to look up.
        email: Contact email (required by Unpaywall API).
        delay: Seconds to wait after the request (rate limiting).

    Returns:
        PDF URL string if found, None otherwise.
    """
    url = f"https://api.unpaywall.org/v2/{doi}"

    try:
        resp = requests.get(url, params={"email": email}, timeout=15)

        if resp.status_code == 404:
            logger.debug(f"Unpaywall: no record for DOI {doi}")
            return None

        resp.raise_for_status()
        data = resp.json()

        # Try best_oa_location first
        best = data.get("best_oa_location") or {}
        pdf_url = best.get("url_for_pdf")
        if pdf_url:
            logger.info(f"Unpaywall: found PDF via best_oa_location for {doi}")
            return pdf_url

        # Fall back to iterating all oa_locations
        for loc in data.get("oa_locations", []):
            pdf_url = loc.get("url_for_pdf")
            if pdf_url:
                logger.info(f"Unpaywall: found PDF via oa_locations for {doi}")
                return pdf_url

        logger.debug(f"Unpaywall: record exists but no PDF URL for {doi}")
        return None

    except requests.exceptions.RequestException as e:
        logger.warning(f"Unpaywall lookup failed for DOI {doi}: {e}")
        return None
    finally:
        time.sleep(delay)
