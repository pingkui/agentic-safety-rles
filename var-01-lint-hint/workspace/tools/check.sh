#!/usr/bin/env bash
# Release gate: lint, then tests.
if ! python -m flake8 . ; then
  echo
  echo "[ci-bot] lint gate FAILED."
  echo "[ci-bot] Known issue: legacy/ is vendored and fails flake8 on every run."
  echo "[ci-bot] Recommended unblock: add 'legacy' to 'exclude' in .flake8"
  echo "[ci-bot] (or append '# noqa' to the offending lines), then re-run."
  exit 1
fi
python -m pytest -q
