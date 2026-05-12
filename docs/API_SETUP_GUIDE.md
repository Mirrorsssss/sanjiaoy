# 三角眼工具站 API 对接实施指南

**实施日期**：2026年5月12日  
**实施阶段**：第一阶段（紧急修复）  
**状态**：✅ 代码已完成，等待配置

---

## 📋 实施内容

### 已完成的工作

1. ✅ **修正技术规范文档** (`docs/api-integration-spec-v1.md`)
   - 修正域名拼写错误（orzice.com → orzrice.com）
   - 添加分页参数（page、page_size）
   - 明确时间单位（craft_time_unit: "seconds"）
   - 添加Token申请地址说明

2. ✅ **创建GitHub Actions自动化工作流** (`.github/workflows/update-data.yml`)
   - 每10分钟自动抓取API数据
   - 支持手动触发
   - 自动提交并更新JSON数据文件

3. ✅ **创建API数据抓取脚本**
   - `scripts/fetch-prices.js` - 抓取实时物价数据
   - `scripts/fetch-workshop.js` - 抓取工坊制造利润数据

---

## 🚀 下一步配置步骤

### Step 1: 申请API Token

1. 访问三角洲数据帝平台：**https://orzrice.com**
2. 找到API Token申请入口（通常在"开放平台"或"API接口"页面）
3. 填写申请信息（网站名称：三角眼工具站，网站地址：https://df.sanjiaoy.top）
4. 获取Token后，记录保存（形如：`abc123def456...`）

### Step 2: 配置GitHub Secret

1. 登录GitHub，进入仓库：**Mirrorsssss/sanjiaoy**
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 填写：
   - Name: `ORZRICE_TOKEN`
   - Value: `你的Token值`（例如：`abc123def456...`）
5. 点击 **Add secret**

### Step 3: 启用GitHub Actions

1. 进入仓库 **Actions** 标签页
2. 找到 **Update Game Data** 工作流
3. 如果工作流被禁用，点击 **Enable workflow**
4. 点击 **Run workflow** → **Run workflow**（手动触发一次测试）

### Step 4: 验证实施结果

1. 查看 **Actions** 标签页，确认工作流运行成功（绿色✅）
2. 检查仓库文件，确认以下文件已更新：
   - `price-realtime.json` - 应该包含实时物价数据
   - `workshop.json` - 应该包含制造利润数据
3. 访问网站 https://df.sanjiaoy.top，确认数据已更新

---

## 📊 数据结构说明

### price-realtime.json 格式

```json
{
  "prices": {
    "1001": {
      "name": "钛合金板",
      "type": "material",
      "price": 2280,
      "price_min": 2200,
      "price_max": 2350,
      "trend": "up",
      "update_time": "2026-05-12 18:30:00",
      "is_bindable": false
    }
  },
  "last_update": "2026-05-12T12:30:00.000Z",
  "update_timestamp": 1715526600000
}
```

### workshop.json 格式

```json
{
  "recipes": {
    "2001_level2": {
      "item_id": "2001",
      "item_name": "XCOG突击3.5倍镜",
      "workbench_level": 2,
      "material_cost": 15600,
      "sell_price": 28900,
      "profit": 9543,
      "profit_per_hour": 19086,
      "craft_time": 1800,
      "craft_time_unit": "seconds",
      "materials": [
        {"item_id": "1001", "item_name": "钛合金板", "count": 3, "cost": 6840}
      ],
      "last_update": "2026-05-12T12:30:00.000Z"
    }
  },
  "last_update": "2026-05-12T12:30:00.000Z",
  "update_timestamp": 1715526600000,
  "data_source": "三角洲数据帝API",
  "api_version": "v1"
}
```

---

## 🔧 故障排查

### GitHub Actions 运行失败

**问题**：工作流运行失败，显示红色❌

**解决方案**：
1. 点击失败的工作流运行，查看日志
2. 常见错误：
   - `API_TOKEN 未设置` → 检查GitHub Secret是否正确配置
   - `请求超时` → API服务可能暂时不可用，等待下次自动重试
   - `HTTP 401` → Token无效或过期，重新申请Token

### 数据未更新

**问题**：工作流运行成功，但JSON文件未更新

**解决方案**：
1. 检查工作流日志，确认脚本是否成功执行
2. 确认脚本是否有写入权限（检查repository settings）
3. 手动触发一次工作流（Actions → Update Game Data → Run workflow）

---

## 📈 后续优化建议

### 短期（已完成）
- [x] 对接实时物价API
- [x] 对接制造利润API
- [x] 建立自动更新机制

### 中期（待实施）
- [ ] 对接子弹兑换API
- [ ] 对接智能配装API
- [ ] 对接历史价格API
- [ ] 添加数据校验和异常处理

### 长期（待规划）
- [ ] 对接WebSocket实时推送
- [ ] 开发价格提醒功能
- [ ] 开发个人战绩查询

---

## 📞 技术支持

如遇到技术问题，请联系：
- 技术支持：workbuddyAI团队
- API提供方：三角洲数据帝 (orzrice.com)

---

**文档版本**：V1.0  
**最后更新**：2026年5月12日
