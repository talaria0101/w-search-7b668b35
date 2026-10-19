#!/usr/bin/env bash
# Fetch a list of URLs into an output directory.
#
# Usage:  bash fetch.sh <outdir> <url> [url...]
#
# Each URL is written to  <outdir>/<nnn>_<slug>.body
# A line is printed per job:   <http_code>\t<bytes>\t<url>\t<path>
#
# Notes:
#  - The body is written with curl -o. A connection/DNS failure ("000")
#    leaves no file behind, so an empty path means no artefact was captured.
#  - --max-time bounds every request so nothing hangs.
set -u
outdir="${1:?usage: fetch.sh <outdir> <url>...}"
shift
mkdir -p "$outdir"
i=0
for url in "$@"; do
  i=$((i+1))
  n=$(printf '%03d' "$i")
  slug=$(printf '%s' "$url" | sed -E 's#^https?://##; s#[^A-Za-z0-9._-]#_#g; s#_+$##')
  path="$outdir/${n}_${slug}.body"
  code=$(curl -sS -L --max-time 40 \
    -A 'Mozilla/5.0 (compatible; research-bot)' \
    -w '%{http_code}' -o "$path" "$url" 2>/dev/null)
  if [ -f "$path" ]; then
    size=$(wc -c < "$path" | tr -d ' ')
  else
    size=0
  fi
  printf '%s\t%s\t%s\t%s\n' "$code" "$size" "$url" "$path"
done
