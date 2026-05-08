# 三角眼数据更新指南

## 概述

三角眼战备工具站的数据来自多个游戏数据网站。为了确保数据准确性和实时性，需要定期更新数据。

## 数据来源

| 数据类型 | 来源网站 | URL | 更新频率 |
|---------|---------|-----|---------|
| 武器价格 | 三角洲零号站 | https://sjz.jbskins.com | 每日 |
| 配件价格 | 三角洲零号站 | https://sjz.jbskins.com | 每日 |
| 防具价格 | 三角洲零号站 | https://sjz.jbskins.com | 每日 |
| 武器数据 | DeltaForce Tools | https://deltaforcetools.gg | 每周 |
| TTK数据 | DFTK | https://dfttk.com | 每周 |
| 工坊利润 | 三角洲数据站 | https://www.dfhub.cn | 每日 |

## 数据文件结构

```
data/
├── game-data.json      # 主数据文件
├── weapons/            # 武器数据
│   ├── prices.json     # 价格数据
│   ├── stats.json      # 属性数据
│   └── attachments.json # 配件兼容
├── attachments/        # 配件数据
├── armor/             # 防具数据
├── bullets/           # 子弹数据
├── workshop/          # 工坊数据
└── meta/
    └── update-log.json # 更新日志
```

## 更新流程

### 方式一：手动更新（推荐用于小规模更新）

1. 访问数据来源网站
2. 复制最新的数据
3. 更新 `data/game-data.json` 文件
4. 提交更改到 GitHub

### 方式二：半自动更新（推荐）

使用提供的更新脚本抓取最新数据：

```bash
# 安装依赖
npm install

# 运行更新脚本
npm run update-data
```

### 方式三：自动化更新（GitHub Actions）

数据已配置 GitHub Actions 定时任务：
- **每日 08:00** - 更新价格数据
- **每周一 08:00** - 更新武器属性数据

## 手动更新数据步骤

### 1. 更新武器价格

访问 https://sjz.jbskins.com/Item/index/category_id/4

获取所有页面的武器数据，格式如下：

```json
{
  "weapons": {
    "pistol": {
      "name": "手枪",
      "items": [
        { "id": "g17", "name": "G17", "price": 4799, "level": 0, "grid": "2×1" }
      ]
    }
  }
}
```

### 2. 更新配件价格

访问 https://sjz.jbskins.com/Item/index/category_id/2

获取所有页面的配件数据。

### 3. 更新工坊利润

访问 https://www.dfhub.cn/workshop/

获取工坊制造的配方、成本和利润数据。

### 4. 验证数据

确保数据格式正确后，更新 `_lastUpdate` 字段为当前日期。

## 数据格式规范

### 武器数据

```json
{
  "id": "唯一ID",
  "name": "显示名称",
  "price": 价格(数字),
  "level": 等级(0-3),
  "grid": "网格尺寸如2×1",
  "param": 参数值(可选)
}
```

### 价格显示

所有价格使用整数，单位为游戏内货币。
显示时使用格式化函数转为 `X万` 或 `XXX万` 格式。

### 数据验证

更新后请验证：
1. JSON 格式正确
2. 价格是数字类型
3. 所有必填字段存在
4. 无重复的 ID

## 常见问题

### Q: 网站数据加载失败怎么办？

A: 可能原因：
1. 网站暂时不可用 - 等待后重试
2. 网站改版导致数据格式变化 - 需要更新抓取脚本
3. 网络问题 - 检查网络连接

### Q: 如何知道数据是过期的？

A: 查看 `meta.lastUpdate` 字段，值应该是当天或昨天的日期。

### Q: 发现数据明显错误怎么办？

A: 
1. 首先在 GitHub Issues 报告
2. 等待维护者确认
3. 维护者更新数据

## 贡献数据

欢迎玩家社区贡献数据！请：

1. Fork 项目
2. 更新数据文件
3. 提交 Pull Request
4. 等待审核合并

## 联系方式

如有问题，请通过以下方式联系：
- GitHub Issues: https://github.com/你的用户名/delta-tool/issues
- 游戏内: 在三角眼社区发帖

---

**最后更新**: 2026-05-08
**维护者**: 三角眼工具站团队
