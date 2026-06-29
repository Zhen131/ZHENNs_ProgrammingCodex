---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [Next App Router, App Router, Next 应用路由, page.tsx, layout.tsx]
created: 2026-06-29
updated: 2026-06-29
---

# Next.js App Router（Next 应用路由）

## 一句话

`Next.js App Router（Next 应用路由）` 是 Next.js 中通过 `src/app/` 目录和特殊文件名组织页面、路由和布局的约定。

## 背景：它出现前的问题

`layout.tsx` 和 `page.tsx` 本质上看起来都像 React component，但它们放进 `src/app/` 后会突然拥有特殊意义。初学者容易困惑：这是 React 规定的，还是 Next.js 规定的？

## 它解决了什么

App Router 让 Next.js 可以根据目录和文件名自动理解应用结构：

- 哪个文件是页面。
- 哪个文件是布局。
- 哪个目录对应哪个路由。
- 哪些 UI 会作为共同外壳复用。

## 核心机制

在 Next.js 项目里：

```text
src/app/page.tsx
```

通常表示首页 `/`。

```text
src/app/layout.tsx
```

通常表示页面的共同外壳，例如整体 HTML 结构、公共字体、公共布局、全局样式入口等。

关键理解是：

```text
layout.tsx 和 page.tsx 是 React component。
但它们被 Next.js 识别成特殊页面结构。
```

[[React（React UI 库）]] 负责组件怎么写，[[Next.js（Next 应用框架）]] 负责这些组件在应用里扮演什么角色。

## 典型使用场景

- `src/app/page.tsx`：定义首页页面。
- `src/app/layout.tsx`：定义全局布局和共同外壳。
- 在 `src/app/` 下增加目录，形成更多页面路径。

## 局限性

这是一套框架约定，不是 TSX 文件语法本身。脱离 Next.js 的 `src/app/` 规则，`page.tsx` 和 `layout.tsx` 不会自动拥有同样的应用含义。

## 和其他概念的关系

- [[Next.js（Next 应用框架）]] 提供 App Router 规则。
- [[TSX（TypeScript XML）]] 是 `page.tsx`、`layout.tsx` 的文件语法。
- [[UI Component（UI 组件）]] 是这些文件的 React 本质。
- [[TSX 和 Next.js 是一回事吗]] 解释语法和框架规则的区别。

## 在项目中的表现

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]：这次学习把 `page.tsx` 理解为页面文件，把 `layout.tsx` 理解为共同外壳。

## 关联

- [[Next.js（Next 应用框架）]]
- [[TSX（TypeScript XML）]]
- [[React（React UI 库）]]
- [[为什么 .next 不用读]]
