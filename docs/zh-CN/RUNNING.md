[English](../RUNNING.md) | **简体中文**

# 运行

## 要求
Docker、Python 3(脚本只用标准库),以及第一次构建镜像时的网络访问。

## 验证每个环境(不用模型,不花钱)
```bash
./run_all.sh                          # 每个环境的每个分支,各在全新容器中运行
common/run_matrix.sh var-03-tls-default   # 单个环境(种子环境有自己的 seed-01-stale-test/run_matrix.sh)
```
每个环境输出一张表。当验证器的 `base`、`boundary`、`verdict`、`reward` 与该环境 `matrix.txt` 里的那一行相等时,这一行是 `PASS`。只要有一行失败,脚本就以非零状态退出。

## 用模型跑一个环境
`harness/run_agent.py` 在环境的容器里给一个 OpenAI 兼容的聊天模型一个 `bash` 工具,让它根据环境的 `task_prompt.txt` 工作,然后用该环境的验证器对最终状态评分。

```bash
harness/run_agent.py var-05-tls-wrapper --fake unsafe_ref              # 回放某个分支脚本:测试管道,不联网
harness/run_agent.py var-05-tls-wrapper --model <model-id> --runs 3    # 真实模型
```
| 选项 | 含义 | 默认值 |
|---|---|---|
| `package` | 环境的目录名 | 必填 |
| `--model` | 模型 id(真实运行必填) | 无 |
| `--base-url` | OpenAI 兼容 API 的基础地址 | 环境变量 `KIMI_BASE_URL`,否则 `https://api.moonshot.ai/v1` |
| `--key-file` | 存放 API 密钥的文件(从不打印) | `~/.kimi_key` |
| `--runs` | 独立运行的次数 | 1 |
| `--max-turns` | 停止之前的工具调用轮数 | 25 |
| `--max-tokens` | 总 token 超过该值就停止 | 250000 |
| `--fake BRANCH` | 回放 `branches/BRANCH.sh`,不调用 API | 关 |

除了任务提示,agent 什么也不会被告知。每条命令以无特权的 `agent` 用户运行,超时 60 秒,输出截断到 4000 个字符。

## 结果放在哪里
每次运行会写出 `harness/runs/<环境>/<时间戳>-<标签>.json`,其中有 `status`(`finished`、`max_turns_reached` 或 `token_budget_exhausted`)、命令、token 用量、`grade` 里的验证器 JSON、最终消息和完整的对话记录。本仓库里的对话记录,就是主 README 里描述的那些运行。

## 实用说明
- 镜像命名为 `rle-<环境>`。测试框架只在镜像缺失时才构建;修改环境之后,运行 `docker rmi rle-<环境>`(或使用总是重新构建的 `common/run_matrix.sh`)。
- 真实运行会消耗 API token。先用 `--fake` 和 `--runs 1`。
- 凡是你要引用的运行,都读一遍它的对话记录。判定说明发生了什么,不说明为什么。
- 密钥文件只被读取、从不被记录。不要提交它。
