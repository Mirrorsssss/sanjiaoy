# 三角眼战备工具站 - 记忆文件

## 项目信息
- 项目路径: C:\Users\11342\WorkBuddy\2026-05-08-task-1
- 网站: 三角洲行动战备工具站
- GitHub: 需配置Token才能推送

## 已完成工作

### 1. 数据调研与更新（2026-05-08）
- 找到数据来源网站：
  - sjz.jbskins.com - 武器、防具、配件价格数据
  - dfhub.cn - 工坊利润数据
  - deltaforcetools.gg - 武器基础数据
  - dfttk.com - TTK数据
- 创建了独立数据文件: data/game-data.json
- 更新了 index.html 中的所有价格数据为真实数据

### 2. 数据更新机制
- 创建了数据更新脚本: scripts/update-data.js
- 创建了更新指南: DATA_UPDATE_GUIDE.md
- 创建了 package.json 管理依赖

### 3. 已更新数据
- tickerData: 30+条真实武器/配件价格
- wsData: 30+种工坊制造物品
- buildData: 所有战备配置的真实价格
- 添加了数据来源和更新时间显示

## 待完成
- 继续补充子弹数据、工坊制造详细配方
- 完善武器属性数据（伤害、穿透等）
- 添加数据自动更新GitHub Actions

## 文件结构
```
├── index.html          # 主网站
├── data/
│   └── game-data.json  # 真实游戏数据
├── scripts/
│   └── update-data.js  # 数据更新脚本
├── DATA_UPDATE_GUIDE.md # 数据更新指南
└── package.json        # npm依赖
```

## 备注
- 大部分游戏数据通过网页抓取获取，但有些网站有动态加载或反爬机制
- 建议手动定期更新数据以确保准确性
