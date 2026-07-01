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
package.json          遥控器说明书 / 按钮面板
scripts               遥控器上的按钮
npm                   真正按按钮并解释按钮含义的人
dependencies          运行时要安装的机器和零件
devDependencies       开发、测试、构建时要安装的机器和零件
node_modules          真实安装在本地的机器和零件
node_modules/.bin     这些机器暴露出来的开关入口
package-lock.json     机器和零件的精确型号清单，不是运行日志
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

读 `scripts` 时还可以记住一个左右关系：

```text
左边：我给按钮起的名字
右边：npm 或工具真正要执行的东西
```

例如 `"dev": "next dev"` 里，`dev` 是按钮名，`next dev` 是按下按钮后真正要执行的命令。npm 会去 `node_modules/.bin/next` 找到本地安装的 Next.js 命令入口，然后由 [[Next.js（Next 应用框架）]] 启动开发服务器。

所以拿到 JavaScript 项目后，比起先打开 `node_modules/`，更合理的顺序是：

```text
README.md
package.json
src/
```

## 关联

- [[为什么不要从 node_modules 读项目]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
