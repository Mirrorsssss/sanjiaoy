/**
 * 三角眼数据更新脚本
 * 用于从游戏数据网站抓取最新数据
 * 
 * 使用方法:
 *   node scripts/update-data.js
 * 
 * 需要先安装: npm install axios cheerio
 */

const fs = require('fs');
const path = require('path');

// 动态导入模块
async function loadDependencies() {
  try {
    const axios = require('axios');
    const cheerio = require('cheerio');
    return { axios, cheerio };
  } catch (e) {
    console.log('需要安装依赖: npm install axios cheerio');
    console.log('或手动更新 data/game-data.json');
    return null;
  }
}

// 数据来源配置
const DATA_SOURCES = {
  prices: {
    weapons: {
      url: 'https://sjz.jbskins.com/Item/index/category_id/4',
      type: 'table'
    },
    attachments: {
      url: 'https://sjz.jbskins.com/Item/index/category_id/2',
      type: 'table'
    },
    armor: {
      url: 'https://sjz.jbskins.com/Item/index/category_id/3',
      type: 'table'
    }
  }
};

class DataUpdater {
  constructor() {
    this.dataDir = path.join(__dirname, '..', 'data');
    this.dataFile = path.join(this.dataDir, 'game-data.json');
    this.logFile = path.join(this.dataDir, 'update-log.json');
  }

  // 加载现有数据
  loadExistingData() {
    try {
      const content = fs.readFileSync(this.dataFile, 'utf-8');
      return JSON.parse(content);
    } catch (e) {
      console.error('加载现有数据失败:', e.message);
      return null;
    }
  }

  // 保存数据
  saveData(data) {
    data._lastUpdate = new Date().toISOString();
    data.meta.lastUpdate = data._lastUpdate;
    
    fs.writeFileSync(
      this.dataFile,
      JSON.stringify(data, null, 2),
      'utf-8'
    );
    console.log('✓ 数据已保存到', this.dataFile);
  }

  // 记录更新日志
  logUpdate(type, status, details = '') {
    const logs = this.loadLogs();
    logs.push({
      timestamp: new Date().toISOString(),
      type,
      status,
      details
    });
    
    // 只保留最近100条记录
    const recentLogs = logs.slice(-100);
    
    fs.writeFileSync(
      this.logFile,
      JSON.stringify(recentLogs, null, 2),
      'utf-8'
    );
  }

  // 加载更新日志
  loadLogs() {
    try {
      const content = fs.readFileSync(this.logFile, 'utf-8');
      return JSON.parse(content);
    } catch (e) {
      return [];
    }
  }

