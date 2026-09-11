---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/计算机基础, 领域/数据与存储, 层级/基础]
aliases: [IANA Time Zone Database, IANA 时区数据库, tzdata, tz database, Olson Database, Asia/Shanghai]
created: 2026-09-06
updated: 2026-09-06
---

# IANA Time Zone Database（IANA 时区数据库）

## 一句话

`IANA Time Zone Database（IANA 时区数据库）` 是全球时区规则的权威数据库，用 `区域/城市` 命名，存的不是一个偏移量，而是一套随时间变化的规则。

## 背景：它出现前的问题

时区不是地理常量，是政治决定：夏令时的起止日期会改，国家会整体改时区，也会宣布永久取消夏令时。

如果每个程序自己维护一张「国家 → 偏移量」的表，规则一变就得全网改代码，而且历史数据会被算错。

## 它解决了什么

它把「规则」这件事集中维护成一份公共数据，程序只需要存一个名字：

```text
Asia/Shanghai
Europe/Budapest
America/New_York
```

名字背后是一整套带生效时间的规则，所以同一个名字在不同日期会算出不同的 [[UTC Offset（UTC 偏移量）]]：

```text
Europe/Budapest  2026-01-15 → GMT+01:00
Europe/Budapest  2026-07-15 → GMT+02:00
Asia/Shanghai    两个日期均 → GMT+08:00
```

## 核心机制

在 JavaScript 里通过 `Intl` 访问，语言内置，不需要安装任何依赖：

```js
new Intl.DateTimeFormat('zh-CN', {
  timeZone: 'Europe/Budapest',
  timeZoneName: 'longOffset',
}).format(new Date('2026-07-15T12:00:00Z'))
```

用法上，它是 [[Instant（瞬间）]] 和 [[Wall Clock Time（墙上时间）]] 之间的换算器：给它一个瞬间和一个地点名，它给出那一刻在那儿的钟面数字，以及当时生效的偏移量。

## 典型使用场景

- 存储用户所在时区、事件发生地。
- 服务端按用户时区渲染日期、做「本地哪一天」的分组统计。
- 处理跨夏令时边界的重复日程。

## 局限性

- 数据库本身需要随系统或运行时更新，长期不更新的环境会算错未来的日期。
- 它只提供规则，不提供事实：**没人告诉它当时人在哪儿**。地点这个信息必须由业务系统自己记录或补齐。
- 历史规则变更几乎都面向未来，所以已发生事件的偏移量基本稳定；问题通常出在当初有没有把地点记下来。

## 和其他概念的关系

- [[UTC Offset（UTC 偏移量）]]：是这套规则的计算输出，不能反过来代替规则。
- [[ZonedDateTime（带时区时间）]]：地点那一半就是 IANA 名字。
- [[Instant（瞬间）]] 与 [[Wall Clock Time（墙上时间）]]：靠它互相换算。

## 关联

- [[UTC Offset（UTC 偏移量）]]
- [[ZonedDateTime（带时区时间）]]
- [[Instant（瞬间）]]
- [[Wall Clock Time（墙上时间）]]
- [[为什么存时间要存时区名而不是 UTC 偏移量]]
