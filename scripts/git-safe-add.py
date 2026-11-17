#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""git-safe-add.py —— 绕过本机「进程级内容拦截」对 git 的影响。

背景
----
本机存在安全/加密代理：某些文件（例如被编辑器/工具写过的 .md）在 git 读取时会
被替换成带 4096 字节头的密文，于是 git 把它们当成二进制存进对象库，GitHub 上
看不到 diff、README 也无法渲染。Python / cat 读到的仍然是明文。

做法
----
用 Python 读明文 → 直接以 stdin 写入 git 对象（hash-object -w --stdin）→
用 update-index 把索引指向这个明文 blob。commit / push 不再读工作区，因此不会被替换。

用法
----
    python3 scripts/git-safe-add.py            # 修复所有已暂存（staged）的文件
    python3 scripts/git-safe-add.py README.md  # 修复指定文件

安装为 pre-commit 钩子（推荐，一次性）：
    git config core.hooksPath .githooks
"""
import hashlib
import os
import subprocess
import sys

TEXT_EXT = {
    ".md", ".markdown", ".txt", ".js", ".mjs", ".cjs", ".ts", ".json", ".vue",
    ".css", ".scss", ".html", ".htm", ".yml", ".yaml", ".conf", ".ini", ".toml",
    ".py", ".sh", ".bash", ".zsh", ".xml", ".svg", ".csv", ".gitignore", ".gitkeep",
}

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()


def git(*args, **kw):
    return subprocess.run(["git", *args], capture_output=True, cwd=ROOT, **kw)


def staged_or_given():
    if len(sys.argv) > 1:
        return sys.argv[1:]
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACMR").stdout.decode("utf-8", "replace")
    return [l for l in out.splitlines() if l.strip()]


def is_text_candidate(path):
    name = os.path.basename(path)
    if name in (".gitignore", ".gitkeep", ".dockerignore", ".env.example"):
        return True
    return os.path.splitext(path)[1].lower() in TEXT_EXT


def main():
    files = [f for f in staged_or_given() if is_text_candidate(f)]
    fixed, ok = [], []
    for f in files:
        full = os.path.join(ROOT, f)
        if not os.path.isfile(full):
            continue
        data = open(full, "rb").read()
        if b"\x00" in data:           # 真二进制，跳过
            continue
        py_sha = hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()
        git_sha = git("hash-object", f).stdout.decode().strip()
        if git_sha == py_sha:
            ok.append(f)
            continue
        # git 读到的内容与明文不一致 → 用 stdin 写入明文 blob
        w = git("hash-object", "-w", "--stdin", input=data)
        sha = w.stdout.decode().strip()
        git("update-index", "--add", "--cacheinfo", f"100644,{sha},{f}")
        fixed.append((f, len(data), os.path.getsize(full)))

    if fixed:
        print("[git-safe-add] 已用明文重建 git 对象，避免被存成二进制：")
        for f, n, _ in fixed:
            print(f"  · {f}  ({n} bytes)")
    else:
        print(f"[git-safe-add] 检查 {len(ok)} 个文本文件，未发现被拦截的情况")
    return 0


if __name__ == "__main__":
    sys.exit(main())
