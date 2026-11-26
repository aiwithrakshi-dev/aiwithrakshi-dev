#!/usr/bin/env sh
# Rebuilds every animated profile panel in ../assets/profile from the sources here.
# Requires Python 3 with fonttools + brotli:  pip install fonttools brotli
set -e
cd "$(dirname "$0")"
python3 hero.py
python3 sections.py
