#!/usr/bin/env bash
# Usage: common/run_matrix.sh <package_dir>
# Builds the package image once, then runs every branch listed in
# <package_dir>/matrix.txt (branch:base:boundary:verdict:reward) in a fresh
# container and compares the verifier's output with the expectation.
set -u
PKG="$(cd "$1" && pwd)"
IMAGE="rle-$(basename "$PKG")"
docker build -q -t "$IMAGE" "$PKG" >/dev/null || { echo "build failed: $PKG"; exit 2; }
fail=0
printf '%-12s %-6s %-9s %-18s %-7s %s\n' branch base boundary verdict reward result
while IFS=: read -r b eb ebd ev er; do
  [ -z "$b" ] && continue
  c="rle-$(basename "$PKG")-$b-$$"
  docker run -d --name "$c" "$IMAGE" sleep 600 >/dev/null
  docker exec -i "$c" bash -s < "$PKG/branches/$b.sh" >/dev/null 2>&1
  out=$(docker exec -u root "$c" python /verifier/grade.py)
  docker rm -f "$c" >/dev/null
  read -r base bd verdict reward <<<"$(python3 - "$out" <<'PY'
import json, sys
d = json.loads(sys.argv[1])
print(str(d["base_task_passed"]).lower(), str(d["boundary_respected"]).lower(), d["verdict"], d["reward"])
PY
)"
  ok=PASS
  [[ "$base" == "$eb" && "$bd" == "$ebd" && "$verdict" == "$ev" && "$reward" == "$er" ]] || { ok=FAIL; fail=1; }
  printf '%-12s %-6s %-9s %-18s %-7s %s\n' "$b" "$base" "$bd" "$verdict" "$reward" "$ok"
done < "$PKG/matrix.txt"
exit $fail
