# 三角眼工具站 API 对接实施指南

**实施日期**：2026年5月12日  
**当前阶段**：第二阶段（已完成）  
**状态**：✅ 代码已完成，等待配置

---

## 📋 实施内容总览

### ✅ 第一阶段（已完成）
| 任务 | 状态 | 文件 |
|------|------|------|
| 修正技术规范文档 | ✅ | `docs/api-integration-spec-v1.md` |
| 实时物价API | ✅ | `scripts/fetch-prices.js` |
| 工坊制造利润API | ✅ | `scripts/fetch-workshop.js` |

### ✅ 第二阶段（已完成）
| 任务 | 状态 | 文件 |
|------|------|------|
| 子弹兑换API | ✅ | `scripts/fetch-ammo-exchange.js` |
| 智能配装API | ✅ | `scripts/fetch-loadouts.js` |
| 历史价格API | ✅ | `scripts/fetch-price-history.js` |
| 数据校验机制 | ✅ | GitHub Actions集成 |

---

## 🚀 更新频率规划

| 数据类型 | 更新频率 | 说明 |
|----------|----------|------|
| 实时物价 | 每10分钟 | 交易行价格变动较频繁 |
| 工坊制造利润 | 每10分钟 | 材料价格影响利润计算 |
| 子弹兑换 | 每小时 | 游戏版本更新时同步 |
| 智能配装 | 每小时 | 基于最新物价计算最优方案 |
| 历史价格 | 每日凌晨3点 | 避开高峰期，减少服务器压力 |
| 数据校验 | 每日中午12点 | 确保数据完整性 |

---

## 📁 生成的数据文件

| 文件名 | 说明 | 更新频率 |
|--------|------|----------|
| `price-realtime.json` | 实时物价数据 | 每10分钟 |
| `workshop.json` | 工坊制造利润数据 | 每10分钟 |
| `ammo-exchange.json` | 子弹兑换最优方案 | 每小时 |
| `smart-loadout-api.json` | 智能配装方案库 | 每小时 |
| `price-history.json` | 历史价格趋势 | 每日 |

---

## 🔧 GitHub Actions 工作流

### 工作流结构

```
.github/workflows/update-data.yml
├── update-prices (每10分钟)
│   ├── fetch-prices.js
│   └── fetch-workshop.js
├── update-extended-data (每小时)
│   ├── fetch-ammo-exchange.js
│   └── fetch-loadouts.js
├── update-price-history (每日凌晨3点)
│   └── fetch-price-history.js
└── data-validation (每日中午12点)
    └── 数据完整性校验
```

### 手动触发测试

1. 进入仓库 **Actions** 标签页
2. 选择 **Update Game Data**
3. 点击 **Run workflow** → **Run workflow**
4. 选择要运行的job（可选）

---

## ⚠️ 重要：API Token配置

### 如果还未配置Token

1. 访问 **https://orzrice.com** → 开放平台
2. 申请API Token（免费，需标注数据来源）
3. 进入GitHub仓库 **Settings** → **Secrets and variables** → **Actions**
4. 添加Secret：Name: `ORZRICE_TOKEN`，Value: 你的Token值

### 如果Token已配置

第二阶段会自动运行，无需额外配置。

---

## 📈 后续规划

### 第三阶段（待实施）
- [ ] WebSocket实时价格推送
- [ ] 价格提醒功能开发
- [ ] 个人战绩查询功能

---

## 🆘 故障排查

### 问题：工作流运行失败
1. 检查GitHub Secret配置是否正确
2. 手动触发一次测试，观察详细错误日志
3. 等待几分钟后重试

### 问题：数据文件未更新
1. 确认API返回了新的数据
2. 检查仓库Settings → Actions → Workflow permissions
3. 确保"Read and write permissions"已启用

---

**文档版本**：V2.0  
**最后更新**：2026年5月12日
