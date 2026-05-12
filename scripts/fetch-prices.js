const axios = require('axios');
const fs = require('fs');
const path = require('path');

const API_BASE = 'https://orzrice.com/workApi/v1/sjz_api';
const TOKEN = process.env.API_TOKEN;

if (!TOKEN) {
  console.error('❌ 错误：未设置 API_TOKEN 环境变量');
  process.exit(1);
}

// 获取所有物品类型的价格
async function fetchAllPrices() {
  const types = ['all', 'weapon', 'armor', 'ammo', 'material'];
  const allItems = {};

  for (const type of types) {
    console.log(`📡 正在获取 ${type} 类型物品价格...`);
    
    let page = 1;
    let totalPages = 1;
    
    do {
      try {
        const response = await axios.get(`${API_BASE}/item_list`, {
          params: {
            token: TOKEN,
            type: type,
            page: page,
            page_size: 100
          },
          timeout: 10000
        });

        if (response.data.code === 200) {
          const items = response.data.data;
          const total = response.data.total;
          totalPages = Math.ceil(total / 100);

          items.forEach(item => {
            allItems[item.item_id] = {
              name: item.item_name,
              type: item.item_type,
              price: item.price,
              price_min: item.price_min,
              price_max: item.price_max,
              trend: item.trend,
              update_time: item.update_time,
              is_bindable: item.is_bindable
            };
          });

          console.log(`  ✓ 第 ${page}/${totalPages} 页，获取 ${items.length} 个物品`);
          page++;
        } else {
          console.error(`❌ API返回错误：${response.data.msg}`);
          break;
        }
      } catch (error) {
        console.error(`❌ 获取 ${type} 价格失败（第 ${page} 页）：`, error.message);
        // 重试一次
        await new Promise(resolve => setTimeout(resolve, 5000));
        try {
          const retryResponse = await axios.get(`${API_BASE}/item_list`, {
            params: {
              token: TOKEN,
              type: type,
              page: page,
              page_size: 100
            },
            timeout: 10000
          });
          // 处理重试逻辑...
        } catch (retryError) {
          console.error(`❌ 重试失败，跳过第 ${page} 页`);
          page++;
        }
      }
    } while (page <= totalPages);
  }

  return allItems;
}

// 主函数
async function main() {
  console.log('🚀 开始抓取实时物价数据...');
  console.log(`⏰ 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`);

  try {
    const prices = await fetchAllPrices();
    const itemCount = Object.keys(prices).length;
    
    console.log(`✅ 成功获取 ${itemCount} 个物品的价格数据`);

    // 读取现有数据
    const priceFile = path.join(__dirname, '..', 'price-realtime.json');
    let existingData = {};
    if (fs.existsSync(priceFile)) {
      existingData = JSON.parse(fs.readFileSync(priceFile, 'utf8'));
    }

    // 更新数据
    const updatedData = {
      ...existingData,
      prices: prices,
      last_update: new Date().toISOString(),
      update_timestamp: Date.now()
    };

    // 写入文件
    fs.writeFileSync(priceFile, JSON.stringify(updatedData, null, 2), 'utf8');
    console.log(`💾 数据已保存到 ${priceFile}`);

    // 生成更新日志
    const logEntry = {
      timestamp: new Date().toISOString(),
      item_count: itemCount,
      status: 'success'
    };
    
    console.log('📝 更新日志：', logEntry);
    console.log('✅ 物价数据更新完成！');

  } catch (error) {
    console.error('❌ 抓取物价数据失败：', error.message);
    process.exit(1);
  }
}

main();
