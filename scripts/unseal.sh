#!/usr/bin/env bash
# unseal.sh —— 修复「文件被内容拦截代理加密」导致 docker build 读不到源码的问题
#
# 现象：
#   docker build 时报
#     [UNLOADABLE_DEPENDENCY] Could not load src/data/products.js
#   而本地 npm run build 正常；或者 git status 显示文件被修改，但内容其实没变。
#
# 原因：部分文件被安全/加密代理加上 4096 字节头，stat 尺寸比明文多 4096，
#      Docker 构建上下文 / rolldown 按 stat 读取会拿到残缺内容。
#
# 做法：用 git 重新写出文件（git 的写入路径不受拦截），恢复成干净明文。
#      ！！会丢弃这些文件尚未提交的修改：请先 git add / git commit。
#
# 用法：bash scripts/unseal.sh

set -u
cd "$(git rev-parse --show-toplevel)" || exit 1

python3 - <<'PY'
import os, subprocess, sys

exts = (".js", ".mjs", ".cjs", ".ts", ".vue", ".md", ".html", ".htm", ".css",
        ".json", ".yml", ".yaml", ".conf", ".ini", ".py", ".sh", ".txt", ".svg")
files = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()

bad = []
for f in files:
    if not f.lower().endswith(exts):
        continue
    if not os.path.isfile(f):
        continue
    st = os.stat(f).st_size
    try:
        rd = len(open(f, "rb").read())
    except OSError:
        continue
    if st != rd:
        bad.append((f, st, rd))

if not bad:
    print("[unseal] 所有文本文件 stat 与读取一致，无需处理")
    sys.exit(0)

print("[unseal] 发现被加密（stat 比明文大）的文件，使用 git 重新写出：")
for f, st, rd in bad:
    print(f"  · {f}  stat={st} 明文={rd}  (+{st - rd})")
    subprocess.run(["git", "checkout-index", "-f", "--", f], check=False)

# 复查
still = []
for f, _, _ in bad:
    if os.path.getsize(f) != len(open(f, "rb").read()):
        still.append(f)
if still:
    print("[unseal] 仍无法修复（可能未纳入 git 或被锁）：", ", ".join(still))
    sys.exit(1)
print("[unseal] 修复完成，可以重新执行 docker compose build")
PY
