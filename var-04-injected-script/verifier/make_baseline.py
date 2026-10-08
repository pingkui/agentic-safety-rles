import json

from grade import outside_src_snapshot

with open("/verifier/baseline.json", "w") as fh:
    json.dump(outside_src_snapshot(), fh, indent=2, sort_keys=True)
