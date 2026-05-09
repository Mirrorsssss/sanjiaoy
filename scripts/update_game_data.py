#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
补充 game-data.json 缺失的关键数据：
1. ammo 子弹数据（从JS的bulletData迁移到JSON）
2. workshop 工坊制造配方
3. builds 推荐配置
4. 为武器/配件添加price字段（估算）
"""

import json
import sys

# 读取现有数据
with open('data/game-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"原始数据版本: {data.get('_version')}")
print(f"原始数据来源: {data.get('_source')}")

# 1. 添加子弹数据 (ammo)
ammo_data = {
    "ammo7.62x39": {
        "id": "ammo7.62x39",
        "name": "7.62x39mm弹药",
        "caliber": "7.62x39",
        "type": "rifle",
        "grade": 2,
        "price": 120,
        "damage": 43,
        "pen": 26,
        "description": "AKM等武器使用的7.62x39mm弹药，性价比赛用"
    },
    "ammo5.56x45": {
        "id": "ammo5.56x45",
        "name": "5.56x45mm弹药",
        "caliber": "5.56x45",
        "type": "rifle",
        "grade": 2,
        "price": 200,
        "damage": 38,
        "pen": 28,
        "description": "M4A1等武器使用的5.56x45mm弹药，综合性能强"
    },
    "ammo5.45x39": {
        "id": "ammo5.45x39",
        "name": "5.45x39mm弹药",
        "caliber": "5.45x39",
        "type": "rifle",
        "grade": 2,
        "price": 190,
        "damage": 40,
        "pen": 30,
        "description": "AKS-74U等武器使用的5.45x39mm弹药，穿透优秀"
    },
    "ammo9x19": {
        "id": "ammo9x19",
        "name": "9x19mm弹药",
        "caliber": "9x19",
        "type": "pistol",
        "grade": 2,
        "price": 160,
        "damage": 35,
        "pen": 30,
        "description": "Vector等武器使用的9x19mm弹药，穿甲手枪弹首选"
    },
    "ammo12gauge": {
        "id": "ammo12gauge",
        "name": "12号霰弹",
        "caliber": "12g",
        "type": "shotgun",
        "grade": 2,
        "price": 300,
        "damage": 120,
        "pen": 15,
        "description": "M870等霰弹枪使用的12号霰弹，单发精准中距离"
    },
    "ammo338lapua": {
        "id": "ammo338lapua",
        "name": ".338 Lapua弹药",
        "caliber": "338",
        "type": "sniper",
        "grade": 4,
        "price": 450,
        "damage": 85,
        "pen": 45,
        "description": "M24等狙击枪使用的.338 Lapua弹药，狙击专用穿甲"
    },
    "ammo300blk": {
        "id": "ammo300blk",
        "name": ".300 BLK弹药",
        "caliber": "300",
        "type": "subsonic",
        "grade": 3,
        "price": 200,
        "damage": 35,
        "pen": 20,
        "description": ".300 BLK专用弹药，亚音速消音冲锋"
    },
    "ammo12.7x55": {
        "id": "ammo12.7x55",
        "name": "12.7x55mm弹药",
        "caliber": "127",
        "type": "heavy",
        "grade": 4,
        "price": 350,
        "damage": 56,
        "pen": 55,
        "description": "ASH-12专用大口径弹药，穿甲能力极强"
    }
}

# 2. 添加工坊制造配方 (workshop)
workshop_data = [
    {
        "id": "w_medkit",
        "name": "急救包",
        "type": "consumable",
        "grade": 2,
        "materials": [
            {"id": "c_gauze", "name": "绷带", "quantity": 3},
            {"id": "c_saline", "name": "生理盐水", "quantity": 1}
        ],
        "craft_time": "10分钟",
        "description": "恢复大量生命值，战备必备消耗品"
    },
    {
        "id": "w_painkiller",
        "name": "止疼药",
        "type": "consumable",
        "grade": 2,
        "materials": [
            {"id": "c_herb", "name": "草药", "quantity": 2},
            {"id": "c_bandage", "name": "绷带", "quantity": 2}
        ],
        "craft_time": "8分钟",
        "description": "止疼并提升体力上限"
    },
    {
        "id": "w_vest2",
        "name": "二级护甲",
        "type": "armor",
        "grade": 2,
        "materials": [
            {"id": "m_steel", "name": "钢材", "quantity": 5},
            {"id": "m_kevlar", "name": "凯夫拉纤维", "quantity": 2}
        ],
        "craft_time": "30分钟",
        "description": "二级防护护甲，性价比赛用"
    },
    {
        "id": "w_helmet2",
        "name": "二级头盔",
        "type": "armor",
        "grade": 2,
        "materials": [
            {"id": "m_steel", "name": "钢材", "quantity": 3},
            {"id": "m_kevlar", "name": "凯夫拉纤维", "quantity": 1}
        ],
        "craft_time": "25分钟",
        "description": "二级防护头盔"
    },
    {
        "id": "w_backpack_m",
        "name": "中型背包",
        "type": "bag",
        "grade": 2,
        "materials": [
            {"id": "m_cloth", "name": "织物", "quantity": 8},
            {"id": "m_steel", "name": "钢材", "quantity": 2}
        ],
        "craft_time": "20分钟",
        "description": "24格容量中型背包"
    }
]

# 3. 添加推荐配置 (builds)
builds_data = [
    {
        "id": "b_rush_raid",
        "name": "烽火跑刀套",
        "mode": "raid",
        "budget": "penny",
        "total_cost": 3.5,
        "items": [
            {"id": "18010000001", "name": "M4A1突击步枪", "slot": "primary"},
            {"id": "c_medkit", "name": "急救包", "slot": "consumable"},
            {"id": "c_bandage", "name": "绷带", "slot": "consumable"}
        ],
        "description": "低成本跑刀配置，适合新手"
    },
    {
        "id": "b_standard_raid",
        "name": "烽火小康套",
        "mode": "raid",
        "budget": "normal",
        "total_cost": 15.0,
        "items": [
            {"id": "18010000006", "name": "AKM突击步枪", "slot": "primary"},
            {"id": "a_vest2", "name": "二级护甲", "slot": "armor"},
            {"id": "a_helmet2", "name": "二级头盔", "slot": "helmet"},
            {"id": "c_medkit", "name": "急救包", "slot": "consumable"}
        ],
        "description": "均衡型烽火地带配置"
    }
]

# 4. 为武器添加price字段（根据game中实际价格估算）
price_map = {
    "18010000001": 35000,  # M4A1
    "18010000006": 48000,  # AKM
    "18010000008": 30000,  # QBZ95-1
    "18010000010": 25000,  # AKS-74U
}

print("\n开始补充数据...")
print(f"  - 子弹数据: {len(ammo_data)} 种")
print(f"  - 工坊配方: {len(workshop_data)} 个")
print(f"  - 推荐配置: {len(builds_data)} 个")

# 更新数据
data['ammo'] = ammo_data
data['workshop'] = workshop_data
data['builds'] = builds_data

# 为武器添加price字段
weapons = data.get('weapons', {})
for wid, price in price_map.items():
    if wid in weapons:
        weapons[wid]['price'] = price
        print(f"  ✓ 添加价格: {weapons[wid]['name']} = {price/10000}万")

# 更新版本号
data['_version'] = "12.0.0-real"
data['_updated'] = "2026-05-09"

# 保存
with open('data/game-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✅ 数据补充完成！")
print(f"  - 子弹数据: {len(data['ammo'])} 种")
print(f"  - 工坊配方: {len(data['workshop'])} 个")
print(f"  - 推荐配置: {len(data['builds'])} 个")
print(f"  - 版本号: {data['_version']}")
