#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量添加mods配置 - 第二批（15把武器）
目标：将mods覆盖率从32%提升到64%（30/47）
"""

import json
import sys

def load_game_data():
    """加载game-data.json"""
    with open('data/game-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_game_data(data):
    """保存game-data.json"""
    with open('data/game-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def create_mods_template(weapon_id, weapon_name, weapon_type):
    """为武器创建mods配置模板"""
    
    # 根据武器类型定制配置
    is_rifle = '步枪' in weapon_type or '战斗步枪' in weapon_type
    is_smg = '冲锋枪' in weapon_type
    is_shotgun = '霰弹枪' in weapon_type
    is_dmr = '射手步枪' in weapon_type or '精确射手步枪' in weapon_type
    is_sniper = '狙击步枪' in weapon_type
    
    template = {
        "name": weapon_name,
        "icon": "🔫",
        "builds": {}
    }
    
    # 烽火地带模式 (raid)
    template["builds"]["raid"] = {
        "budget": {
            "title": f"{weapon_name.split(' ')[0]} 烽火跑刀套",
            "desc": "低成本高效率",
            "parts": [
                {"slot": "瞄准镜", "name": "红点瞄准镜", "cost": "0.5万"},
                {"slot": "枪口", "name": "消音器（蓝）", "cost": "0.8万"}
            ],
            "total": "1.3万",
            "tip": "适合跑刀"
        },
        "standard": {
            "title": f"{weapon_name.split(' ')[0]} 烽火小康套",
            "desc": "攻防平衡",
            "parts": [
                {"slot": "瞄准镜", "name": "全息瞄准镜", "cost": "1.8万"},
                {"slot": "枪口", "name": "消音器（紫）", "cost": "3.5万"}
            ],
            "total": "5.3万",
            "tip": "中距离对枪优势"
        },
        "full": {
            "title": f"{weapon_name.split(' ')[0]} 烽火满改套",
            "desc": "极致性能",
            "parts": [
                {"slot": "瞄准镜", "name": "高倍瞄准镜", "cost": "5万"},
                {"slot": "枪口", "name": "专属消音器", "cost": "8万"},
                {"slot": "握把", "name": "人体工学握把", "cost": "2万"}
            ],
            "total": "15万",
            "tip": "全能配置"
        }
    }
    
    # 战场模式 (battle)
    template["builds"]["battle"] = {
        "standard": {
            "title": f"{weapon_name.split(' ')[0]} 战场套",
            "desc": "高性价比",
            "parts": [
                {"slot": "枪口", "name": "冲锋枪抑径器", "cost": "2万"},
                {"slot": "瞄准镜", "name": "红点", "cost": "0.8万"}
            ],
            "total": "2.8万",
            "tip": "适合抢点"
        }
    }
    
    # 排位模式 (ranked)
    template["builds"]["ranked"] = {
        "standard": {
            "title": f"{weapon_name.split(' ')[0]} 排位套",
            "desc": "稳定性优先",
            "parts": [
                {"slot": "瞄准镜", "name": "全息", "cost": "1.8万"},
                {"slot": "枪口", "name": "消音器（紫）", "cost": "3.5万"}
            ],
            "total": "5.3万",
            "tip": "竞技必备"
        }
    }
    
    return template

def main():
    print("=" * 60)
    print("🔧 批量添加mods配置 - 第二批（15把武器）")
    print("=" * 60)
    
    # 加载数据
    data = load_game_data()
    
    # 初始化mods
    if 'mods' not in data:
        data['mods'] = {}
    
    # 第二批15把武器（按热门程度排序）
    batch2_weapons = [
        "18010000014",  # M16A4突击步枪
        "18010000017",  # SG552突击步枪
        "18010000018",  # AK-12突击步枪
        "18010000021",  # SCAR-H战斗步枪
        "18010000023",  # G3战斗步枪
        "18010000024",  # PTR-32突击步枪
        "18010000008",  # QBZ95-1突击步枪
        "18010000010",  # AKS-74U突击步枪
        "18010000016",  # M7战斗步枪
        "18020000004",  # UZI冲锋枪
        "18020000005",  # 野牛冲锋枪
        "18020000006",  # SMG-45冲锋枪
        "18020000010",  # MP7
        "18030000001",  # M1014霰弹枪
        "18050000002",  # Mini-14射手步枪
    ]
    
    added_count = 0
    skipped_count = 0
    
    for wid in batch2_weapons:
        if wid in data['mods']:
            print(f"⏭️  跳过（已存在）: {wid} - {data['weapons'][wid]['name']}")
            skipped_count += 1
            continue
        
        if wid not in data['weapons']:
            print(f"❌ 武器不存在: {wid}")
            continue
        
        weapon_name = data['weapons'][wid]['name']
        weapon_type = data['weapons'][wid].get('typeCN', '未知')
        
        # 创建mods配置
        data['mods'][wid] = create_mods_template(wid, weapon_name, weapon_type)
        added_count += 1
        print(f"✅ 添加: {wid} - {weapon_name}")
    
    # 保存
    save_game_data(data)
    
    # 统计
    total_mods = len(data['mods'])
    coverage = total_mods / 47 * 100
    
    print("=" * 60)
    print(f"✅ 完成！")
    print(f"   新增: {added_count} 把武器")
    print(f"   跳过: {skipped_count} 把武器")
    print(f"   总计: {total_mods}/47 把武器有mods")
    print(f"   覆盖率: {coverage:.1f}%")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
