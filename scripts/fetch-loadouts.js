const axios = require('axios');
const fs = require('fs');
const path = require('path');

const API_BASE = 'https://orzrice.com/workApi/v1/sjz_api';
const TOKEN = process.env.API_TOKEN;

if (!TOKEN) {
  console.error('❌ 错误：未设置 API_TOKEN 环境变量');
  process.exit(1);
}

// 预定义的配装查询参数组合
const LOADOUT_CONFIGS = [
  // 烽火地带 - 单排
  { mode: 'fenghuo', budget: 30000, play_style: 'paodao', team_size: 1, label: '烽火-跑刀-单排-3万' },
  { mode: 'fenghuo', budget: 50000, play_style: 'tuji', team_size: 1, label: '烽火-突击-单排-5万' },
  { mode: 'fenghuo', budget: 100000, play_style: 'tuji', team_size: 1, label: '烽火-突击-单排-10万' },
  { mode: 'fenghuo', budget: 200000, play_style: 'juji', team_size: 1, label: '烽火-狙击-单排-20万' },
  
  // 烽火地带 - 双排
  { mode: 'fenghuo', budget: 50000, play_style: 'tuji', team_size: 2, label: '烽火-突击-双排-5万' },
  { mode: 'fenghuo', budget: 100000, play_style: 'tuji', team_size: 2, label: '烽火-突击-双排-10万' },
  
  // 烽火地带 - 四排
  { mode: 'fenghuo', budget: 100000, play_style: 'tuji', team_size: 4, label: '烽火-突击-四排-10万' },
  { mode: 'fenghuo', budget: 200000, play_style: 'tuji', team_size: 4, label: '烽火-突击-四排-20万' },
  
  // 全面战场
  { mode: 'quanmian', budget: 50000, play_style: 'tuji', team_size: 1, label: '全面-突击-单排-5万' },
  { mode: 'quanmian', budget: 100000, play_style: 'tuji', team_size: 4, label: '全面-突击-四排-10万' }
];

// 获取单个配装方案
async function fetchLoadout(config) {
  try {
    const response = await axios.post(`${API_BASE}/jzv3_zb_plus_all`, {
      token: TOKEN,
      mode: config.mode,
      budget: config.budget,
      play_style: config.play_style,
      team_size: config.team_size
    }, {
      timeout: 15000,
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.data.code === 200) {
      return {
        ...config,
        success: true,
        data: response.data.data,
        fetched_at: new Date().toISOString()
      };
    } else {
      return {
        ...config,
        success: false,
        error: response.data.msg,
        fetched_at: new Date().toISOString()
      };
    }
  } catch (error) {
    return {
      ...config,
      success: false,
      error: error.message,
      fetched_at: new Date().toISOString()
    };
  }
}

// 主函数
async function main() {
  console.log('🚀 开始抓取智能配装数据...');
  console.log(`⏰ 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`);

  const allLoadouts = {};
  let successCount = 0;
  let failCount = 0;

  for (const config of LOADOUT_CONFIGS) {
    console.log(`📡 获取配装：${config.label}...`);
    
    const result = await fetchLoadout(config);
    
    if (result.success) {
      const key = `${config.mode}_${config.play_style}_${config.team_size}_${config.budget}`;
      allLoadouts[key] = result;
      successCount++;
      console.log(`  ✓ 成功`);
    } else {
      const key = `${config.mode}_${config.play_style}_${config.team_size}_${config.budget}`;
      allLoadouts[key] = result;
      failCount++;
      console.log(`  ❌ 失败：${result.error}`);
    }

    // 避免请求过快，添加延迟
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  console.log(`\n📊 获取结果：成功 ${successCount} 个，失败 ${failCount} 个`);

  // 读取现有数据
  const loadoutFile = path.join(__dirname, '..', 'smart-loadout-api.json');
  let existingData = {};
  if (fs.existsSync(loadoutFile)) {
    existingData = JSON.parse(fs.readFileSync(loadoutFile, 'utf8'));
  }

  // 更新数据
  const updatedData = {
    ...existingData,
    loadouts: allLoadouts,
    last_update: new Date().toISOString(),
    update_timestamp: Date.now(),
    data_source: '三角洲数据帝API',
    config_count: LOADOUT_CONFIGS.length,
    success_count: successCount,
    fail_count: failCount
  };

  // 写入文件
  fs.writeFileSync(loadoutFile, JSON.stringify(updatedData, null, 2), 'utf8');
  console.log(`💾 数据已保存到 ${loadoutFile}`);
  console.log('✅ 智能配装数据更新完成！');
}

main();
