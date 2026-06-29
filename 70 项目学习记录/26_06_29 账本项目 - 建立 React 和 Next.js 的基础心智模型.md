---
type: 项目学习记录
project: Local-First Trading Ledger
date: 2026-06-29
tags: [类型/项目学习记录, 项目/Local-First-Trading-Ledger, 领域/Web与网络, 语言/JavaScript, 语言/TypeScript]
created: 2026-06-29
updated: 2026-06-29
---

# 26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型

## 项目背景

这次学习发生在 `Local-First Trading Ledger` 账本项目。相关目录和文件包括：

- `src/app/`
- `src/app/layout.tsx`
- `src/app/page.tsx`
- `src/components/`
- `tailwind.config.ts`
- `next.config.mjs`
- `.next/`
- `node_modules/next/`

## 当时卡住的问题

我遇到了很多新概念：React、Next.js、Component、JSX、TSX、CSS、Tailwind CSS、`layout.tsx`、`page.tsx`、`.next/`。

真正卡住的不是某一行代码，而是不知道这些概念分别处在什么层级：

- React 到底是干什么的？
- Next.js 到底是干什么的？
- TSX 是不是 Next.js？
- Tailwind 和 CSS 是什么关系？
- 为什么 `page.tsx` 放在 `app` 目录里就变成页面？
- 为什么前端项目要分这么多层？

## 学到的内容

这次先建立一个临时心智模型，不追求完全理解底层原理：

```text
React 负责造和拼 UI 零件。
JavaScript / TypeScript 负责写这些零件的行为逻辑。
JSX / TSX 负责在代码里描述界面长什么样。
CSS / Tailwind 负责控制界面的样式。
Next.js 负责规定这些零件如何变成一个完整网站应用。
```

更具体地说：

- [[React（React UI 库）]] 是用来写 UI 的库。
- [[UI Component（UI 组件）]] 是界面零件。
- [[TypeScript（类型化 JavaScript）]] 帮助描述业务对象和组件数据结构。
- [[JSX（JavaScript XML）]] / [[TSX（TypeScript XML）]] 是描述界面结构的语法。
- [[CSS（层叠样式表）]] / [[Tailwind CSS（Tailwind 样式工具）]] 控制界面样式。
- [[Next.js（Next 应用框架）]] 是基于 React 的应用框架。
- [[Next.js App Router（Next 应用路由）]] 让 `page.tsx` 和 `layout.tsx` 拥有特殊意义。

## 已经校正的误区

- React 不是随便用 C / Python 写；普通 React 前端项目主要用 JavaScript / TypeScript。
- [[TSX（TypeScript XML）]] 不是 [[Next.js（Next 应用框架）]]。
- Next.js 不是主要提供 UI，React 更负责 UI，Next.js 更负责应用结构、路由、构建和运行。
- `.next/` 不是工具包本体，`node_modules/next/` 才是 Next.js package 实体。

## 应该沉淀的技术卡片

- [[React（React UI 库）]]
- [[UI Component（UI 组件）]]
- [[TypeScript（类型化 JavaScript）]]
- [[JSX（JavaScript XML）]]
- [[TSX（TypeScript XML）]]
- [[CSS（层叠样式表）]]
- [[Tailwind CSS（Tailwind 样式工具）]]
- [[Framework（框架）]]
- [[Next.js（Next 应用框架）]]
- [[Next.js App Router（Next 应用路由）]]

## 相关问题卡片

- [[React 和 Next.js 有什么区别]]
- [[TSX 和 Next.js 是一回事吗]]
- [[Tailwind 和 CSS 是一回事吗]]
- [[为什么 .next 不用读]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
- [[为什么需要 JSX 或 TSX]]

## 后续要补的内容

- [ ] 为什么前端界面会发展成用 JavaScript 管理？
- [ ] JSX / TSX 最后是怎么变成浏览器能理解的内容的？
- [ ] 没有 Next.js 时，React 项目通常怎么组织？
- [ ] Tailwind 的好处、代价和适用场景是什么？
- [ ] `next dev` 启动时到底发生了什么？
- [ ] `.next/` 里具体生成了什么？

## 关联

- [[26_06_29 账本项目 - 理解 Node.js、npm 与 node_modules]]
- [[JavaScript Project Structure（JavaScript 项目结构）]]
- [[Next.js（Next 应用框架）]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
