---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [JSX, JavaScript XML]
created: 2026-06-29
updated: 2026-06-29
---

# JSX（JavaScript XML）

## 一句话

`JSX（JavaScript XML）` 是一种让 JavaScript 代码里可以描述类似 HTML 界面结构的语法，常用于写 React component。

## 背景：它出现前的问题

前端界面既需要结构，又需要逻辑。传统直觉会把 HTML 放在 HTML 文件里，把 JavaScript 放在 JS 文件里。但 React 的组件化思路更关注“一个界面组件的结构和逻辑如何放在一起表达”。

## 它解决了什么

JSX 让开发者可以在 JavaScript 中直接描述界面结构：

```jsx
<button>新增交易</button>
```

它看起来像 HTML，但不是普通 HTML 文件。工具会把 JSX 转换成 React 能理解的界面描述。

## 核心机制

JSX 是语法层，不是应用框架。它通常和 [[React（React UI 库）]] 一起出现，用来描述 [[UI Component（UI 组件）]] 的界面结构。

如果项目使用 TypeScript，那么常见形式就是 [[TSX（TypeScript XML）]]。

## 典型使用场景

- 在 React component 中返回按钮、表单、列表、表格。
- 用条件判断决定是否显示某块 UI。
- 把数组数据渲染成列表项。

## 局限性

JSX 不是浏览器原生直接执行的 HTML。它需要被构建工具转换。初学时如果只看外观，很容易误以为 JSX 就是 HTML。

## 和其他概念的关系

- [[TSX（TypeScript XML）]] 是 TypeScript + JSX。
- [[React（React UI 库）]] 常用 JSX 描述 component。
- [[TSX 和 Next.js 是一回事吗]] 解释了语法和框架的区别。

## 在项目中的表现

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]：这次学习把 JSX/TSX 理解为“在代码里描述界面长什么样的语法”。

## 关联

- [[TSX（TypeScript XML）]]
- [[React（React UI 库）]]
- [[UI Component（UI 组件）]]
- [[为什么需要 JSX 或 TSX]]
