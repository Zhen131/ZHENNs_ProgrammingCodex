---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/读项目, 领域/软件工程, 语言/JavaScript]
aliases: [为什么先看 package.json, package.json 为什么重要, JavaScript 项目入口]
created: 2026-06-29
updated: 2026-06-29
---

# 为什么 package.json 是读 JavaScript 项目的入口

## 痛点

JavaScript/TypeScript 项目根目录里常常同时出现源码、配置文件、依赖目录、构建缓存和工具文件。初学者如果不知道从哪里开始，很容易把所有文件都当成同等重要。

这会导致一个实际问题：还没进入业务代码，就先被大量工具和依赖淹没。

## 以前怎么解决

没有 package.json 这类统一入口时，开发者需要靠文档、口头说明或手动猜测项目怎么启动、怎么测试、依赖了什么工具。项目越复杂，这种猜测成本越高。

## 技术演进

[[package.json（项目清单）]] 把项目信息集中到一个标准位置：

- `scripts` 记录命令菜单。
- `dependencies` 记录运行时依赖。
- `devDependencies` 记录开发、测试、构建依赖。
- 项目名称、版本、私有性等元信息也在这里。

[[npm（Node 包管理器）]] 则根据 package.json 执行 `npm run dev`、`npm test`、`npm run build` 等命令。

## 相关技术

- [[package.json（项目清单）]]
- [[npm（Node 包管理器）]]
- [[Dependency（依赖）]]
- [[Package（软件包）]]
- [[JavaScript Project Structure（JavaScript 项目结构）]]

## 我的理解

package.json 不是业务代码，但它是读项目的导航。它告诉我项目怎么跑、用了哪些技术、哪些命令是作者希望开发者使用的。

所以拿到 JavaScript 项目后，比起先打开 `node_modules/`，更合理的顺序是：

```text
README.md
package.json
src/
```

## 关联

- [[为什么不要从 node_modules 读项目]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
