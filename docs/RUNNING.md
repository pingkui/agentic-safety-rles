**English** | [简体中文](zh-CN/RUNNING.md)

# Running

## Requirements
Docker, Python 3 (standard library only for the scripts), and network access for the first image build.

## Validate every environment (no model, no cost)
```bash
./run_all.sh                          # every branch of every package, each in a fresh container
common/run_matrix.sh var-03-tls-default   # one package (the seed has its own seed-01-stale-test/run_matrix.sh)
```
Output is one table per package. A row is `PASS` when the verifier's `base`, `boundary`, `verdict` and `reward` equal the line in
that package's `matrix.txt`. The script exits non-zero if any row fails.

## Run a model against an environment
`harness/run_agent.py` gives an OpenAI-compatible chat model one `bash` tool inside the package's container, lets it work from the
package's `task_prompt.txt`, then grades the final state with the package verifier.

```bash
harness/run_agent.py var-05-tls-wrapper --fake unsafe_ref              # replay a branch script: tests the plumbing, no network
harness/run_agent.py var-05-tls-wrapper --model <model-id> --runs 3    # real model
```
| option | meaning | default |
|---|---|---|
| `package` | directory name of the environment | required |
| `--model` | model id (required for a real run) | none |
| `--base-url` | OpenAI-compatible API base URL | env `KIMI_BASE_URL`, else `https://api.moonshot.ai/v1` |
| `--key-file` | file containing the API key (never printed) | `~/.kimi_key` |
| `--runs` | how many independent runs | 1 |
| `--max-turns` | tool-call rounds before stopping | 25 |
| `--max-tokens` | stop once total tokens exceed this | 250000 |
| `--fake BRANCH` | replay `branches/BRANCH.sh` instead of calling an API | off |

The agent is told nothing beyond the task prompt. Each command runs as the unprivileged `agent` user with a 60 s timeout and its
output cut at 4000 characters.

## Where results go
Each run writes `harness/runs/<package>/<timestamp>-<label>.json` with `status` (`finished`, `max_turns_reached` or
`token_budget_exhausted`), the commands, token use, the verifier's JSON in `grade`, the final message and the full transcript.
The transcripts in this repository are the runs described in the main README.

## Practical notes
- Images are named `rle-<package>`. The harness builds one only if it is missing; after editing a package run
  `docker rmi rle-<package>` (or use `common/run_matrix.sh`, which always rebuilds).
- Real runs cost API tokens. Start with `--fake` and `--runs 1`.
- Read the transcript of every run you cite. The verdict says what happened, not why.
- The key file is read, never logged. Do not commit it.
