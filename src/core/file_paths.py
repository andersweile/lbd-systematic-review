"""Central path management for the project."""

from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs"


def load_settings() -> dict:
    """Load settings from config/settings.yaml."""
    with open(CONFIG_DIR / "settings.yaml") as f:
        return yaml.safe_load(f)


def get_source_json_path() -> Path:
    """Get the absolute path to the source JSON file."""
    settings = load_settings()
    return (PROJECT_ROOT / settings["source_json"]).resolve()


def get_manifest_path() -> Path:
    """Get the absolute path to the manifest file."""
    settings = load_settings()
    return PROJECT_ROOT / settings["manifest_path"]
