---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [DOM, Document Object Model, 文档对象模型, DOM 树]
created: 2026-07-05
updated: 2026-07-05
---

# DOM（文档对象模型）

## 一句话

`DOM（文档对象模型）` 是浏览器把 HTML 解析后，在内存中生成的页面结构树，也是 JavaScript 可以读取和修改页面的对象结构。

## 背景：它出现前的问题

浏览器不能直接把一段 HTML 字符串当成可交互页面来操作。它需要先把 HTML 里的标签、文字、属性和层级关系变成一套运行时对象，这样 JavaScript 才能找到某个按钮、段落或输入框，并响应用户操作。

## 它解决了什么

DOM 让页面从“写在文件里的 HTML”变成“浏览器可以操作的对象树”：

- HTML 是源代码里的页面结构。
- DOM 是浏览器读完 HTML 后生成的内存结构。
- JavaScript 可以通过 DOM API 找到节点、读取内容、修改内容或绑定事件。

在账本页面里，可以把 HTML 类比成装修图纸，把 DOM 类比成浏览器真正搭出来的房子结构。

## 核心机制

HTML 结构会被浏览器解析成一棵树。比如 `body` 下面有标题、列表、按钮和输入框，这些元素在 DOM 里会变成有父子关系的节点。

传统 JavaScript 可以直接操作 DOM：

```js
document.querySelector("p").innerText = "BTC 持仓：0.02";
```

这类代码的意思是：先在 DOM 树里找到某个页面元素，再手动修改它显示的内容。

## 典型使用场景

- 读取用户点击了哪个按钮。
- 修改某个页面元素的文字。
- 给表单、按钮或列表绑定事件。
- 理解 [[React（React UI 库）]] 为什么不鼓励在组件里到处手动 `querySelector`。

## 局限性

DOM 本身只是页面对象结构，不负责保证业务数据一致。复杂页面里，如果开发者手动修改很多 DOM 节点，很容易出现某些区域更新了、另一些区域忘了更新的问题。

在账本项目里，一笔交易可能同时影响交易列表、资产汇总、平均成本和盈亏。如果每个地方都靠手动 DOM 更新，就很容易让页面和真实数据不同步。

## 和其他概念的关系

- [[JavaScript Runtime（JavaScript 运行时）]] 解释浏览器为什么会给 JavaScript 提供 `document` 和 DOM 能力。
- [[React（React UI 库）]] 把常见前端思路从“手动改 DOM”转向“更新状态后重新渲染界面”。
- [[React State（React 状态）]] 是 React 用来驱动页面变化的关键数据。
- [[为什么 React 不推荐手动操作 DOM]] 是 DOM 在复杂前端项目中的问题入口。

## 关联

- [[React（React UI 库）]]
- [[React State（React 状态）]]
- [[JavaScript Runtime（JavaScript 运行时）]]
- [[为什么 React 不推荐手动操作 DOM]]
