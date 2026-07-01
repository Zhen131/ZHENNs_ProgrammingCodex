---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/读项目, 领域/软件工程, 语言/JavaScript]
aliases: [为什么先看 package.json, package.json 为什么重要, JavaScript 项目入口]
created: 2026-06-29
updated: 2026-07-01
---

# 为什么 package.json 是读 JavaScript 项目的入口

## 痛点

JavaScript/TypeScript 项目根目录里常常同时出现源码、配置文件、依赖目录、构建缓存和工具文件。初学者如果不知道从哪里开始，很容易把所有文件都当成同等重要。

这会导致一个实际问题：还没进入业务代码，就先被大量工具和依赖淹没。

## 以前怎么解决

没有 package.json 这类统一入口时，开发者需要靠文档、口头说明或手动猜测项目怎么启动、怎么测试、依赖了什么工具。项目越复杂，这种猜测成本越高。

## 技术演进

[[package.json（项目清单）]] 把项目信息集中到一个标准位置：

- `scripts` 记录命令菜单，也就是 [[npm scripts（npm 脚本）]]。
- `dependencies` 记录运行时依赖。
- `devDependencies` 记录开发、测试、构建依赖。
- 项目名称、版本、私有性等元信息也在这里。

[[npm（Node 包管理器）]] 则根据 package.json 执行 `npm run dev`、`npm test`、`npm run build` 等命令。

这几个文件和目录的关系可以先压缩成一张心智图：

```text
package.json          项目说明书：命令和依赖声明
scripts               常用命令的快捷名字
dependencies          运行时需要 npm 安装的包
devDependencies       开发、测试、构建时需要 npm 安装的包
node_modules          npm 实际下载到本地的包
node_modules/.bin     本地包暴露出来的可执行命令
package-lock.json     npm 自动记录的精确安装结果
```

## 相关技术

- [[package.json（项目清单）]]
- [[npm（Node 包管理器）]]
- [[npm scripts（npm 脚本）]]
- [[Dependency（依赖）]]
- [[Package（软件包）]]
- [[node_modules（依赖实体目录）]]
- [[package-lock.json（依赖锁文件）]]
- [[JavaScript Project Structure（JavaScript 项目结构）]]

## 我的理解

package.json 不是业务代码，但它是读项目的导航。它告诉我项目怎么跑、用了哪些技术、哪些命令是作者希望开发者使用的。

更准确地说，package.json 是声明入口，npm 是执行者，node_modules 是安装结果，package-lock.json 是精确安装记录。读项目先看 package.json，是为了先知道“这个项目想怎么被启动、测试、构建，以及它依赖哪些外部能力”。

所以拿到 JavaScript 项目后，比起先打开 `node_modules/`，更合理的顺序是：

```text
README.md
package.json
src/
```

## 关联

- [[为什么不要从 node_modules 读项目]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
