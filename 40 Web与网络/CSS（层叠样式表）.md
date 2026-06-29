---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 层级/基础]
aliases: [CSS, Cascading Style Sheets, 层叠样式表, 网页样式语言]
created: 2026-06-29
updated: 2026-06-29
---

# CSS（层叠样式表）

## 一句话

`CSS（Cascading Style Sheets，层叠样式表）` 是网页样式语言，用来控制页面元素的颜色、字体、布局、间距、大小、背景和响应式变化。

## 背景：它出现前的问题

网页不仅需要结构和内容，还需要视觉呈现。按钮、表格、表单和页面布局都需要样式规则，否则界面难以阅读和使用。

## 它解决了什么

CSS 负责表达界面的视觉层：

- 颜色。
- 字体。
- 边距。
- 布局。
- 宽度和高度。
- 背景。
- 边框。
- 响应式变化。

如果 [[React（React UI 库）]] component 是界面零件，那么 CSS 可以理解成给零件上颜色、定尺寸、摆位置的规则。

## 核心机制

CSS 是浏览器理解的样式语言。[[Tailwind CSS（Tailwind 样式工具）]] 不是替代 CSS 的新语言，而是建立在 CSS 之上的工具体系，最终仍然生成 CSS。

## 典型使用场景

- 控制按钮颜色和大小。
- 控制表格布局。
- 设置页面整体间距。
- 处理不同屏幕尺寸下的响应式布局。

## 局限性

CSS 规则分散、命名和层叠关系复杂时，样式也会变得难维护。这也是 Tailwind 等工具出现的背景之一。

## 和其他概念的关系

- [[Tailwind CSS（Tailwind 样式工具）]] 是基于 CSS 的样式工具。
- [[React（React UI 库）]] 负责 UI component，CSS 负责视觉样式。
- [[Tailwind 和 CSS 是一回事吗]] 解释了语言和工具的区别。

## 在项目中的表现

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]：这次学习把 CSS/Tailwind 放在“控制界面样式”的层级。

## 关联

- [[Tailwind CSS（Tailwind 样式工具）]]
- [[React（React UI 库）]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
- [[Tailwind 和 CSS 是一回事吗]]
