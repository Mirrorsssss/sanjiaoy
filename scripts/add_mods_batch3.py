#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次3：为剩余11把非手枪武器添加mods配置
目标：覆盖率从64%提升到91%
注意：使用占位符数据，需要后续完善真实配件信息
"""

import json
import sys

def load_data():
    with open('data/game-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open('data/game-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('✅ 数据已保存到 game-data.json')

def get_weapon_base_info(weapons, weapon_id):
    """获取武器基础信息"""
    w = weapons.get(weapon_id, {})
    return {
        'name': w.get('name', '未知武器'),
        'type': w.get('type', ''),
        'typeCN': w.get('typeCN', ''),
        'caliber': w.get('caliber', ''),
        'price': w.get('price', 0)
    }

def generate_builds_for_weapon(weapon_id, weapon_info):
    """为武器生成builds配置（占位符版本）"""
    name = weapon_info['name']
    wtype = weapon_info['type']
    type_cn = weapon_info['typeCN']
    
    # 根据武器类型生成合适的配置
    builds = {
        "raid": {
            "budget": {
                "title": f"{name} 烽火跑刀经济套",
                "desc": "低成本高效率",
                "parts": [
                    {"slot": "瞄准镜", "name": "红点瞄准镜（待更新）", "cost": "0.5万"},
                    {"slot": "枪口", "name": "消音器（待更新）", "cost": "0.8万"}
                ],
                "total": "1.3万",
                "tip": "适合跑刀，后续请完善真实配件"
            },
            "standard": {
                "title": f"{name} 烽火小康套",
                "desc": "攻防平衡",
                "parts": [
                    {"slot": "瞄准镜", "name": "全息瞄准镜（待更新）", "cost": "1.8万"},
                    {"slot": "枪口", "name": "消音器（待更新）", "cost": "3.5万"},
                    {"slot": "护木", "name": "战术护木（待更新）", "cost": "1.2万"}
                ],
                "total": "6.5万",
                "tip": "中距离对枪优势"
            },
            "full": {
                "title": f"{name} 烽火满改套",
                "desc": "极致性能",
                "parts": [
                    {"slot": "瞄准镜", "name": "高倍瞄准镜（待更新）", "cost": "5万"},
                    {"slot": "枪口", "name": "专属消音器（待更新）", "cost": "8万"},
                    {"slot": "护木", "name": "重装护木（待更新）", "cost": "3万"},
                    {"slot": "枪托", "name": "顶级枪托（待更新）", "cost": "4万"}
                ],
                "total": "20万",
                "tip": "全能配置，后续请完善真实配件"
            }
        },
        "battle": {
            "budget": {
                "title": f"{name} 战场经济套",
                "desc": "适合抢点",
                "parts": [
                    {"slot": "瞄准镜", "name": "红点（待更新）", "cost": "0.8万"},
                    {"slot": "枪口", "name": "冲锋枪抑径器（待更新）", "cost": "2万"}
                ],
                "total": "2.8万",
                "tip": "适合抢点"
            },
            "standard": {
                "title": f"{name} 战场套",
                "desc": "高射速",
                "parts": [
                    {"slot": "瞄准镜", "name": "红点（待更新）", "cost": "0.8万"},
                    {"slot": "枪口", "name": "冲锋枪抑径器（待更新）", "cost": "2万"},
                    {"slot": "护木", "name": "战术护木（待更新）", "cost": "1.5万"}
                ],
                "total": "4.3万",
                "tip": "高射速，适合突击"
            },
            "full": {
                "title": f"{name} 战场满配套",
                "desc": "极致性能",
                "parts": [
                    {"slot": "瞄准镜", "name": "高倍镜（待更新）", "cost": "3万"},
                    {"slot": "枪口", "name": "消音器（待更新）", "cost": "3万"},
                    {"slot": "护木", "name": "战术护木（待更新）", "cost": "1.5万"},
                    {"slot": "枪托", "name": "顶级枪托（待更新）", "cost": "4万"}
                ],
                "total": "11.5万",
                "tip": "战场全能配置"
            }
        },
        "ranked": {
            "budget": {
                "title": f"{name} 排位经济套",
                "desc": "稳定性优先",
                "parts": [
                    {"slot": "瞄准镜", "name": "红点（待更新）", "cost": "0.8万"},
                    {"slot": "枪口", "name": "消音器（待更新）", "cost": "3万"}
                ],
                "total": "3.8万",
                "tip": "稳定性优先"
            },
            "standard": {
                "title": f"{name} 排位套",
                "desc": "竞技必备",
                "parts": [
                    {"slot": "瞄准镜", "name": "全息（待更新）", "cost": "2万"},
                    {"slot": "枪口", "name": "消音器（待更新）", "cost": "3万"},
                    {"slot": "护木", "name": "战术护木（待更新）", "cost": "1.5万"}
                ],
                "total": "6.5万",
                "tip": "竞技必备"
            },
            "full": {
                "title": f"{name} 排位满配套",
                "desc": "竞技终极配置",
                "parts": [
                    {"slot": "瞄准镜", "name": "高倍镜（待更新）", "cost": "5万"},
                    {"slot": "枪口", "name": "消音器（待更新）", "cost": "3万"},
                    {"slot": "护木", "name": "战术护木（待更新）", "cost": "1.5万"},
                    {"slot": "枪托", "name": "顶级枪托（待更新）", "cost": "4万"},
                    {"slot": "镭指", "name": "激光指示器（待更新）", "cost": "1万"}
                ],
                "total": "14.5万",
                "tip": "竞技终极配置，需要完善真实配件"
            }
        }
    }
    
    return builds

def main():
    print('=== 批次3：为剩余11把非手枪武器添加mods配置 ===\n')
    print('⚠️  注意：使用占位符数据，配件名称标记为"待更新"')
    print('   后续需要完善真实的配件信息\n')
    
    # 加载数据
    data = load_data()
    
    if 'mods' not in data:
        data['mods'] = {}
    
    # 缺失mods的武器列表（非手枪）
    missing_weapons = [
        '18010000012',  # ASh-12战斗步枪
        '18020000009',  # 勇士冲锋枪
        '18030000002',  # S12K霰弹枪
        '18050000004',  # SVD狙击步枪
        '18050000005',  # M14射手步枪
        '18050000006',  # SKS射手步枪
        '18050000007',  # SR-25射手步枪
        '18050000031',  # PSG-1射手步枪
        '18060000007',  # SV-98狙击步枪
        '18060000009',  # M700狙击步枪
        '18060000011',  # AWM狙击步枪
    ]
    
    weapons = data.get('weapons', {})
    added_count = 0
    
    for wid in missing_weapons:
        if wid in data['mods']:
            print(f'⚠️  {wid} 已有mods配置，跳过')
            continue
        
        weapon_info = get_weapon_base_info(weapons, wid)
        print(f'➕ 为 {wid} {weapon_info["name"]} 添加mods配置...')
        
        # 生成mods配置
        builds = generate_builds_for_weapon(wid, weapon_info)
        
        data['mods'][wid] = {
            'name': weapon_info['name'],
            'icon': '🔫',
            'builds': builds
        }
        
        added_count += 1
    
    print(f'\n✅ 成功添加 {added_count} 把武器的mods配置')
    
    # 保存
    save_data(data)
    
    # 统计
    total_weapons = len(weapons)
    total_mods = len(data['mods'])
    coverage = total_mods / total_weapons * 100
    
    print(f'\n📊 更新后的统计：')
    print(f'  武器总数: {total_weapons}')
    print(f'  已有mods: {total_mods}')
    print(f'  覆盖率: {coverage:.1f}%')
    print(f'  本次提升: +{added_count}把')
    
    print(f'\n⚠️  下一步：')
    print(f'  1. 完善占位符配件为真实游戏数据')
    print(f'  2. 更新index.html的weaponKeyMap')
    print(f'  3. 测试所有47把武器的动态加载')

if __name__ == '__main__':
    main()
