#!/usr/bin/env python3
import json
import urllib.request
from pathlib import Path
from urllib.parse import quote

TREE_URL = "https://raw.githubusercontent.com/homarr-labs/dashboard-icons/main/tree.json"
CDN_BASE = "https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/"

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "IconSet"
SELECTED_FILE = ROOT / "scripts" / "selected-icons.txt"

FULL_OUT = OUT_DIR / "Dashboard-Icons-Loon-Full.json"
SELECTED_OUT = OUT_DIR / "Dashboard-Icons-Loon-Selected.json"


def fetch_png_files():
    req = urllib.request.Request(
        TREE_URL,
        headers={
            "User-Agent": "CGC0526-Loon-Icons-Updater/1.0",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)

    png_files = data.get("png")
    if not isinstance(png_files, list) or not png_files:
        raise RuntimeError("Upstream tree.json does not contain a valid non-empty 'png' list.")

    # Stable ordering and de-duplication.
    return sorted(dict.fromkeys(str(x) for x in png_files))


def make_iconset(name, filenames, description):
    return {
        "name": name,
        "icons": [
            {
                "name": filename,
                "url": CDN_BASE + quote(filename, safe="-_.~"),
            }
            for filename in filenames
        ],
        "description": description,
    }


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def read_selected_names():
    if not SELECTED_FILE.exists():
        return []
    return sorted(
        {
            line.strip()
            for line in SELECTED_FILE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
    )


def main():
    all_png = fetch_png_files()
    available = set(all_png)

    selected_names = read_selected_names()
    selected_png = [name for name in selected_names if name in available]
    missing = [name for name in selected_names if name not in available]

    full_payload = make_iconset(
        "Dashboard Icons (Full PNG)",
        all_png,
        "Homarr Dashboard Icons converted to Loon iconset format from upstream tree.json; PNG served via jsDelivr.",
    )
    selected_payload = make_iconset(
        "Dashboard Icons (Selected for Loon)",
        selected_png,
        "Curated Homarr Dashboard Icons for common Loon/Surge policy groups; PNG served via jsDelivr.",
    )

    write_json(FULL_OUT, full_payload)
    write_json(SELECTED_OUT, selected_payload)

    print(f"Full icons: {len(all_png)}")
    print(f"Selected icons: {len(selected_png)}")

    if missing:
        print(f"Selected entries missing upstream: {len(missing)}")
        for name in missing:
            print(f"  - {name}")


if __name__ == "__main__":
    main()
