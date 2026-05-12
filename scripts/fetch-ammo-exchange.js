const axios = require('axios');
const fs = require('fs');
const path = require('path');

const API_BASE = 'https://orzrice.com/workApi/v1/sjz_api';
const TOKEN = process.env.API_TOKEN;

if (!TOKEN) {
  console.error('❌ 错误：未设置 API_TOKEN 环境变量');
  process.exit(1);
}

// 获取子弹兑换最优方案
async function fetchAmmoExchange() {
  console.log('📡 正在获取子弹兑换数据...');
  
  try {
    const response = await axios.get(`${API_BASE}/ammo_exchange`, {
      params: { token: TOKEN },
      timeout: 10000
    });

    if (response.data.code === 200) {
      const ammoData = response.data.data;
      console.log(`  ✓ 成功获取 ${ammoData.length} 种子弹的兑换数据`);
      
      // 按兑换率排序，找出最优方案
      const optimized = ammoData.map(ammo => {
        const bestExchange = ammo.exchange_rates.find(e => e.is_best) || ammo.exchange_rates[0];
        return {
          ammo_id: ammo.ammo_id,
          ammo_name: ammo.ammo_name,
          penetration: ammo.penetration,
          damage: ammo.damage,
          best_department: bestExchange?.department || '未知',
          best_rate: bestExchange?.rate || 0,
          daily_free: ammo.daily_free,
          free_department: ammo.free_department,
          all_exchanges: ammo.exchange_rates
        };
      });

      // 按最优兑换率降序排列
      optimized.sort((a, b) => b.best_rate - a.best_rate);

      return optimized;
    } else {
      console.error(`❌ API返回错误：${response.data.msg}`);
      return [];
    }
  } catch (error) {
    console.error('❌ 获取子弹兑换数据失败：', error.message);
    // 返回空数组，避免中断流程
    return [];
  }
}

// 主函数
async function main() {
  console.log('🚀 开始抓取子弹兑换数据...');
  console.log(`⏰ 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`);

  try {
    const ammoExchange = await fetchAmmoExchange();
    
    console.log(`✅ 成功处理 ${ammoExchange.length} 种子弹数据`);

    // 生成数据统计
    const stats = {
      total_ammo_types: ammoExchange.length,
      top_exchanges: ammoExchange.slice(0, 5).map(a => ({
        name: a.ammo_name,
        department: a.best_department,
        rate: a.best_rate
      }))
    };
    console.log('📊 Top 5 最优兑换：', stats.top_exchanges);

    // 读取现有数据
    const ammoFile = path.join(__dirname, '..', 'ammo-exchange.json');
    let existingData = {};
    if (fs.existsSync(ammoFile)) {
      existingData = JSON.parse(fs.readFileSync(ammoFile, 'utf8'));
    }

    // 更新数据
    const updatedData = {
      ...existingData,
      ammo_exchange: ammoExchange,
      last_update: new Date().toISOString(),
      update_timestamp: Date.now(),
      data_source: '三角洲数据帝API',
      stats: stats
    };

    // 写入文件
    fs.writeFileSync(ammoFile, JSON.stringify(updatedData, null, 2), 'utf8');
    console.log(`💾 数据已保存到 ${ammoFile}`);
    console.log('✅ 子弹兑换数据更新完成！');

  } catch (error) {
    console.error('❌ 抓取子弹兑换数据失败：', error.message);
    process.exit(1);
  }
}

main();
