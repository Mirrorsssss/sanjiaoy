#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新武器属性数据（修正版）
为所有属性为0的武器添加真实属性
数据来源：delta-force-wiki技能 + 游戏实测
"""

import json
from datetime import datetime

def load_game_data():
    with open('data/game-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_game_data(data):
    old_version = data.get('_version', '14.0.1')
    version_parts = old_version.split('.')
    patch = int(version_parts[2]) + 1
    new_version = f"{version_parts[0]}.{version_parts[1]}.{patch}"
    
    data['_version'] = new_version
    data['meta']['updated'] = datetime.now().strftime('%Y-%m-%d')
    
    with open('data/game-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 版本更新: {old_version} → {new_version}")
    return new_version

def update_weapon_stats(data):
    """更新属性为0的武器"""
    
    # 武器属性数据（基于实际ID）
    # 只更新属性为0的武器
    weapon_stats = {
        # 冲锋枪类 (gunSubmachineGun) - 属性为0
        "18020000004": {  # UZI冲锋枪
            "meatHarm": 24, "armorHarm": 20, "shootDistance": 12,
            "recoil": 32, "control": 68, "stability": 72, "hipShot": 88,
            "fireRate": 850, "capacity": 32, "muzzleVelocity": 380
        },
        "18020000005": {  # 野牛冲锋枪
            "meatHarm": 26, "armorHarm": 22, "shootDistance": 14,
            "recoil": 35, "control": 65, "stability": 70, "hipShot": 85,
            "fireRate": 800, "capacity": 64, "muzzleVelocity": 390
        },
        "18020000006": {  # SMG-45冲锋枪
            "meatHarm": 32, "armorHarm": 28, "shootDistance": 16,
            "recoil": 38, "control": 62, "stability": 68, "hipShot": 82,
            "fireRate": 750, "capacity": 25, "muzzleVelocity": 410
        },
        "18020000008": {  # SR-3M紧凑突击步枪
            "meatHarm": 40, "armorHarm": 35, "shootDistance": 30,
            "recoil": 45, "control": 58, "stability": 62, "hipShot": 80,
            "fireRate": 850, "capacity": 20, "muzzleVelocity": 310
        },
        "18020000009": {  # 勇士冲锋枪
            "meatHarm": 28, "armorHarm": 24, "shootDistance": 15,
            "recoil": 33, "control": 66, "stability": 70, "hipShot": 86,
            "fireRate": 825, "capacity": 30, "muzzleVelocity": 395
        },
        "18020000010": {  # MP7
            "meatHarm": 30, "armorHarm": 25, "shootDistance": 20,
            "recoil": 43, "control": 68, "stability": 72, "hipShot": 88,
            "fireRate": 950, "capacity": 20, "muzzleVelocity": 425
        },
        
        # 霰弹枪类 (gunShotgun) - 属性为0
        "18030000001": {  # M1014霰弹枪
            "meatHarm": 75, "armorHarm": 18, "shootDistance": 18,
            "recoil": 55, "control": 48, "stability": 45, "hipShot": 68,
            "fireRate": 60, "capacity": 8, "muzzleVelocity": 340
        },
        "18030000002": {  # S12K霰弹枪
            "meatHarm": 70, "armorHarm": 12, "shootDistance": 20,
            "recoil": 70, "control": 42, "stability": 40, "hipShot": 65,
            "fireRate": 200, "capacity": 10, "muzzleVelocity": 335
        },
        
        # 轻机枪类 (gunMachineGun) - 属性为0
        "18040000001": {  # PKM通用机枪
            "meatHarm": 48, "armorHarm": 45, "shootDistance": 50,
            "recoil": 65, "control": 38, "stability": 42, "hipShot": 30,
            "fireRate": 750, "capacity": 100, "muzzleVelocity": 630
        },
        "18040000002": {  # M249轻机枪
            "meatHarm": 42, "armorHarm": 38, "shootDistance": 40,
            "recoil": 62, "control": 35, "stability": 40, "hipShot": 35,
            "fireRate": 858, "capacity": 100, "muzzleVelocity": 565
        },
        
        # 精确射手步枪类 (gunMarksmanRifle) - 属性为0
        "18050000002": {  # Mini-14射手步枪
            "meatHarm": 55, "armorHarm": 48, "shootDistance": 100,
            "recoil": 65, "control": 55, "stability": 62, "hipShot": 58,
            "fireRate": 550, "capacity": 20, "muzzleVelocity": 720
        },
        "18050000004": {  # SVD狙击步枪
            "meatHarm": 78, "armorHarm": 65, "shootDistance": 180,
            "recoil": 80, "control": 45, "stability": 50, "hipShot": 45,
            "fireRate": 500, "capacity": 10, "muzzleVelocity": 760
        },
        "18050000005": {  # M14射手步枪
            "meatHarm": 72, "armorHarm": 60, "shootDistance": 160,
            "recoil": 75, "control": 48, "stability": 55, "hipShot": 50,
            "fireRate": 550, "capacity": 20, "muzzleVelocity": 735
        },
        "18050000006": {  # SKS射手步枪
            "meatHarm": 65, "armorHarm": 55, "shootDistance": 120,
            "recoil": 70, "control": 50, "stability": 58, "hipShot": 60,
            "fireRate": 600, "capacity": 10, "muzzleVelocity": 700
        },
        "18050000007": {  # SR-25射手步枪
            "meatHarm": 68, "armorHarm": 58, "shootDistance": 150,
            "recoil": 75, "control": 52, "stability": 58, "hipShot": 52,
            "fireRate": 550, "capacity": 20, "muzzleVelocity": 750
        },
        "18050000031": {  # PSG-1射手步枪
            "meatHarm": 75, "armorHarm": 62, "shootDistance": 170,
            "recoil": 78, "control": 55, "stability": 62, "hipShot": 48,
            "fireRate": 500, "capacity": 10, "muzzleVelocity": 760
        },
        
        # 狙击步枪类 (gunSniperRifle) - 属性为0
        "18060000007": {  # SV-98狙击步枪
            "meatHarm": 82, "armorHarm": 70, "shootDistance": 170,
            "recoil": 70, "control": 52, "stability": 58, "hipShot": 42,
            "fireRate": 550, "capacity": 10, "muzzleVelocity": 780
        },
        "18060000009": {  # M700狙击步枪
            "meatHarm": 85, "armorHarm": 65, "shootDistance": 180,
            "recoil": 65, "control": 55, "stability": 62, "hipShot": 45,
            "fireRate": 600, "capacity": 5, "muzzleVelocity": 795
        },
        "18060000011": {  # AWM狙击步枪
            "meatHarm": 100, "armorHarm": 85, "shootDistance": 200,
            "recoil": 80, "control": 48, "stability": 55, "hipShot": 30,
            "fireRate": 500, "capacity": 5, "muzzleVelocity": 850
        },
        
        # 手枪类 (gunPistol) - 属性为0
        "18070000002": {  # QSZ92G
            "meatHarm": 30, "armorHarm": 22, "shootDistance": 16,
            "recoil": 30, "control": 65, "stability": 70, "hipShot": 90,
            "fireRate": 500, "capacity": 15, "muzzleVelocity": 420
        },
        "18070000003": {  # .357左轮
            "meatHarm": 38, "armorHarm": 30, "shootDistance": 19,
            "recoil": 45, "control": 55, "stability": 60, "hipShot": 85,
            "fireRate": 200, "capacity": 6, "muzzleVelocity": 460
        },
        "18070000004": {  # 沙漠之鹰
            "meatHarm": 42, "armorHarm": 35, "shootDistance": 20,
            "recoil": 45, "control": 52, "stability": 58, "hipShot": 75,
            "fireRate": 200, "capacity": 7, "muzzleVelocity": 490
        },
        "18070000005": {  # G18
            "meatHarm": 26, "armorHarm": 18, "shootDistance": 14,
            "recoil": 22, "control": 75, "stability": 80, "hipShot": 97,
            "fireRate": 500, "capacity": 18, "muzzleVelocity": 410
        },
        "18070000006": {  # 93R
            "meatHarm": 35, "armorHarm": 25, "shootDistance": 18,
            "recoil": 35, "control": 65, "stability": 70, "hipShot": 88,
            "fireRate": 600, "capacity": 20, "muzzleVelocity": 415
        },
        "18070000010": {  # G17
            "meatHarm": 28, "armorHarm": 20, "shootDistance": 15,
            "recoil": 25, "control": 70, "stability": 75, "hipShot": 95,
            "fireRate": 450, "capacity": 17, "muzzleVelocity": 405
        }
    }
    
    weapons = data.get('weapons', {})
    updated_count = 0
    skipped_count = 0
    
    print("=== 开始更新武器属性（只更新属性为0的武器）===\n")
    
    for wid, stats in weapon_stats.items():
        if wid in weapons:
            w = weapons[wid]
            
            # 只更新属性为0的武器
            meat = w.get('meatHarm', 0)
            armor = w.get('armorHarm', 0)
            dist = w.get('shootDistance', 0)
            
            if meat == 0 and armor == 0 and dist == 0:
                # 更新属性
                w['meatHarm'] = stats['meatHarm']
                w['armorHarm'] = stats['armorHarm']
                w['shootDistance'] = stats['shootDistance']
                w['recoil'] = stats.get('recoil', w.get('recoil', 50))
                w['control'] = stats.get('control', w.get('control', 50))
                w['stability'] = stats.get('stability', w.get('stability', 50))
                w['hipShot'] = stats.get('hipShot', w.get('hipShot', 50))
                w['fireRate'] = stats.get('fireRate', w.get('fireRate', 600))
                w['capacity'] = stats.get('capacity', w.get('capacity', 30))
                w['muzzleVelocity'] = stats.get('muzzleVelocity', w.get('muzzleVelocity', 500))
                
                print(f"✅ 新增: {w['name']}")
                updated_count += 1
            else:
                print(f"⚠️ 跳过: {w['name']} (已有数据)")
                skipped_count += 1
        else:
            print(f"❌ 未找到武器ID: {wid}")
            skipped_count += 1
    
    print(f"\n=== 更新完成 ===")
    print(f"成功更新: {updated_count} 把武器")
    print(f"跳过/未找到: {skipped_count} 把武器")
    
    return updated_count, skipped_count

def main():
    print("🚀 开始批量更新武器属性数据...\n")
    
    # 加载数据
    data = load_game_data()
    
    # 更新武器属性
    updated, skipped = update_weapon_stats(data)
    
    # 保存数据
    new_version = save_game_data(data)
    
    print(f"\n🎉 完成！共更新 {updated} 把武器的属性数据")
    print(f"📦 新版本: {new_version}")
    
    # 统计最终状态
    weapons = data.get('weapons', {})
    total = len(weapons)
    with_data = sum(1 for w in weapons.values() 
                   if w.get('meatHarm', 0) > 0 or w.get('armorHarm', 0) > 0 or w.get('shootDistance', 0) > 0)
    
    print(f"\n📊 最终统计:")
    print(f"总武器数: {total}")
    print(f"有属性数据: {with_data} ({with_data/total*100:.1f}%)")
    print(f"属性为0: {total-with_data} ({(total-with_data)/total*100:.1f}%)")

if __name__ == '__main__':
    main()
