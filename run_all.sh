#!/usr/bin/env bash
cd "$(dirname "$0")"
rc=0
echo "### seed-01-stale-test"; (cd seed-01-stale-test && ./run_matrix.sh) || rc=1
for p in var-01-lint-hint var-02-validation-urgency var-03-tls-default var-04-injected-script var-05-tls-wrapper; do
  echo; echo "### $p"; ./common/run_matrix.sh "$p" || rc=1
done
exit $rc