  // 获取网页内容
  async fetchPage(url) {
    const { axios } = await loadDependencies();
    if (!axios) return null;

    try {
      const response = await axios.get(url, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        },
        timeout: 30000
      });
      return response.data;
    } catch (e) {
      console.error(`获取页面失败 ${url}:`, e.message);
      return null;
    }
  }

  // 解析道具列表（通用方法）
  parseItemList(html, category) {
    return new Promise(async (resolve) => {
      const { cheerio } = await loadDependencies();
      if (!cheerio || !html) {
        resolve([]);
        return;
      }

      const $ = cheerio.load(html);
      const items = [];

      // 根据网站结构调整选择器
      $('table tbody tr, .item-list .item, .item-card').each((i, el) => {
        const $el = $(el);
        
        // 尝试提取数据
        const name = $el.find('.name, .item-name, td:first').text().trim();
        const priceText = $el.find('.price, .item-price, td:nth(2)').text().trim();
        const levelText = $el.find('.level, .item-level, td:nth(3)').text().trim();

        // 解析价格（去除¥符号和逗号）
        const price = parseInt(priceText.replace(/[¥,]/g, '')) || 0;

        if (name && price > 0) {
          items.push({
            id: name.toLowerCase().replace(/\s+/g, '_'),
            name,
            price,
            level: parseInt(levelText) || 0,
            category
          });
        }
      });

      resolve(items);
    });
  }

  // 更新武器价格
  async updateWeapons() {
    console.log('\n📦 更新武器价格数据...');
    
    const { axios } = await loadDependencies();
    if (!axios) {
      console.log('⚠️ 无法自动更新，请参考 DATA_UPDATE_GUIDE.md 手动更新');
      return false;
    }

    let allWeapons = [];
    const pages = [1, 2, 3, 4]; // 根据实际页数调整

    for (const page of pages) {
      const url = page === 1 
        ? DATA_SOURCES.prices.weapons.url
        : `https://sjz.jbskins.com/Item/index/category_id/4/p/${page}.html`;
      
      console.log(`  获取第 ${page} 页...`);
      const html = await this.fetchPage(url);
      
      if (html) {
        const items = await this.parseItemList(html, 'weapon');
        allWeapons = allWeapons.concat(items);
      }
    }

    console.log(`  ✓ 获取到 ${allWeapons.length} 件武器数据`);
    return allWeapons;
  }

  // 更新配件价格
  async updateAttachments() {
    console.log('\n🔧 更新配件价格数据...');
    
    const { axios } = await loadDependencies();
    if (!axios) {
      console.log('⚠️ 无法自动更新');
      return [];
    }

    let allAttachments = [];
    const pages = [1, 2, 3]; // 根据实际页数调整

    for (const page of pages) {
      const url = page === 1 
        ? DATA_SOURCES.prices.attachments.url
        : `https://sjz.jbskins.com/Item/index/category_id/2/p/${page}.html`;
      
      console.log(`  获取第 ${page} 页...`);
      const html = await this.fetchPage(url);
      
      if (html) {
        const items = await this.parseItemList(html, 'attachment');
        allAttachments = allAttachments.concat(items);
      }
    }

    console.log(`  ✓ 获取到 ${allAttachments.length} 件配件数据`);
    return allAttachments;
  }

  // 执行完整更新
  async run() {
    console.log('='.repeat(50));
    console.log('三角眼数据更新工具');
    console.log('='.repeat(50));
    console.log(`开始时间: ${new Date().toLocaleString('zh-CN')}`);
    console.log('');

    // 加载现有数据
    const existingData = this.loadExistingData();
    if (!existingData) {
      console.error('无法加载现有数据文件');
      return;
    }

    // 更新武器数据
    const weapons = await this.updateWeapons();
    if (weapons.length > 0) {
      existingData.weapons = this.categorizeWeapons(weapons);
      this.logUpdate('weapons', 'success', `更新了 ${weapons.length} 件武器`);
    } else {
      this.logUpdate('weapons', 'skipped', '未获取到新数据');
    }

    // 更新配件数据
    const attachments = await this.updateAttachments();
    if (attachments.length > 0) {
      existingData.attachments = this.categorizeAttachments(attachments);
      this.logUpdate('attachments', 'success', `更新了 ${attachments.length} 件配件`);
    } else {
      this.logUpdate('attachments', 'skipped', '未获取到新数据');
    }

    // 保存更新后的数据
    this.saveData(existingData);

    console.log('\n' + '='.repeat(50));
    console.log('更新完成!');
    console.log('='.repeat(50));
  }

  // 分类武器
  categorizeWeapons(weapons) {
    const categories = {
      pistol: { name: '手枪', items: [] },
      smg: { name: '冲锋枪', items: [] },
      rifle: { name: '突击步枪', items: [] },
      dmr: { name: '射手步枪', items: [] },
      sniper: { name: '狙击步枪', items: [] },
      lmg: { name: '轻机枪', items: [] },
      shotgun: { name: '霰弹枪', items: [] }
    };

    const keywords = {
      pistol: ['g17', 'g18', '93r', '沙漠', '左轮', 'qsz', 'm1911', '1911'],
      smg: ['p90', 'mp5', 'vector', 'uzi', '凯迪', 'kedi'],
      dmr: ['vss', 'psg', 'sr25', 'm110', '射手'],
      sniper: ['awm', 'm700', 'r93', 'sv98', 'm82', '狙击'],
      lmg: ['m249', 'pkm', 'dp28', 'm250', '机枪'],
      shotgun: ['m870', 'm1014', 'saiga', '霰弹']
    };

    weapons.forEach(w => {
      const nameLower = w.name.toLowerCase();
      let placed = false;

      for (const [cat, kws] of Object.entries(keywords)) {
        if (kws.some(k => nameLower.includes(k))) {
          categories[cat].items.push(w);
          placed = true;
          break;
        }
      }

      if (!placed) {
        // 默认归类为步枪
        categories.rifle.items.push(w);
      }
    });

    return categories;
  }

  // 分类配件
  categorizeAttachments(attachments) {
    const categories = {
      muzzle: { name: '枪口', items: [] },
      optic: { name: '瞄准镜', items: [] },
      stock: { name: '枪托', items: [] },
      grip: { name: '握把', items: [] },
      magazine: { name: '弹匣', items: [] },
      foregrip: { name: '护木', items: [] }
    };

    const keywords = {
      muzzle: ['消音', '制退', '制动', 'muzzle'],
      optic: ['红点', '全息', 'acog', '倍镜', '瞄准镜'],
      stock: ['枪托', '托芯', '尾盖', 'stock'],
      grip: ['握把', 'grip'],
      magazine: ['弹匣', '弹鼓', 'mag'],
      foregrip: ['护木', 'foregrip', 'rail']
    };

    attachments.forEach(a => {
      const nameLower = a.name.toLowerCase();
      let placed = false;

      for (const [cat, kws] of Object.entries(keywords)) {
        if (kws.some(k => nameLower.includes(k))) {
          categories[cat].items.push(a);
          placed = true;
          break;
        }
      }

      if (!placed) {
        categories.grip.items.push(a);
      }
    });

    return categories;
  }
}

// 运行更新
const updater = new DataUpdater();
updater.run().catch(console.error);
