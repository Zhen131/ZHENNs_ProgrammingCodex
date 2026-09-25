---
type: 技术卡片
status: 已整理
tags: [类型/技术卡片, 领域/AI, 层级/基础]
aliases: [Reinforcement Learning, RL, 强化学习, Agent, Environment, State, Action, Reward, Policy]
created: 2026-09-23
updated: 2026-09-25
---

# Reinforcement Learning（强化学习）

## 一句话

Reinforcement Learning 让 Agent（智能体）在环境中不断试错，依靠奖励信号学会"在什么状态下做什么动作"，从而拿到长期最高回报。

## 背景：它出现前的问题

有一类问题既没有现成的标准答案可以标注，又需要连续做决策：下棋、走迷宫、控制机器人、做交易。而且每一步"对不对"往往要很久之后才知道——一笔买入要过几天才知道赚没赚。

[[Supervised Learning（监督学习）]] 要求每一步都有正确答案，在这里用不上。强化学习换了个思路：不告诉你答案，只在事后告诉你"做得好不好"。

## 核心组件

- **Agent（智能体）**：决策者，例如交易 AI。
- **Environment（环境）**：Agent 所处的世界，例如 K 线市场。
- **State（状态）**：Agent 对当前环境的观测，例如最近 N 根 K 线、当前持仓。
- **Action（动作）**：Agent 可以做的选择，例如买入 / 卖出 / 持有。
- **Reward（奖励）**：环境对动作的反馈，例如赚钱是正奖励、亏损是负奖励。

最初记住的是 Agent、State、Environment、Reward 四个；Action 同样必不可少——没有动作，Agent 就无法影响环境。Agent 最终学到的东西叫 **Policy（策略）**：从 State 到 Action 的映射。

## 核心机制

```text
State → Agent 选择 Action → Environment 返回新的 State 和 Reward → 循环
```

目标是最大化**长期累计奖励**，而不是只看眼前这一步。Agent 在大量试错中慢慢学会：哪些动作在哪些状态下最终能拿到最高收益。

## 典型使用场景

- 游戏与棋类 AI、走迷宫。
- 机器人控制。
- 交易、资源调度等连续决策问题。

## 局限性

- **浅层强化学习需要人工设计状态**：例如 K 线交易，要先手动算好 MACD、均线、涨幅、顶背离等技术指标作为 State，Agent 自己无法从原始 K 线中发现这些模式。状态一多，表格型方法（如 Q-Learning 用一张 Q 表记录每个"状态-动作"的价值）就存不下、学不动。这正是 [[Deep Reinforcement Learning（深度强化学习）]] 要解决的问题。
- **试错成本高**：真实交易里试错是真金白银，所以通常先在历史数据构成的模拟环境中训练和回测。
- **奖励设计不好会学歪**：例如只奖励收益、不惩罚风险，Agent 可能学会高风险的赌博式操作。
- 训练往往不稳定、需要大量交互样本。

## 关联

- [[Machine Learning（机器学习）]]：上位概念，强化学习是三大范式之一。
- [[Supervised Learning（监督学习）]]：对照——监督学习给标准答案，强化学习只给奖惩且可能延迟。
- [[Deep Reinforcement Learning（深度强化学习）]]：加上深度网络后，不再依赖人工设计状态特征。
- [[深度学习和强化学习有什么区别]]：强化学习是学习范式，不是深度学习的分支。
