---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [JavaScript 项目结构, TypeScript 项目结构, 前端项目结构, 项目根目录, 工程骨架]
created: 2026-06-29
updated: 2026-06-29
---

# JavaScript Project Structure（JavaScript 项目结构）

## 一句话

`JavaScript Project Structure（JavaScript 项目结构）` 是 JavaScript/TypeScript 工程根目录中源码、依赖、配置、缓存和工具文件的组织方式。

## 背景：它出现前的问题

初学者拿到一个 GitHub 项目后，容易把根目录里的所有文件都当成“必须理解的代码”。但现代前端项目会同时包含业务源码、依赖目录、构建缓存、Git 内部数据、TypeScript 配置、框架配置、测试配置和样式配置。

如果不先识别工程骨架，就会一头扎进 `node_modules/`、`.next/`、`.git/` 这类目录里，越看越乱。

## 它解决了什么

项目结构判断帮助读代码时先分层：

- 哪些是优先入口。
- 哪些是工具配置。
- 哪些是生成物或外部依赖。
- 哪些才是业务源码。

## 核心机制

拿到 JavaScript/TypeScript 项目时，可以先按三层判断。

第一层：优先看。

- `README.md`：项目做什么、怎么启动。
- [[package.json（项目清单）]]：项目命令、依赖和工具链。
- `src/`：通常是业务源码主线。

第二层：知道用途，遇到对应问题再深入。

- `tsconfig.json`
- `next.config.mjs`
- `tailwind.config.ts`
- `postcss.config.mjs`
- `.eslintrc.json`
- `vitest.config.ts`
- `next-env.d.ts`
- [[package-lock.json（依赖锁文件）]]
- `.gitignore`

第三层：基本别作为读项目入口。

- [[node_modules（依赖实体目录）]]：第三方依赖实体。
- `.next/`：[[Next.js（Next 应用框架）]] 生成的构建产物和缓存。
- `.git/`：Git 内部数据库。

## 典型使用场景

- `git clone` 一个项目后先判断读代码入口。
- 区分业务源码和工具生成物。
- 理解为什么前端项目根目录会有很多配置文件。
- 避免把第三方依赖和构建缓存当成当前项目源码。

## 局限性

目录约定会随框架变化。`src/` 不一定在所有项目中存在，配置文件也可能改名或换工具。这个卡片提供的是读项目的默认判断顺序，不是绝对规则。

## 和其他概念的关系

- [[Node.js（Node 运行环境）]] 提供运行开发工具的环境。
- [[npm（Node 包管理器）]] 通过 package.json 运行项目命令。
- [[Dependency（依赖）]] 帮助判断 package 在项目里的角色。
- [[Next.js（Next 应用框架）]] 会通过 `src/app/`、`page.tsx`、`layout.tsx`、`.next/` 等约定影响项目结构。
- [[为什么读 JavaScript 项目要先识别工程骨架]] 是对应问题入口。

## 进一步理解

- [[Next.js App Router（Next 应用路由）]]：`src/app/page.tsx` 和 `src/app/layout.tsx` 不是普通文件名，而是 Next.js 通过目录和文件名约定识别应用结构的例子。
- [[为什么 .next 不用读]]：`.next/` 是框架加工项目后的产物和缓存，不是业务源码入口。

## 关联

- [[package.json（项目清单）]]
- [[node_modules（依赖实体目录）]]
- [[Dependency（依赖）]]
- [[Next.js（Next 应用框架）]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
