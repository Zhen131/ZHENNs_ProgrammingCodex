---
name: programming-knowledge-ingest
description: Import programming knowledge into the 编程宝典 Obsidian vault. Use when the user asks to入库, add a learning packet, create or update technical cards, maintain direct Obsidian wikilinks/tags, or connect new programming knowledge to existing notes.
---

# Programming Knowledge Ingest

Use this skill inside the `编程宝典` vault.

The goal is not just to create files. The goal is to keep the programming knowledge graph connected, searchable, and useful for future coding.

## Required Reading

Before editing, read:

- `AGENTS.md`
- `00 工具与指南/编程知识入库指南.md`

## Workflow

1. Read the incoming material.
   - It may be a learning packet, rough note, copied explanation, project debugging summary, or direct user instruction.

2. Search for existing nodes.
   - Search English terms.
   - Search Chinese translations.
   - Search abbreviations and aliases.
   - Search related frameworks, languages, and problem names.

3. Classify the material.
   - Stable concept: create or update a technical card.
   - Pain point: create or update a problem card.
   - Immature material: place in `90 素材与临时笔记`.

4. Decide create vs update.
   - Update existing notes when they already cover the concept.
   - Create new notes only when the concept is meaningfully distinct.
   - Add `aliases` instead of duplicating notes for naming variants.

5. Write connected notes.
   - Use Chinese reasoning and English technical terms.
   - Use `English Term（中文翻译）.md` for technical cards.
   - Add YAML frontmatter.
   - Add inline `[[wikilink]]` in the body.
   - Add a non-empty `## 关联` section.

6. Update old notes.
   - If a new note deepens an old note, append a short `## 进一步理解` entry to the old note.
   - If a problem card points to a technology, make sure the technology card links back where useful.

7. Verify direct graph links.
   - Technical cards should link to related technical cards directly.
   - Problem cards should link to the technical cards that solve the pain point.
   - Project context should appear inside the relevant technical/problem cards, not as a separate aggregation note.
   - Do not create extra routing files or aggregation notes as a navigation layer.

8. Verify.
   - Confirm new files are in the right folder.
   - Confirm links are not empty placeholders.
   - Confirm no duplicate note was created.
   - Report changed files and any uncertain decisions.

## Placement Rules

- `10 计算机基础`: low-level and foundational CS concepts.
- `20 编程语言`: language syntax, type systems, runtime behavior, language-specific concepts.
- `30 软件工程`: architecture, testing, refactoring, Git, CI/CD, design patterns.
- `40 Web与网络`: browser, frontend/backend, HTTP, TCP/IP, web frameworks.
- `50 数据与存储`: databases, cache, indexes, transactions, storage models.
- `60 AI与编程工具`: LLM, AI coding, MCP, NLP, Embedding, Tokenization, developer tools.
- `80 问题与痛点`: why/how problem cards.
- `90 素材与临时笔记`: raw material not ready to become stable knowledge.

## Completion Report

After入库, report:

- Created files
- Updated files
- Main links added
- Items left as `待确认`
