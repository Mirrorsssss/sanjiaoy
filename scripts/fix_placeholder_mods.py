#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复mods配置中的占位符数据
将"待更新"占位符改为通用配件名称
"""
import json
import re

def load_data():
    with open('data/game-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open('data/game-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('✅ 数据已保存到 game-data.json')

def fix_placeholder_text(text):
    """移除'待更新'字样"""
    if isinstance(text, str):
        return text.replace('（待更新）', '').replace('(待更新)', '')
    return text

def fix_builds(builds):
    """递归修复builds中的所有占位符"""
    if isinstance(builds, dict):
        for key, value in builds.items():
            if key == 'name':
                builds[key] = fix_placeholder_text(value)
            elif key == 'tip':
                # 更新tip，移除"后续请完善"之类的提示
                if isinstance(value, str) and '待更新' in value:
                    builds[key] = value.replace('，后续请完善真实配件', '').replace('需要完善真实配件', '')
            else:
                fix_builds(value)
    elif isinstance(builds, list):
        for item in builds:
            fix_builds(item)

def main():
    print('=== 修复mods配置中的占位符数据 ===\n')
    
    data = load_data()
    
    if 'mods' not in data:
        print('⚠️  没有mods数据')
        return
    
    fixed_count = 0
    for weapon_id, mod_data in data['mods'].items():
        if 'builds' in mod_data:
            old_data = json.dumps(mod_data['builds'], ensure_ascii=False)
            fix_builds(mod_data['builds'])
            new_data = json.dumps(mod_data['builds'], ensure_ascii=False)
            
            if old_data != new_data:
                fixed_count += 1
                weapon_name = mod_data.get('name', weapon_id)
                print(f'✅ 修复 {weapon_name} 的占位符')
    
    print(f'\n✅ 总共修复 {fixed_count} 把武器的占位符')
    
    # 保存
    save_data(data)
    
    print('\n💡 下一步：')
    print('  1. 为每把武器完善真实的配件数据')
    print('  2. 更新配件的cost为真实价格')
    print('  3. 测试所有武器的动态加载')

if __name__ == '__main__':
    main()
