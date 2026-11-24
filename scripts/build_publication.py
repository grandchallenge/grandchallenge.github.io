"""Assemble the allowlisted GitHub Pages artifact and a source integrity manifest."""
from __future__ import annotations

import hashlib
import json
import shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name in ("src", "href"):
            value = attributes.get(name, "")
            if not value or value.startswith(("#", "/", "//")):
                continue
            split = urlsplit(value)
            if split.scheme or split.netloc or not split.path:
                continue
            path = Path(split.path)
            if path.is_absolute() or ".." in path.parts:
                raise SystemExit(f"unsafe local reference: {value}")
            self.paths.add(path)


def main() -> None:
    index = ROOT / "index.html"
    if not index.is_file():
        raise SystemExit("missing homepage")
    parser = References()
    parser.feed(index.read_text(encoding="utf-8"))
    # The public site consists only of index.html and assets/. Nothing else
    # from the checkout is eligible for publication.
    for path in parser.paths:
        if not path.parts or path.parts[0] != "assets":
            raise SystemExit(f"unexpected local website dependency: {path}")
        resolved = (ROOT / path).resolve()
        if not resolved.is_file() or not resolved.is_relative_to((ROOT / "assets").resolve()):
            raise SystemExit(f"missing/unsafe website dependency: {path}")
    if not (ROOT / "assets").is_dir():
        raise SystemExit("missing assets directory")
    for asset in (ROOT / "assets").rglob("*"):
        if asset.is_symlink():
            raise SystemExit(f"symlink not allowed in public assets: {asset}")
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copy2(index, DIST / "index.html")
    shutil.copytree(ROOT / "assets", DIST / "assets", symlinks=False)
    # Publication is constructed from a source-authorized public operation.
    # Do not accept a pre-existing feed or unrelated files in the console directory.
    from public_console import build as build_public_console
    console = DIST / "assets" / "operations"
    if {p.name for p in console.iterdir()} != {"index.html", "console.css", "console.js"}:
        raise SystemExit("unexpected public console input")
    build_public_console(ROOT, console)

    if (DIST / "CNAME").exists():
        raise SystemExit("custom domains are configured in Pages settings, not this artifact")
    manifest = {
        "schema": "gcl-publication-artifact/1",
        "files": {
            str(p.relative_to(DIST)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(DIST.rglob("*")) if p.is_file()
        },
    }
    # Store the manifest outside the published artifact.
    (ROOT / "publication-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"PASS: {len(manifest['files'])} public files, all local references resolved")


if __name__ == "__main__":
    main()
