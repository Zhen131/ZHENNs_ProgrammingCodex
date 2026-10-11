#!/usr/bin/env python3
"""编程宝典体检脚本。在仓库根目录运行：python3 "00 工具与指南/check.py"

检查：断链、孤岛（没人链它）、frontmatter 缺字段、关联为空、文件名不合规。
另外按《写作规范》报 WARN：名词堆、语气词、关联里的裸链接。
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
        body = re.sub(r"```.*?```", "", text[m.end():], flags=re.S)
        # 名词堆：连续 >=4 个列表项，每项去掉标点后不超过 8 个字
        run = 0
        for line in body.split("\n"):
            item = re.match(r"\s*[-*]\s+(.*)", line)
            if item and len(re.sub(r"[。．.，、：:；;\s`]", "", item.group(1))) <= 8:
                run += 1
                if run == 4:
                    warns.append(f"[名词堆：连续 4 个短列表项，改成句子] {f}")
            else:
                run = 0
        tone = re.findall(r"(啊|呢|嘛|呀|对不对|对吧)[，。！？\n]", body)
        if tone:
            warns.append(f"[语气词 {len(tone)} 处] {f}")
        bare = re.findall(r"^- \[\[[^\]]+\]\]\s*$", body, re.M)
        if len(bare) >= 3:
            warns.append(f"[关联里 {len(bare)} 条裸链接没写关系] {f}")
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
