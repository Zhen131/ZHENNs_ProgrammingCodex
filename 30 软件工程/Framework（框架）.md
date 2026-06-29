---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 层级/基础]
aliases: [Framework, 框架, 应用框架, Web Framework]
created: 2026-06-29
updated: 2026-06-29
---

# Framework（框架）

## 一句话

`Framework（框架）` 是一套组织应用的规则和工具，它不只是一个函数库，而是规定项目结构、运行方式和协作约定的体系。

## 背景：它出现前的问题

“框架”这个词很抽象，初学者容易觉得它像玄学：既不是一个具体按钮，也不是某个业务函数。但在真实项目里，框架会以代码实体、目录约定、命令和构建流程的形式存在。

## 它解决了什么

Framework 降低了组织完整应用的成本。它通常会回答：

- 文件放哪里。
- 路由怎么对应。
- 开发服务器怎么启动。
- 项目怎么构建。
- 代码如何被编译、打包或渲染。
- 部署时需要什么产物。

## 核心机制

可以先区分 library 和 framework：

```text
Library（库）：给你一个具体能力。
Framework（框架）：给你一套组织应用的规则和流程。
```

[[React（React UI 库）]] 更像 UI library，核心是 component。[[Next.js（Next 应用框架）]] 更像 application framework，在 React 之上规定页面、路由、布局、构建和运行。

## 典型使用场景

- Next.js 规定 `src/app/page.tsx` 对应页面。
- Next.js 规定 `src/app/layout.tsx` 对应布局。
- 通过 `npm run dev` 启动开发服务器。
- 通过构建命令生成可部署产物。

## 局限性

框架降低组织成本，也引入了约定成本。初学者需要同时理解“自己写的源码”和“框架为什么赋予某些文件特殊意义”。

## 和其他概念的关系

- [[Next.js（Next 应用框架）]] 是这次学习中的具体框架例子。
- [[Package（软件包）]] 可以是框架、库或工具。
- [[JavaScript Project Structure（JavaScript 项目结构）]] 帮助识别框架配置和生成物。
- [[React 和 Next.js 有什么区别]] 解释了 UI library 和 application framework 的区别。

## 在项目中的表现

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]：这次学习把框架从抽象词理解成“代码、规则、约定和运行流程”。

## 关联

- [[Next.js（Next 应用框架）]]
- [[React（React UI 库）]]
- [[JavaScript Project Structure（JavaScript 项目结构）]]
- [[React 和 Next.js 有什么区别]]
