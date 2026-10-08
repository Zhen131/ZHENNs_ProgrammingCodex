---
type: 技术卡片
status: 草稿
tags: [领域/软件工程, 语言/JavaScript]
aliases: [Next.js, Next, Next 应用框架, next, Next React Framework]
created: 2026-06-29
updated: 2026-10-08
---

# Next.js（Next 应用框架）

## 一句话

Next.js 是搭在 React 上面的一层框架。React 只管怎么造零件，Next.js 管这些零件怎么拼成一个完整的网站：哪个文件是哪个页面、页面之间怎么跳、怎么打包上线。

## 背景：它出现前的问题

你学会了 [[React（React UI 库）]]，会写组件了。然后打开一个真实项目，看到 `src/app/page.tsx`、`src/app/layout.tsx`、`.next/`、`next.config.mjs`——这些 React 教程里一个都没讲过。

因为 React 本身不管这些。一个能上线的网站还需要路由（URL 对应哪个页面）、公共布局（每页都有的导航栏）、开发服务器、打包构建、服务端渲染、部署适配。以前这些要你自己拼一堆工具。Next.js 把它们打包成一套约定：你按它的规矩放文件，剩下的它来。

## 核心机制

Next.js 是一个 [[Framework（框架）]]，意思是它规定了你的代码怎么组织，而不是你调用它。几个你一定会碰到的东西：

- 本体在 `node_modules/next/`，是你安装的依赖，不是你写的。
- `src/app/page.tsx` 是首页。在 `src/app/` 下新建一个目录再放一个 `page.tsx`，就多了一个页面，URL 就是目录名。这套规则叫 [[Next.js App Router（Next 应用路由）]]。
- `src/app/layout.tsx` 是所有页面共用的外壳，导航栏、字体、全局样式都放这里。
- `.next/` 是构建出来的产物和缓存，不是源码。读项目时跳过它，见 [[为什么 .next 不用读]]。
- `next.config.mjs` 是配置。

关键一点：`page.tsx` 和 `layout.tsx` 本身就是普通的 React 组件，用 [[TSX（TypeScript XML）]] 写。它们之所以"特殊"，只是因为被放在了 Next.js 约定的位置上。换个目录，它们就是普通文件。

## 典型使用场景

`npm run dev` 启动开发服务器，改代码页面自动刷新。加一个 `src/app/settings/page.tsx`，就有了 `/settings` 页面。`npm run build` 打包成可以部署的产物。

## 局限性

框架约定是双刃剑：它省掉了你拼工具的功夫，代价是你得记住哪些文件名、哪些目录有特殊含义。不知道规矩的时候，`layout.tsx` 为什么会自动包住所有页面这件事会很玄学。

另外 Next.js 不造零件。界面长什么样还是 React + CSS 的事，它只负责把零件放到对的页面上。

## 容易混淆

**React 和 Next.js 有什么区别？** React 是 UI 库，Next.js 是用 React 搭完整应用的框架。详见 [[React 和 Next.js 有什么区别]]。

**TSX 和 Next.js 是一回事吗？** 不是。TSX 是文件语法，Next.js 是框架；Next.js 项目里有很多 `.tsx` 文件只是因为它基于 React。详见 [[TSX 和 Next.js 是一回事吗]]。

## 关联

- [[React（React UI 库）]]：Next.js 的地基，所有零件都是 React 组件。
- [[UI Component（UI 组件）]]：Next.js 拼的就是这些零件。
- [[Framework（框架）]]：Next.js 是框架，意味着它规定你的代码怎么组织。
- [[Next.js App Router（Next 应用路由）]]：`page.tsx`、`layout.tsx` 这套文件约定的具体规则。
- [[JavaScript Project Structure（JavaScript 项目结构）]]：`.next/`、`node_modules/next/`、`next.config.mjs` 各在项目里什么位置。
- [[为什么 .next 不用读]]：构建产物为什么不算源码。
