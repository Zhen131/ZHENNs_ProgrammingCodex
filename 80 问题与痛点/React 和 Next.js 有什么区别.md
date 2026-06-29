---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/前端框架, 领域/Web与网络, 语言/JavaScript]
aliases: [React vs Next.js, React 和 Next 的区别, React 和 Next.js 区别]
created: 2026-06-29
updated: 2026-06-29
---

# React 和 Next.js 有什么区别

## 痛点

读账本项目前端代码时，很容易把 [[React（React UI 库）]] 和 [[Next.js（Next 应用框架）]] 混成一团：React 是不是框架？Next.js 是不是主要提供 UI？为什么两个名字总是一起出现？

## 以前怎么解决

如果只记“Next.js 基于 React”，还是不够。这个说法没有告诉我两者分别负责什么，于是看到 `page.tsx`、`layout.tsx`、component、route、build 时仍然会混乱。

## 技术演进

可以先这样分层：

- React 负责写 [[UI Component（UI 组件）]]，也就是界面零件。
- Next.js 负责组织完整应用，包括页面、路由、布局、开发服务器、构建和部署适配。

所以：

```text
React 是 UI 层。
Next.js 是应用框架层。
```

## 相关技术

- [[React（React UI 库）]]
- [[Next.js（Next 应用框架）]]
- [[Framework（框架）]]
- [[Next.js App Router（Next 应用路由）]]
- [[TSX（TypeScript XML）]]

## 我的理解

React 更像“造和拼 UI 零件”的能力，Next.js 更像“这些零件如何组成网站应用”的规则体系。`page.tsx` 本质上还是 React component，但它被 Next.js 的规则识别成页面。

## 关联

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
- [[TSX 和 Next.js 是一回事吗]]
