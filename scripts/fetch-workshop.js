const axios = require('axios');
const fs = require('fs');
const path = require('path');

const API_BASE = 'https://orzrice.com/workApi/v1/sjz_api';
const TOKEN = process.env.API_TOKEN;

if (!TOKEN) {
  console.error('❌ 错误：未设置 API_TOKEN 环境变量');
  process.exit(1);
}

// 获取制造利润数据
async function fetchWorkshopData() {
  console.log('📡 正在获取制造利润数据...');
  
  const workbenchLevels = [1, 2]; // 1=普通，2=高级
  const allRecipes = {};

  for (const level of workbenchLevels) {
    try {
      console.log(`  🔧 获取工作台等级 ${level} 的制造数据...`);
      
      const response = await axios.get(`${API_BASE}/manufacturePro`, {
        params: {
          token: TOKEN,
          workbench_level: level,
          include_bind: false
        },
        timeout: 15000
      });

      if (response.data.code === 200) {
        const recipes = response.data.data;
        
        recipes.forEach(recipe => {
          const key = `${recipe.item_id}_level${level}`;
          allRecipes[key] = {
            item_id: recipe.item_id,
            item_name: recipe.item_name,
            workbench_level: level,
            material_cost: recipe.material_cost,
            sell_price: recipe.sell_price,
            profit: recipe.profit,
            profit_per_hour: recipe.profit_per_hour,
            craft_time: recipe.craft_time,
            craft_time_unit: recipe.craft_time_unit || 'seconds',
            materials: recipe.materials,
            last_update: new Date().toISOString()
          };
        });

        console.log(`  ✓ 成功获取 ${recipes.length} 个制造配方`);
      } else {
        console.error(`❌ API返回错误：${response.data.msg}`);
      }
    } catch (error) {
      console.error(`❌ 获取制造利润数据失败（等级 ${level}）：`, error.message);
      
      // 重试一次
      await new Promise(resolve => setTimeout(resolve, 5000));
      try {
        const retryResponse = await axios.get(`${API_BASE}/manufacturePro`, {
          params: {
            token: TOKEN,
            workbench_level: level,
            include_bind: false
          },
          timeout: 15000
        });
        // 处理重试逻辑...
      } catch (retryError) {
        console.error(`❌ 重试失败，跳过等级 ${level}`);
      }
    }
  }

  return allRecipes;
}

// 主函数
async function main() {
  console.log('🚀 开始抓取工坊制造利润数据...');
  console.log(`⏰ 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`);

  try {
    const recipes = await fetchWorkshopData();
    const recipeCount = Object.keys(recipes).length;
    
    console.log(`✅ 成功获取 ${recipeCount} 个制造配方`);

    // 读取现有数据
    const workshopFile = path.join(__dirname, '..', 'workshop.json');
    let existingData = {};
    if (fs.existsSync(workshopFile)) {
      existingData = JSON.parse(fs.readFileSync(workshopFile, 'utf8'));
    }

    // 更新数据
    const updatedData = {
      ...existingData,
      recipes: recipes,
      last_update: new Date().toISOString(),
      update_timestamp: Date.now(),
      data_source: '三角洲数据帝API',
      api_version: 'v1'
    };

    // 写入文件
    fs.writeFileSync(workshopFile, JSON.stringify(updatedData, null, 2), 'utf8');
    console.log(`💾 数据已保存到 ${workshopFile}`);

    // 生成统计信息
    const stats = {
      total_recipes: recipeCount,
      by_level: {
        level1: Object.keys(recipes).filter(k => k.endsWith('_level1')).length,
        level2: Object.keys(recipes).filter(k => k.endsWith('_level2')).length
      },
      avg_profit: Object.values(recipes).reduce((sum, r) => sum + r.profit, 0) / recipeCount,
      max_profit: Math.max(...Object.values(recipes).map(r => r.profit)),
      min_profit: Math.min(...Object.values(recipes).map(r => r.profit))
    };

    console.log('📊 统计信息：', stats);
    console.log('✅ 工坊数据更新完成！');

  } catch (error) {
    console.error('❌ 抓取工坊数据失败：', error.message);
    process.exit(1);
  }
}

main();
