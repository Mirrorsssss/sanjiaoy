const axios = require('axios');
const fs = require('fs');
const path = require('path');

/**
 * 从 GitHub 免费数据源获取三角洲行动数据
 * 数据源: https://github.com/jiansenc/DeltaForceData
 * 使用 jsdelivr CDN 加速访问 (国内更快)
 */

const GITHUB_RAW_BASE = 'https://cdn.jsdelivr.net/gh/jiansenc/DeltaForceData@main/public/json';

// 数据文件映射 (使用实际文件名)
const DATA_FILES = {
  guns: {
    rifle:    `${GITHUB_RAW_BASE}/gun/rifle.json`,
    smg:      `${GITHUB_RAW_BASE}/gun/smg.json`,
    shotgun:  `${GITHUB_RAW_BASE}/gun/shotgun.json`,
    lmg:      `${GITHUB_RAW_BASE}/gun/lmg.json`,
    sniper:   `${GITHUB_RAW_BASE}/gun/sniper.json`,
    pistol:   `${GITHUB_RAW_BASE}/gun/pistol.json`,
  },
  accessories: {
    muzzle:    `${GITHUB_RAW_BASE}/acc/muzzle.json`,
    grip:      `${GITHUB_RAW_BASE}/acc/grip.json`,
    barrel:    `${GITHUB_RAW_BASE}/acc/barrel.json`,
    scope:     `${GITHUB_RAW_BASE}/acc/scope.json`,
    stock:     `${GITHUB_RAW_BASE}/acc/stock.json`,
  },
  protection: {
    armor:   `${GITHUB_RAW_BASE}/protect/armor.json`,
    helmet:  `${GITHUB_RAW_BASE}/protect/helmet.json`,
    bag:     `${GITHUB_RAW_BASE}/protect/bag.json`,
    chest:   `${GITHUB_RAW_BASE}/protect/chest.json`,
  }
};

// 解析 GitHub API 响应格式
function parseResponse(data) {
  // 兼容两种格式：{ ret: 0, jData: { data: { list: [...] } } } 或直接 { list: [...] }
  if (data.jData?.data?.list) {
    return data.jData.data.list;
  }
  if (data.jData?.data?.data?.list) {
    return data.jData.data.data.list;
  }
  if (data.data?.list) {
    return data.data.list;
  }
  if (Array.isArray(data)) {
    return data;
  }
  console.warn('⚠️ 未知数据格式，尝试直接解析');
  return data;
}

// 下载单个JSON文件
async function downloadJson(url, name) {
  try {
    console.log(`  📥 下载 ${name}...`);
    const response = await axios.get(url, { timeout: 30000 });
    const data = parseResponse(response.data);

    if (Array.isArray(data)) {
      console.log(`  ✅ ${name}: ${data.length} 条记录`);
      return data;
    } else {
      console.log(`  ✅ ${name}: 数据解析完成`);
      return data;
    }
  } catch (error) {
    console.error(`  ❌ 下载 ${name} 失败:`, error.message);
    return null;
  }
}

// 主函数
async function main() {
  console.log('🚀 开始从 GitHub 获取三角洲行动数据...');
  console.log(`⏰ 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`);
  console.log(`📡 数据源：https://github.com/jiansenc/DeltaForceData\n`);

  const results = {
    meta: {
      source: 'github.com/jiansenc/DeltaForceData',
      updateTime: new Date().toISOString(),
      dataVersion: 'main'
    },
    guns: {},
    accessories: {},
    protection: {}
  };

  // 1. 下载枪械数据
  console.log('📦 下载枪械数据...');
  for (const [type, url] of Object.entries(DATA_FILES.guns)) {
    const data = await downloadJson(url, `gun_${type}`);
    if (data) results.guns[type] = data;
  }

  // 2. 下载配件数据
  console.log('\n📦 下载配件数据...');
  for (const [type, url] of Object.entries(DATA_FILES.accessories)) {
    const data = await downloadJson(url, `acc_${type}`);
    if (data) results.accessories[type] = data;
  }

  // 3. 下载防护装备数据
  console.log('\n📦 下载防护装备数据...');
  for (const [type, url] of Object.entries(DATA_FILES.protection)) {
    const data = await downloadJson(url, `protect_${type}`);
    if (data) results.protection[type] = data;
  }

  // 统计信息
  const totalGuns = Object.values(results.guns).reduce((sum, arr) => sum + (Array.isArray(arr) ? arr.length : 0), 0);
  const totalAcc = Object.values(results.accessories).reduce((sum, arr) => sum + (Array.isArray(arr) ? arr.length : 0), 0);
  const totalProt = Object.values(results.protection).reduce((sum, arr) => sum + (Array.isArray(arr) ? arr.length : 0), 0);

  console.log('\n' + '='.repeat(50));
  console.log('📊 统计信息：');
  console.log(`   枪械总数: ${totalGuns}`);
  console.log(`   配件总数: ${totalAcc}`);
  console.log(`   防护装备: ${totalProt}`);
  console.log(`   总计: ${totalGuns + totalAcc + totalProt}`);
  console.log('='.repeat(50));

  // 保存到文件
  const dataDir = path.join(__dirname, '..');
  const outputFile = path.join(dataDir, 'game-data.json');

  fs.writeFileSync(outputFile, JSON.stringify(results, null, 2), 'utf8');
  console.log(`\n💾 数据已保存到 ${outputFile}`);
  console.log('✅ 数据更新完成！');
}

// 运行
main().catch(error => {
  console.error('❌ 脚本执行失败:', error.message);
  process.exit(1);
});
