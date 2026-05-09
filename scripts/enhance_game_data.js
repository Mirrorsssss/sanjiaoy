/**
 * 增强game-data.json - 添加gear数据和扩充builds
 * 作为产品经理的自主完善行动
 */

const fs = require('fs');
const path = require('path');

const DATA_FILE = path.join(__dirname, '..', 'data', 'game-data.json');

console.log('🚀 开始增强game-data.json...');

// 读取现有数据
let data;
try {
  const raw = fs.readFileSync(DATA_FILE, 'utf8');
  data = JSON.parse(raw);
  console.log('✅ 成功读取现有数据');
} catch (e) {
  console.error('❌ 读取失败:', e.message);
  process.exit(1);
}

// ========== 1. 添加gear（防具）数据 ==========
console.log('\n📦 添加gear（防具）数据...');

data.gear = {
  // 头盔
  "a_helmet1": {
    "id": "a_helmet1",
    "name": "一级头盔",
    "type": "helmet",
    "typeCN": "头盔",
    "grade": 1,
    "defense": 15,
    "durability": 50,
    "weight": 1.2,
    "price": 5000,
    "description": "基础防护头盔，适合新手"
  },
  "a_helmet2": {
    "id": "a_helmet2",
    "name": "二级头盔",
    "type": "helmet",
    "typeCN": "头盔",
    "grade": 2,
    "defense": 25,
    "durability": 80,
    "weight": 1.8,
    "price": 12000,
    "description": "标准战术头盔，性价比高"
  },
  "a_helmet3": {
    "id": "a_helmet3",
    "name": "三级头盔",
    "type": "helmet",
    "typeCN": "头盔",
    "grade": 3,
    "defense": 35,
    "durability": 120,
    "weight": 2.5,
    "price": 25000,
    "description": "高级防弹头盔，强力防护"
  },
  "a_helmet4": {
    "id": "a_helmet4",
    "name": "四级头盔",
    "type": "helmet",
    "typeCN": "头盔",
    "grade": 4,
    "defense": 50,
    "durability": 180,
    "weight": 3.2,
    "price": 45000,
    "description": "顶级战术头盔，极致防护"
  },

  // 护甲
  "a_vest1": {
    "id": "a_vest1",
    "name": "一级护甲",
    "type": "vest",
    "typeCN": "护甲",
    "grade": 1,
    "defense": 20,
    "durability": 60,
    "weight": 2.5,
    "price": 8000,
    "description": "基础防护护甲"
  },
  "a_vest2": {
    "id": "a_vest2",
    "name": "二级护甲",
    "type": "vest",
    "typeCN": "护甲",
    "grade": 2,
    "defense": 35,
    "durability": 100,
    "weight": 3.8,
    "price": 18000,
    "description": "标准战术护甲，均衡防护"
  },
  "a_vest3": {
    "id": "a_vest3",
    "name": "三级护甲",
    "type": "vest",
    "typeCN": "护甲",
    "grade": 3,
    "defense": 50,
    "durability": 150,
    "weight": 5.2,
    "price": 35000,
    "description": "高级防弹护甲，重型防护"
  },
  "a_vest4": {
    "id": "a_vest4",
    "name": "四级护甲",
    "type": "vest",
    "typeCN": "护甲",
    "grade": 4,
    "defense": 65,
    "durability": 200,
    "weight": 6.8,
    "price": 60000,
    "description": "顶级战术护甲，极致防御"
  },

  // 背包
  "bag1": {
    "id": "bag1",
    "name": "小型背包",
    "type": "bag",
    "typeCN": "背包",
    "grade": 1,
    "capacity": 12,
    "weight": 0.8,
    "price": 3000,
    "description": "12格容量，适合跑刀"
  },
  "bag2": {
    "id": "bag2",
    "name": "中型背包",
    "type": "bag",
    "typeCN": "背包",
    "grade": 2,
    "capacity": 24,
    "weight": 1.5,
    "price": 8000,
    "description": "24格容量，均衡选择"
  },
  "bag3": {
    "id": "bag3",
    "name": "大型背包",
    "type": "bag",
    "typeCN": "背包",
    "grade": 3,
    "capacity": 36,
    "weight": 2.5,
    "price": 15000,
    "description": "36格容量，适合搜集"
  },
  "bag4": {
    "id": "bag4",
    "name": "军用背包",
    "type": "bag",
    "typeCN": "背包",
    "grade": 4,
    "capacity": 48,
    "weight": 3.5,
    "price": 28000,
    "description": "48格超大容量，大佬专用"
  },

  // 胸挂
  "rig1": {
    "id": "rig1",
    "name": "基础胸挂",
    "type": "rig",
    "typeCN": "胸挂",
    "grade": 1,
    "capacity": 4,
    "weight": 0.5,
    "price": 2000,
    "description": "4格弹匣容量"
  },
  "rig2": {
    "id": "rig2",
    "name": "战术胸挂",
    "type": "rig",
    "typeCN": "胸挂",
    "grade": 2,
    "capacity": 6,
    "weight": 0.8,
    "price": 5000,
    "description": "6格弹匣容量，常用选择"
  },
  "rig3": {
    "id": "rig3",
    "name": "高级胸挂",
    "type": "rig",
    "typeCN": "胸挂",
    "grade": 3,
    "capacity": 8,
    "weight": 1.2,
    "price": 10000,
    "description": "8格弹匣容量，火力持续"
  }
};

