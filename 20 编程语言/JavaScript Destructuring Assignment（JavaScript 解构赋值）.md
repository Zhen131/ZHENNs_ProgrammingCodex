---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/编程语言, 语言/JavaScript, 层级/基础]
aliases: [Destructuring Assignment, JavaScript Destructuring, Array Destructuring, Object Destructuring, 解构赋值, 数组解构, 对象解构, JavaScript 解构赋值]
created: 2026-07-05
updated: 2026-07-06
---

# JavaScript Destructuring Assignment（JavaScript 解构赋值）

## 一句话

`JavaScript Destructuring Assignment（JavaScript 解构赋值）` 是 JavaScript 中从数组或对象里取值，并同时赋给变量的语法。

## 背景：它出现前的问题

很多 React Hook 会返回数组，例如：

```ts
const [state, setState] = useState(initialState);
```

对不熟悉 JavaScript 的人来说，`const [A, B] = ...` 很像特殊 React 语法。其实它是普通 JavaScript 的解构赋值，不是 [[React（React UI 库）]] 独有的写法，也不是“数组这种数据结构”的基础概念。

这里的重点不是数组在内存里怎么存，而是 JavaScript 如何从一个值里拆出局部变量。所以它应该放在编程语言语法里，而不是放进计算机基础的数据结构里。

## 它解决了什么

数组解构让代码不用先保存整个数组，再按下标取值：

```ts
const result = useState(initialState);
const state = result[0];
const setState = result[1];
```

可以写成：

```ts
const [state, setState] = useState(initialState);
```

对象解构也类似，它按属性名取值：

```ts
const trade = { symbol: "BTC", amount: 0.01 };
const { symbol, amount } = trade;
```

## 核心机制

数组解构按位置取值，不按变量名匹配：

```ts
const pair = ["BTC", 100000];
const [symbol, price] = pair;
```

这里：

- `symbol` 得到 `"BTC"`。
- `price` 得到 `100000`。
- 变量名由开发者自己取。
- 真正决定含义的是数组里每个位置代表什么。

对象解构按属性名取值：

```ts
const { symbol, amount } = trade;
```

所以在 [[useState（React 状态 Hook）]] 里，`state` 和 `setState` 不是 React 强制的变量名，而是开发者按照惯例给返回数组里的两个位置起的名字。

## 典型使用场景

- 接收 React Hook 返回值，例如 `const [count, setCount] = useState(0)`。
- 接收 [[useReducer（React Reducer Hook）]] 返回值，例如 `const [state, dispatch] = useReducer(reducer, initialState)`。
- 从对象中取出常用字段，例如 `const { symbol, amount } = trade`。
- 交换两个变量。
- 从固定格式数组里提取多个值。

## 局限性

数组解构依赖位置。如果数组返回值顺序变了，变量含义也会跟着变。读代码时不能只看变量名，还要知道右侧函数返回数组的约定。

对象解构依赖属性名。如果字段名写错，取出来的值可能是 `undefined`。在 [[TypeScript（类型化 JavaScript）]] 项目里，类型检查可以帮助发现一部分字段名错误。

## 和其他概念的关系

- [[useState（React 状态 Hook）]] 的 `[state, setState]` 是数组解构。
- [[useReducer（React Reducer Hook）]] 的 `[state, dispatch]` 也是数组解构。
- [[TypeScript Generic（TypeScript 泛型）]] 解释 `useState<FormDraft>()` 里的尖括号类型写法。
- [[TypeScript（类型化 JavaScript）]] 可以在解构赋值时推断或标注类型。

## 关联

- [[useState（React 状态 Hook）]]
- [[useReducer（React Reducer Hook）]]
- [[TypeScript Generic（TypeScript 泛型）]]
- [[TypeScript（类型化 JavaScript）]]
