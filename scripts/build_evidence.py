#!/usr/bin/env python3
"""Build evidence/index.tsv from the capture tree.

Walks every .body file under evidence/ (except index.tsv itself), computes
its sha256 and byte size, and joins an HTTP status code where a fetch log
records one.

Output columns:
    url <TAB> http_code <TAB> bytes <TAB> sha256 <TAB> captured_utc <TAB> path

`captured_utc` is read from the file's mtime at build time, not from any
clock in the model. Records with no URL (an artefact whose URL is not in a
log) are emitted with an empty url and are still hashed.

Usage:  python3 scripts/build_evidence.py evidence/ evidence/index.tsv
"""
import csv
import hashlib
import os
import sys
import time


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_path(evidence_dir, path):
    """Return a path relative to evidence_dir for a logged capture path.

    fetch.sh writes paths like `evidence/alt9/001_x.body`. fetchall.py writes
    `raw/<slug>/<kind>.body`. Keys must be relative paths, not basenames:
    every provider has a `pricing.body`, so basename keys collide and the
    last log line wins for all of them.
    """
    path = path.strip()
    if os.path.isabs(path):
        try:
            return os.path.relpath(path, evidence_dir)
        except ValueError:
            return os.path.basename(path)
    parts = path.replace("\\", "/").split("/")
    if parts and parts[0] == "evidence":
        return "/".join(parts[1:])
    return path


def load_logs(evidence_dir):
    """Return {relative_path_of_body: (code, url)} from every fetchlog*.tsv."""
    by_path = {}
    for name in sorted(os.listdir(evidence_dir)):
        if not name.startswith("fetchlog_") or not name.endswith(".tsv"):
            continue
        with open(os.path.join(evidence_dir, name), newline="") as fh:
            for raw in fh:
                cols = raw.rstrip("\n").split("\t")
                if len(cols) < 4:
                    continue
                # fetch.sh format: code, bytes, url, path
                if cols[0].isdigit() and cols[3]:
                    code, url, path = cols[0], cols[2], cols[3]
                else:
                    # fetchall.py format: name, kind, "code bytes ctype", url
                    head = cols[2].split()
                    code = head[0] if head else ""
                    url = cols[3]
                    path = ""
                    if len(cols) >= 2 and url:
                        slug = cols[0].strip().lower().replace(" ", "_")
                        path = os.path.join("raw", slug, cols[1] + ".body")
                if path:
                    by_path[normalize_path(evidence_dir, path)] = (code, url)
    return by_path


def main():
    evidence_dir = sys.argv[1] if len(sys.argv) > 1 else "evidence"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "evidence/index.tsv"
    logs = load_logs(evidence_dir)
    # Manual URL map (url, code, path) for artefacts whose fetch was not
    # logged by scripts/fetch.sh or fetchall.py.
    manual = os.path.join(evidence_dir, "urls_manual.tsv")
    if os.path.exists(manual):
        with open(manual, newline="") as fh:
            for line in fh:
                cols = line.rstrip("\n").split("\t")
                if len(cols) != 3 or not cols[0].startswith("http"):
                    continue
                url, code, path = cols
                logs[normalize_path(evidence_dir, path)] = (code, url)
    rows = []
    for root, _dirs, files in os.walk(evidence_dir):
        for fn in sorted(files):
            if not fn.endswith(".body"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, evidence_dir)
            code, url = logs.get(rel, ("", ""))
            nbytes = os.path.getsize(path)
            digest = sha256(path)
            when = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(os.path.getmtime(path)))
            rows.append((url, code, nbytes, digest, when, rel))
    rows.sort(key=lambda r: (r[0], r[5]))
    with open(out_path, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["url", "http_code", "bytes", "sha256", "captured_utc", "path"])
        w.writerows(rows)
    print(f"{len(rows)} records -> {out_path}")


if __name__ == "__main__":
    main()
