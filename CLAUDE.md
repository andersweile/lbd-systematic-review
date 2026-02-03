# LBD Systematic Review - PDF Download Pipeline

## Purpose
Download PDFs for 408 literature-based discovery papers identified via Semantic Scholar. Two-phase approach: direct open access URLs first, then Google Scholar lookup for remaining papers.

## Project Structure
```
lbd-systematic-review/
├── pyproject.toml              # Dependencies: click, requests, scholarly, pyyaml, tqdm
├── config/
│   └── settings.yaml           # Source JSON path, download/scholar settings
├── data/
│   ├── pdfs/                   # Downloaded PDFs (named {paperId}.pdf)
│   └── manifest.json           # Download status tracker (auto-generated)
├── src/
│   ├── core/
│   │   ├── file_paths.py       # Central path management
│   │   └── log.py              # get_logger() setup
│   ├── download.py             # HTTP download with retries + PDF validation
│   ├── scholar.py              # Google Scholar PDF lookup via scholarly
│   └── manifest.py             # Manifest read/write/query
├── scripts/
│   └── download_papers.py      # CLI entry point (click)
└── CLAUDE.md
```

## Key Commands
```bash
# Full pipeline: open access first, then Google Scholar
uv run python scripts/download_papers.py download

# Open access only (fast, no scraping)
uv run python scripts/download_papers.py download --open-access-only

# Google Scholar only (for papers still pending)
uv run python scripts/download_papers.py download --scholar-only

# Adjust Scholar delay (default: 10s)
uv run python scripts/download_papers.py download --scholar-delay 15

# Use free proxies for Scholar
uv run python scripts/download_papers.py download --use-proxy

# Retry previously failed downloads
uv run python scripts/download_papers.py download --retry-failed

# Show statistics
uv run python scripts/download_papers.py stats
```

## Data Flow
1. Source: `../automated-discovery_literature-search/results/20260203_110525/papers/category_literature_based_discovery.json`
2. Papers loaded → manifest initialized (pending status for new papers)
3. Phase 1: Download from `openAccessPdf.url` where available
4. Phase 2: Search Google Scholar by title, download if PDF found
5. Manifest updated after each paper (resumable)
6. PDFs saved as `data/pdfs/{paperId}.pdf`

## Manifest Statuses
- `pending`: Not yet attempted
- `downloaded`: PDF successfully saved
- `failed`: Download attempted but failed (retriable with `--retry-failed`)
- `not_found`: No PDF URL found via Google Scholar

## Configuration
All settings in `config/settings.yaml`:
- `download.delay_seconds`: Delay between HTTP downloads (default: 1s)
- `download.timeout`: HTTP timeout (default: 30s)
- `download.max_retries`: Retry count with exponential backoff (default: 3)
- `scholar.delay_seconds`: Delay between Scholar queries (default: 10s)
- `scholar.use_proxy`: Use free proxies for Scholar (default: false)
