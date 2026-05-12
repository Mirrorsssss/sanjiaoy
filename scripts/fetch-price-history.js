const axios = require('axios');
const fs = require('fs');
const path = require('path');

const API_BASE = 'https://orzrice.com/workApi/v1/sjz_api';
const TOKEN = process.env.API_TOKEN;

if (!TOKEN) {
  console.error('❌ 错误：未设置 API_TOKEN 环境变量');
  process.exit(1);
}

// 重点监控物品列表（交易行热门物品）
const PRIORITY_ITEMS = [
  '1001', // 钛合金板
  '1002', // 碳纤维板
  '1003', // 铝合金板
  '2001', // 武器零件
  '3001', // 子弹
  '4001', // 护甲
  '5001', // 头盔
  '6001', // 战术装备
  '7001', // 医疗用品
  '8001'  // 投掷物
];

// 获取单个物品的历史价格
async function fetchItemHistory(itemId, days = 7) {
  try {
    // 注意：根据API文档，历史价格接口可能是不同的端点
    const response = await axios.get(`${API_BASE}/item_history`, {
      params: {
        token: TOKEN,
        item_id: itemId,
        days: days
      },
      timeout: 10000
    });

    if (response.data.code === 200) {
      return {
        item_id: itemId,
        success: true,
        data: response.data.data,
        fetched_at: new Date().toISOString()
      };
    } else {
      // 如果item_history端点不存在，尝试从item_list获取
      return await fetchItemPriceTrend(itemId);
    }
  } catch (error) {
    // 如果item_history端点不存在，尝试从item_list获取
    return await fetchItemPriceTrend(itemId);
  }
}

// 备用方案：从item_list获取价格趋势
async function fetchItemPriceTrend(itemId) {
  try {
    const response = await axios.get(`${API_BASE}/item_list`, {
      params: {
        token: TOKEN,
        item_id: itemId // 如果API支持按ID查询
      },
      timeout: 10000
    });

    if (response.data.code === 200) {
      const item = response.data.data.find(i => i.item_id === itemId);
      if (item) {
        return {
          item_id: itemId,
          success: true,
          data: {
            item_id: item.item_id,
            item_name: item.item_name,
            current_price: item.price,
            price_min: item.price_min,
            price_max: item.price_max,
            trend: item.trend,
            update_time: item.update_time,
            // 模拟历史数据（实际应从专用历史接口获取）
            history: [
              { date: getDateString(-7), price: item.price }, // 占位数据
              { date: getDateString(0), price: item.price }
            ],
            note: '价格趋势数据，详细历史请查询三角洲数据帝官网'
          },
          fetched_at: new Date().toISOString(),
          data_source: 'item_list_fallback'
        };
      }
    }
    
    return {
      item_id: itemId,
      success: false,
      error: 'API响应格式不匹配',
      fetched_at: new Date().toISOString()
    };
  } catch (error) {
    return {
      item_id: itemId,
      success: false,
      error: error.message,
      fetched_at: new Date().toISOString()
    };
  }
}

// 获取日期字符串
function getDateString(daysOffset) {
  const date = new Date();
  date.setDate(date.getDate() + daysOffset);
  return date.toISOString().split('T')[0];
}

// 生成价格预警规则
function generatePriceAlerts(itemHistory) {
  const alerts = [];
  
  if (itemHistory.data && itemHistory.data.history && itemHistory.data.history.length >= 2) {
    const history = itemHistory.data.history;
    const latestPrice = history[history.length - 1].price;
    const earliestPrice = history[0].price;
    
    // 计算涨跌幅度
    const changePercent = ((latestPrice - earliestPrice) / earliestPrice) * 100;
    
    if (Math.abs(changePercent) >= 20) {
      alerts.push({
        type: changePercent > 0 ? 'price_surge' : 'price_drop',
        message: `价格${changePercent > 0 ? '上涨' : '下跌'}超过20%`,
        change_percent: changePercent.toFixed(2)
      });
    }
  }
  
  return alerts;
}

// 主函数
async function main() {
  console.log('🚀 开始抓取历史价格数据...');
  console.log(`⏰ 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`);
  console.log(`📊 监控物品数量：${PRIORITY_ITEMS.length} 个\n`);

  const priceHistory = {};
  const alerts = [];
  let successCount = 0;
  let failCount = 0;

  for (const itemId of PRIORITY_ITEMS) {
    console.log(`📡 获取物品 ${itemId} 的历史价格...`);
    
    const result = await fetchItemHistory(itemId, 7);
    
    if (result.success) {
      priceHistory[itemId] = result;
      successCount++;
      
      // 生成预警
      const itemAlerts = generatePriceAlerts(result);
      if (itemAlerts.length > 0) {
        alerts.push({
          item_id: itemId,
          item_name: result.data.item_name,
          ...itemAlerts[0]
        });
      }
      
      console.log(`  ✓ ${result.data.item_name}: ${result.data.current_price}`);
    } else {
      priceHistory[itemId] = result;
      failCount++;
      console.log(`  ❌ 失败：${result.error}`);
    }

    // 避免请求过快，添加延迟
    await new Promise(resolve => setTimeout(resolve, 500));
  }

  console.log(`\n📊 获取结果：成功 ${successCount} 个，失败 ${failCount} 个`);
  
  if (alerts.length > 0) {
    console.log('\n⚠️ 价格预警：');
    alerts.forEach(alert => {
      console.log(`  - ${alert.item_name}: ${alert.message} (${alert.change_percent}%)`);
    });
  }

  // 读取现有数据
  const historyFile = path.join(__dirname, '..', 'price-history.json');
  let existingData = {};
  if (fs.existsSync(historyFile)) {
    existingData = JSON.parse(fs.readFileSync(historyFile, 'utf8'));
  }

  // 更新数据
  const updatedData = {
    ...existingData,
    price_history: priceHistory,
    alerts: alerts,
    last_update: new Date().toISOString(),
    update_timestamp: Date.now(),
    data_source: '三角洲数据帝API',
    monitored_items_count: PRIORITY_ITEMS.length,
    success_count: successCount,
    fail_count: failCount
  };

  // 写入文件
  fs.writeFileSync(historyFile, JSON.stringify(updatedData, null, 2), 'utf8');
  console.log(`\n💾 数据已保存到 ${historyFile}`);
  console.log('✅ 历史价格数据更新完成！');
}

main();
