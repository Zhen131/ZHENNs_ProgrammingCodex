---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [dependency, dependencies, devDependencies, 依赖, 运行时依赖, 开发依赖]
created: 2026-06-29
updated: 2026-06-29
---

# Dependency（依赖）

## 一句话

`Dependency（依赖）` 是项目为了运行、开发、测试或构建而需要的外部 package。

## 背景：它出现前的问题

项目依赖第三方 package 后，初学者容易把所有依赖都看成“项目运行时必须要的东西”，也容易把 `node_modules/` 中成千上万的文件误认为当前项目的业务源码。

## 它解决了什么

依赖分类帮助工程师判断一个 package 在项目中的角色：

- `dependencies（运行时依赖）`：项目实际运行时需要。
- `devDependencies（开发依赖）`：开发、测试、构建、类型检查、代码检查时需要。

这个区分能帮助理解项目结构和工具链，而不是把所有 package 混在一起。

## 核心机制

在 [[package.json（项目清单）]] 中，依赖通常分成：

```json
{
  "dependencies": {
    "next": "14.2.35",
    "react": "^18",
    "decimal.js": "^10.6.0"
  },
  "devDependencies": {
    "typescript": "^5",
    "vitest": "^4.1.9",
    "eslint": "^8"
  }
}
```

还要区分：

- 直接依赖：当前项目自己声明的 package。
- 传递依赖：某个 package 自己依赖的其他 package。

[[node_modules（依赖实体目录）]] 变大，常常是因为传递依赖很多。

## 典型使用场景

- 判断 `decimal.js` 这类库是否属于业务运行所需。
- 判断 `vitest`、`eslint`、`typescript` 是否主要服务开发流程。
- 读项目时通过 package.json 快速识别技术栈。
- 排查为什么 node_modules 中出现了自己没有直接声明的包。

## 局限性

依赖分类是工程约定，不等于所有项目都绝对准确。有些工具可能既影响构建也影响运行，所以具体还要结合项目脚本、框架和部署方式判断。

## 和其他概念的关系

- [[Package（软件包）]] 是依赖的实体单元。
- [[package.json（项目清单）]] 声明依赖分类。
- [[package-lock.json（依赖锁文件）]] 锁定依赖树的精确版本。
- [[为什么要区分 dependencies 和 devDependencies]] 是这个概念背后的问题入口。

## 关联

- [[Package（软件包）]]
- [[package.json（项目清单）]]
- [[node_modules（依赖实体目录）]]
- [[为什么要区分 dependencies 和 devDependencies]]
