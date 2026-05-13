#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 GitHub 免费数据源获取三角洲行动数据
数据源: https://github.com/jiansenc/DeltaForceData
使用 ghproxy 代理加速国内访问
"""

import json
import os
import sys
import time
import requests

# 配置
GITHUB_RAW = "https://raw.githubusercontent.com/jiansenc/DeltaForceData/main/public/json"
PROXY_BASE = "https://mirror.ghproxy.com/" + GITHUB_RAW

# 要下载的文件映射
FILES_TO_DOWNLOAD = {
    "guns": ["rifle.json", "smg.json", "shotgun.json", "lmg.json", "sniper.json", "pistol.json"],
    "acc": ["muzzle.json", "grip.json", "barrel.json", "scope.json", "stock.json"],
    "protect": ["armor.json", "helmet.json", "bag.json", "chest.json"]
}

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "game-data.json")

def download_file(session, url, name):
    """下载单个文件"""
    try:
        print(f"  📥 下载 {name}...")
        # 尝试使用代理
        proxy_url = url.replace(GITHUB_RAW, PROXY_BASE)
        
        resp = session.get(proxy_url, timeout=30)
        if resp.status_code != 200:
            # 如果代理失败，尝试直连
            print(f"  ⚠️  代理失败 ({resp.status_code})，尝试直连...")
            resp = session.get(url, timeout=30)
        
        resp.raise_for_status()
        data = resp.json()
        
        # 解析嵌套结构
        if isinstance(data, dict):
            if "jData" in data and "data" in data["jData"]:
                inner = data["jData"]["data"]
                if "list" in inner:
                    return inner["list"]
        
        print(f"  ✅ {name}: {len(data) if isinstance(data, list) else 'OK'}")
        return data
        
    except Exception as e:
        print(f"  ❌ 下载 {name} 失败: {e}")
        return None

def main():
    print("🚀 开始从 GitHub 获取三角洲行动数据...")
    print(f"⏰ 更新时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📡 数据源：https://github.com/jiansenc/DeltaForceData\n")
    
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    results = {
        "meta": {
            "source": "github.com/jiansenc/DeltaForceData",
            "updateTime": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            "dataVersion": "main"
        },
        "guns": {},
        "accessories": {},
        "protection": {}
    }
    
    total_count = 0
    
    # 1. 下载枪械
    print("🔫 下载枪械数据...")
    for fname in FILES_TO_DOWNLOAD["guns"]:
        ftype = fname.replace(".json", "")
        url = f"{GITHUB_RAW}/gun/{fname}"
        data = download_file(session, url, f"gun_{ftype}")
        if data:
            results["guns"][ftype] = data
            if isinstance(data, list):
                total_count += len(data)
        time.sleep(0.5)
    
    # 2. 下载配件
    print("\n🔧 下载配件数据...")
    for fname in FILES_TO_DOWNLOAD["acc"]:
        ftype = fname.replace(".json", "")
        url = f"{GITHUB_RAW}/acc/{fname}"
        data = download_file(session, url, f"acc_{ftype}")
        if data:
            results["accessories"][ftype] = data
            if isinstance(data, list):
                total_count += len(data)
        time.sleep(0.5)
    
    # 3. 下载防护
    print("\n🛡️  下载防护装备数据...")
    for fname in FILES_TO_DOWNLOAD["protect"]:
        ftype = fname.replace(".json", "")
        url = f"{GITHUB_RAW}/protect/{fname}"
        data = download_file(session, url, f"protect_{ftype}")
        if data:
            results["protection"][ftype] = data
            if isinstance(data, list):
                total_count += len(data)
        time.sleep(0.5)
    
    # 统计
    print("\n" + "=" * 50)
    print("📊 统计信息：")
    gun_count = sum(len(v) if isinstance(v, list) else 0 for v in results["guns"].values())
    acc_count = sum(len(v) if isinstance(v, list) else 0 for v in results["accessories"].values())
    prot_count = sum(len(v) if isinstance(v, list) else 0 for v in results["protection"].values())
    
    print(f"   枪械总数: {gun_count}")
    print(f"   配件总数: {acc_count}")
    print(f"   防护装备: {prot_count}")
    print(f"   总计: {gun_count + acc_count + prot_count}")
    print("=" * 50)
    
    # 保存
    output_path = os.path.abspath(OUTPUT_FILE)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 数据已保存到 {output_path}")
    print("✅ 数据更新完成！")

if __name__ == "__main__":
    main()