console.log(`✅ 添加了 ${Object.keys(data.gear).length} 件防具`);

// ========== 2. 扩充builds（推荐配置）==========
console.log('\n📦 扩充builds（推荐配置）...');

const newBuilds = [
  // 烽火地带 - 跑刀流
  {
    "id": "b_rush_raid_2",
    "name": "烽火跑刀进阶套",
    "mode": "raid",
    "budget": "penny",
    "total_cost": 5.5,
    "items": [
      {"id": "18010000010", "name": "AKS-74U突击步枪", "slot": "primary"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"},
      {"id": "c_bandage", "name": "绷带", "slot": "consumable"},
      {"id": "bag1", "name": "小型背包", "slot": "bag"}
    ],
    "description": "低成本跑刀进阶配置，AKS-74U高机动"
  },

  // 烽火地带 - 小康流
  {
    "id": "b_standard_raid_2",
    "name": "烽火小康流2",
    "mode": "raid",
    "budget": "normal",
    "total_cost": 18,
    "items": [
      {"id": "18010000001", "name": "M4A1突击步枪", "slot": "primary"},
      {"id": "a_vest2", "name": "二级护甲", "slot": "armor"},
      {"id": "a_helmet2", "name": "二级头盔", "slot": "helmet"},
      {"id": "rig2", "name": "战术胸挂", "slot": "rig"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"}
    ],
    "description": "均衡型烽火地带配置，M4A1稳定输出"
  },

  // 烽火地带 - 富裕流
  {
    "id": "b_rich_raid",
    "name": "烽火富裕套",
    "mode": "raid",
    "budget": "rich",
    "total_cost": 35,
    "items": [
      {"id": "18010000013", "name": "K416突击步枪", "slot": "primary"},
      {"id": "a_vest3", "name": "三级护甲", "slot": "armor"},
      {"id": "a_helmet3", "name": "三级头盔", "slot": "helmet"},
      {"id": "rig3", "name": "高级胸挂", "slot": "rig"},
      {"id": "bag2", "name": "中型背包", "slot": "bag"},
      {"id": "c_adv_medkit", "name": "高级医疗包", "slot": "consumable"}
    ],
    "description": "高性能烽火地带配置，K416高射速压制"
  },

  // 烽火地带 - VIP流
  {
    "id": "b_vip_raid",
    "name": "烽火VIP套装",
    "mode": "raid",
    "budget": "vip",
    "total_cost": 60,
    "items": [
      {"id": "18010000013", "name": "K416突击步枪", "slot": "primary"},
      {"id": "a_vest4", "name": "四级护甲", "slot": "armor"},
      {"id": "a_helmet4", "name": "四级头盔", "slot": "helmet"},
      {"id": "rig3", "name": "高级胸挂", "slot": "rig"},
      {"id": "bag3", "name": "大型背包", "slot": "bag"},
      {"id": "c_adv_medkit", "name": "高级医疗包", "slot": "consumable"},
      {"id": "c_tactical", "name": "战术装备", "slot": "consumable"}
    ],
    "description": "顶级烽火地带配置，无惧任何对手"
  },

  // 对战模式 - 跑刀流
  {
    "id": "b_rush_battle",
    "name": "对战跑刀套",
    "mode": "battle",
    "budget": "penny",
    "total_cost": 4,
    "items": [
      {"id": "18020000001", "name": "MP5冲锋枪", "slot": "primary"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"},
      {"id": "bag1", "name": "小型背包", "slot": "bag"}
    ],
    "description": "对战模式低成本配置，MP5高射速"
  },

  // 对战模式 - 小康流
  {
    "id": "b_standard_battle",
    "name": "对战小康套",
    "mode": "battle",
    "budget": "normal",
    "total_cost": 20,
    "items": [
      {"id": "18010000006", "name": "AKM突击步枪", "slot": "primary"},
      {"id": "a_vest2", "name": "二级护甲", "slot": "armor"},
      {"id": "a_helmet2", "name": "二级头盔", "slot": "helmet"},
      {"id": "rig2", "name": "战术胸挂", "slot": "rig"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"}
    ],
    "description": "对战模式均衡配置，AKM强力输出"
  },

  // 排位模式 - 标准流
  {
    "id": "b_standard_ranked",
    "name": "排位标准套",
    "mode": "ranked",
    "budget": "normal",
    "total_cost": 22,
    "items": [
      {"id": "18010000001", "name": "M4A1突击步枪", "slot": "primary"},
      {"id": "a_vest3", "name": "三级护甲", "slot": "armor"},
      {"id": "a_helmet2", "name": "二级头盔", "slot": "helmet"},
      {"id": "rig2", "name": "战术胸挂", "slot": "rig"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"}
    ],
    "description": "排位模式稳健配置，重视生存"
  },

  // 排位模式 - 富裕流
  {
    "id": "b_rich_ranked",
    "name": "排位富裕套",
    "mode": "ranked",
    "budget": "rich",
    "total_cost": 40,
    "items": [
      {"id": "18010000013", "name": "K416突击步枪", "slot": "primary"},
      {"id": "a_vest3", "name": "三级护甲", "slot": "armor"},
      {"id": "a_helmet3", "name": "三级头盔", "slot": "helmet"},
      {"id": "rig3", "name": "高级胸挂", "slot": "rig"},
      {"id": "bag2", "name": "中型背包", "slot": "bag"},
      {"id": "c_adv_medkit", "name": "高级医疗包", "slot": "consumable"}
    ],
    "description": "排位模式高性能配置，力争上游"
  },

  // 特殊：狙击流
  {
    "id": "b_sniper_raid",
    "name": "烽火狙击套",
    "mode": "raid",
    "budget": "rich",
    "total_cost": 38,
    "items": [
      {"id": "18010000017", "name": "AWM狙击步枪", "slot": "primary"},
      {"id": "a_vest2", "name": "二级护甲", "slot": "armor"},
      {"id": "a_helmet3", "name": "三级头盔", "slot": "helmet"},
      {"id": "rig2", "name": "战术胸挂", "slot": "rig"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"}
    ],
    "description": "狙击手专用配置，一击致命"
  },

  // 特殊：机枪火力压制
  {
    "id": "b_lmg_raid",
    "name": "烽火机枪套",
    "mode": "raid",
    "budget": "rich",
    "total_cost": 32,
    "items": [
      {"id": "18040000001", "name": "PKM通用机枪", "slot": "primary"},
      {"id": "a_vest3", "name": "三级护甲", "slot": "armor"},
      {"id": "a_helmet2", "name": "二级头盔", "slot": "helmet"},
      {"id": "rig3", "name": "高级胸挂", "slot": "rig"},
      {"id": "bag2", "name": "中型背包", "slot": "bag"},
      {"id": "c_medkit", "name": "急救包", "slot": "consumable"}
    ],
    "description": "火力压制配置，PKM持续输出"
  }
];

// 合并现有builds和新builds
data.builds = [...data.builds, ...newBuilds];
console.log(`✅ 扩充了 ${newBuilds.length} 个推荐配置，总计 ${data.builds.length} 个`);

// ========== 3. 为consumables添加price字段 ==========
console.log('\n📦 为consumables添加price字段...');

const priceMap = {
  "14060000003": 15000, // 高级头盔维修组合
  "14060000001": 8000,  // 维修工具包（示例）
  "14010000001": 500,   // 绷带
  "14010000002": 2000,  // 急救包
  "14010000003": 5000,  // 高级医疗包
};

let priceAdded = 0;
for (const [id, item] of Object.entries(data.consumables || {})) {
  if (!item.price && priceMap[id]) {
    item.price = priceMap[id];
    priceAdded++;
  }
}
console.log(`✅ 为 ${priceAdded} 个消耗品添加了price字段`);

// ========== 4. 更新版本和时间 ==========
data._version = "12.1.0";
data._updated = "2026-05-09";

// ========== 5. 保存文件 ==========
console.log('\n💾 保存文件...');
try {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2), 'utf8');
  console.log('✅ 成功保存 game-data.json');
  console.log(`📊 文件大小: ${(fs.statSync(DATA_FILE).size / 1024).toFixed(2)} KB`);
} catch (e) {
  console.error('❌ 保存失败:', e.message);
  process.exit(1);
}

// ========== 6. 输出统计 ==========
console.log('\n========== 完成统计 ==========');
console.log('武器:', Object.keys(data.weapons || {}).length);
console.log('配件:', Object.keys(data.attachments || {}).length);
console.log('子弹:', Object.keys(data.ammo || {}).length);
console.log('消耗品:', Object.keys(data.consumables || {}).length);
console.log('防具:', Object.keys(data.gear || {}).length);
console.log('钥匙卡:', Object.keys(data.keys || {}).length);
console.log('收藏品:', Object.keys(data.collectibles || {}).length);
console.log('工坊配方:', Object.keys(data.workshop || {}).length);
console.log('推荐配置:', data.builds?.length || 0);
console.log('===============================');
console.log('\n🎉 数据增强完成！');
