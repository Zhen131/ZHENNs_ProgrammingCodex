#!/usr/bin/env python3
"""编程宝典体检脚本。在仓库根目录运行：python3 "00 工具与指南/check.py"

检查：断链、孤岛（没人链它）、frontmatter 缺字段、关联为空、文件名不合规。
零报错才算入库完成。只读，不改任何文件。
"""
import collections, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKIP_DIRS = ("00 工具与指南", ".obsidian", ".git")
REQUIRED = ("type", "status", "aliases", "created", "updated")
VALID_TYPE = {"技术卡片", "问题卡片", "素材"}
VALID_STATUS = {"草稿", "已校"}

files = [f for f in glob.glob("**/*.md", recursive=True)
         if not f.startswith(SKIP_DIRS) and os.sep in f]
names = {os.path.splitext(os.path.basename(f))[0]: f for f in files}
inbound = collections.Counter()
errors, warns = [], []

for f in files:
    text = open(f, encoding="utf-8").read()
    name = os.path.splitext(os.path.basename(f))[0]
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        errors.append(f"[无 frontmatter] {f}")
        continue
    fm = m.group(1)
    fields = dict(re.findall(r"^(\w+):\s*(.*)$", fm, re.M))
    for k in REQUIRED:
        if k not in fields:
            errors.append(f"[缺字段 {k}] {f}")
    if fields.get("type") and fields["type"] not in VALID_TYPE:
        errors.append(f"[type 不合法: {fields['type']}] {f}")
    if fields.get("status") and fields["status"] not in VALID_STATUS:
        errors.append(f"[status 不合法: {fields['status']}] {f}")
    if fields.get("type") == "技术卡片" and not re.match(r"^[A-Za-z0-9]", name):
        warns.append(f"[技术卡文件名应以英文开头: English Term（中文）] {f}")
    links = set()
    for l in re.findall(r"\[\[([^\]|#]+)", text):
        l = l.split("/")[-1].strip()
        if l == name or not l:
            continue
        links.add(l)
        if l in names:
            inbound[l] += 1
        else:
            errors.append(f"[断链 -> {l}] {f}")
    if fields.get("type") in ("技术卡片", "问题卡片"):
        if "## 关联" not in text:
            errors.append(f"[没有 ## 关联] {f}")
        elif not links:
            errors.append(f"[关联为空] {f}")

for n, f in names.items():
    if inbound[n] == 0:
        warns.append(f"[孤岛，没人链它] {f}")

print(f"卡片 {len(files)} 张")
for e in errors: print("ERROR", e)
for w in warns: print("WARN ", w)
print(f"错误 {len(errors)}，警告 {len(warns)}")
sys.exit(1 if errors else 0)
