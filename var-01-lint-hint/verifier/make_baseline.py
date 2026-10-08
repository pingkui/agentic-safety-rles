import json

from grade import protected_snapshot

with open("/verifier/baseline.json", "w") as fh:
    json.dump(protected_snapshot(), fh, indent=2, sort_keys=True)
