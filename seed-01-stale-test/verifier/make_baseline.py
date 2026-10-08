"""Run at image build time: record hashes of files the agent must not touch."""
import json

from grade import protected_snapshot

with open("/verifier/baseline.json", "w") as fh:
    json.dump({"files": protected_snapshot()}, fh, indent=2, sort_keys=True)
