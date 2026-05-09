import json

# Load existing data
with open('data/game-data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

# Define mods for 10 popular weapons
new_mods = {
    '18010000006': {  # AKM
        'name': 'AKM突击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'AKM 烽火跑刀套',
                    'desc': '低成本高火力',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'},
                        {'slot': '枪口', 'name': '消音器（蓝）', 'cost': '0.8万'}
                    ],
                    'total': '1.3万',
                    'tip': '适合跑刀，7.62伤害高'
                },
                'standard': {
                    'title': 'AKM 烽火小康套',
                    'desc': '火力与性价比平衡',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'},
                        {'slot': '握把', 'name': '垂直握把', 'cost': '0.5万'}
                    ],
                    'total': '5.8万',
                    'tip': '中距离对枪优势'
                },
                'full': {
                    'title': 'AKM 烽火满改套',
                    'desc': '极致火力',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'},
                        {'slot': '枪口', 'name': '专属消音器', 'cost': '8万'},
                        {'slot': '握把', 'name': '人体工学握把', 'cost': '2万'},
                        {'slot': '枪托', 'name': 'AK枪托', 'cost': '3万'}
                    ],
                    'total': '18万',
                    'tip': '全自动火力压制'
                }
            },
            'battle': {
                'standard': {
                    'title': 'AKM 战场套',
                    'desc': '高伤害',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '适合抢点，7.62子弹伤害高'
                }
            },
            'ranked': {
                'standard': {
                    'title': 'AKM 排位套',
                    'desc': '稳定性优先',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'},
                        {'slot': '握把', 'name': '垂直握把', 'cost': '0.5万'}
                    ],
                    'total': '5.8万',
                    'tip': '排位赛稳定输出'
                }
            }
        }
    },
    '18020000001': {  # MP5
        'name': 'MP5冲锋枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'MP5 烽火跑刀套',
                    'desc': '低成本高射速',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'},
                        {'slot': '枪口', 'name': '消音器（蓝）', 'cost': '0.8万'}
                    ],
                    'total': '1.3万',
                    'tip': '适合跑刀，射速高'
                },
                'standard': {
                    'title': 'MP5 烽火小康套',
                    'desc': '全能型',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '中近距离全能'
                }
            },
            'battle': {
                'standard': {
                    'title': 'MP5 战场套',
                    'desc': '高射速',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '适合室内近战'
                }
            }
        }
    },
    '18020000002': {  # P90
        'name': 'P90冲锋枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'P90 烽火跑刀套',
                    'desc': '大弹容',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '50发弹容，适合跑刀'
                },
                'standard': {
                    'title': 'P90 烽火小康套',
                    'desc': '大弹容高射速',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '50发弹容持续火力'
                }
            },
            'battle': {
                'standard': {
                    'title': 'P90 战场套',
                    'desc': '持续火力',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '50发弹容压制'
                }
            }
        }
    },
    '18020000003': {  # Vector
        'name': 'Vector冲锋枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'Vector 烽火跑刀套',
                    'desc': '超高射速',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '射速1200，近战无敌'
                },
                'standard': {
                    'title': 'Vector 烽火小康套',
                    'desc': '近战特化',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '4万',
                    'tip': '室内近战最强'
                }
            },
            'battle': {
                'standard': {
                    'title': 'Vector 战场套',
                    'desc': '近战爆发',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '适合室内CQB'
                }
            }
        }
    },
    '18050000003': {  # VSS
        'name': 'VSS射手步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'VSS 烽火隐蔽套',
                    'desc': '消音狙击',
                    'parts': [
                        {'slot': '瞄准镜', 'name': 'PSO-1瞄准镜', 'cost': '1.5万'}
                    ],
                    'total': '1.5万',
                    'tip': '自带消音，隐蔽狙击'
                },
                'standard': {
                    'title': 'VSS 烽火狙击套',
                    'desc': '中距离狙击',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'},
                        {'slot': '握把', 'name': '垂直握把', 'cost': '0.5万'}
                    ],
                    'total': '5.5万',
                    'tip': '9x39mm亚音速，隐蔽击杀'
                }
            },
            'battle': {
                'standard': {
                    'title': 'VSS 战场套',
                    'desc': '远距离',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'}
                    ],
                    'total': '5万',
                    'tip': '适合远程支援'
                }
            }
        }
    },
    '18060000008': {  # R93
        'name': 'R93狙击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'R93 烽火入门套',
                    'desc': '大口径狙击',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'}
                    ],
                    'total': '5万',
                    'tip': '.338子弹一枪致死'
                },
                'standard': {
                    'title': 'R93 烽火满配套',
                    'desc': '极致精度',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'},
                        {'slot': '枪托', 'name': '狙击枪托', 'cost': '2万'}
                    ],
                    'total': '10.5万',
                    'tip': '一枪致死，狙击之王'
                }
            },
            'battle': {
                'standard': {
                    'title': 'R93 战场套',
                    'desc': '远程击杀',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'}
                    ],
                    'total': '5万',
                    'tip': '适合远程支援'
                }
            }
        }
    },
    '18030000004': {  # M870
        'name': 'M870霰弹枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'M870 烽火喷子套',
                    'desc': '近战爆发',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '霰弹枪一枪秒杀'
                },
                'standard': {
                    'title': 'M870 烽火满配套',
                    'desc': '近战特化',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '4万',
                    'tip': '室内近战无敌'
                }
            },
            'battle': {
                'standard': {
                    'title': 'M870 战场套',
                    'desc': '近战爆发',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '适合室内近战'
                }
            }
        }
    },
    '18040000001': {  # PKM
        'name': 'PKM通用机枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'PKM 烽火压制套',
                    'desc': '大弹容压制',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '100发弹链，持续压制'
                },
                'standard': {
                    'title': 'PKM 烽火满配套',
                    'desc': '火力压制',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '绝密地图标配'
                }
            },
            'battle': {
                'standard': {
                    'title': 'PKM 战场套',
                    'desc': '火力压制',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '适合火力压制'
                }
            }
        }
    },
    '18040000002': {  # M249
        'name': 'M249轻机枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'M249 烽火压制套',
                    'desc': '超大弹容',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '200发弹链，持续火力'
                },
                'standard': {
                    'title': 'M249 烽火满配套',
                    'desc': '火力压制',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '200发弹容，移动弹药库'
                }
            },
            'battle': {
                'standard': {
                    'title': 'M249 战场套',
                    'desc': '火力压制',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '适合火力压制'
                }
            }
        }
    },
    '18010000031': {  # CAR-15
        'name': 'CAR-15突击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'CAR-15 烽火跑刀套',
                    'desc': '低成本高效率',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'},
                        {'slot': '枪口', 'name': '消音器（蓝）', 'cost': '0.8万'}
                    ],
                    'total': '1.3万',
                    'tip': '适合跑刀'
                },
                'standard': {
                    'title': 'CAR-15 烽火小康套',
                    'desc': '全能型',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '中距离全能'
                }
            },
            'battle': {
                'standard': {
                    'title': 'CAR-15 战场套',
                    'desc': '高射速',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '适合抢点'
                }
            }
        }
    },
    '18010000013': {  # K416
        'name': 'K416突击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'K416 烽火跑刀套',
                    'desc': '高射速高可控',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'},
                        {'slot': '枪口', 'name': '消音器（蓝）', 'cost': '0.8万'}
                    ],
                    'total': '1.3万',
                    'tip': '适合跑刀，射速880'
                },
                'standard': {
                    'title': 'K416 烽火小康套',
                    'desc': '极致可控性',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'},
                        {'slot': '握把', 'name': '垂直握把', 'cost': '0.5万'}
                    ],
                    'total': '5.8万',
                    'tip': '可控性61，后座44'
                }
            },
            'battle': {
                'standard': {
                    'title': 'K416 战场套',
                    'desc': '高可控',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '适合抢点，可控性高'
                }
            }
        }
    },
    '18010000015': {  # AUG
        'name': 'AUG突击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'AUG 烽火跑刀套',
                    'desc': '稳定无托',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '无托设计，稳定高'
                },
                'standard': {
                    'title': 'AUG 烽火小康套',
                    'desc': '稳定精准',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '稳定59，中远距离强'
                }
            },
            'battle': {
                'standard': {
                    'title': 'AUG 战场套',
                    'desc': '稳定输出',
                    'parts': [
                        {'slot': '枪口', 'name': '冲锋枪抑径器', 'cost': '2万'},
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.8万'}
                    ],
                    'total': '2.8万',
                    'tip': '适合中距离对枪'
                }
            }
        }
    },
    '18020000008': {  # SR-3M
        'name': 'SR-3M紧凑突击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'SR-3M 烽火隐蔽套',
                    'desc': '9x39mm亚音速',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '9x39mm，隐蔽击杀'
                },
                'standard': {
                    'title': 'SR-3M 烽火套',
                    'desc': '隐蔽近战',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '全息瞄准镜', 'cost': '1.8万'},
                        {'slot': '枪口', 'name': '消音器（紫）', 'cost': '3.5万'}
                    ],
                    'total': '5.3万',
                    'tip': '9x39mm，近战隐蔽'
                }
            },
            'battle': {
                'standard': {
                    'title': 'SR-3M 战场套',
                    'desc': '隐蔽近战',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '适合室内CQB'
                }
            }
        }
    },
    '18010000037': {  # AS Val
        'name': 'AS Val突击步枪',
        'icon': '🔫',
        'builds': {
            'raid': {
                'budget': {
                    'title': 'AS Val 烽火隐蔽套',
                    'desc': '自带消音',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点瞄准镜', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '自带消音，9x39mm'
                },
                'standard': {
                    'title': 'AS Val 烽火套',
                    'desc': '隐蔽狙击',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '高倍瞄准镜', 'cost': '5万'},
                        {'slot': '握把', 'name': '垂直握把', 'cost': '0.5万'}
                    ],
                    'total': '5.5万',
                    'tip': '9x39mm亚音速，隐蔽击杀'
                }
            },
            'battle': {
                'standard': {
                    'title': 'AS Val 战场套',
                    'desc': '隐蔽输出',
                    'parts': [
                        {'slot': '瞄准镜', 'name': '红点', 'cost': '0.5万'}
                    ],
                    'total': '0.5万',
                    'tip': '适合隐蔽作战'
                }
            }
        }
    }
}

# Merge with existing mods
if 'mods' not in d:
    d['mods'] = {}
d['mods'].update(new_mods)

# Save
with open('data/game-data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f'✅ 已添加 {len(new_mods)} 把武器的mods配置')
print('当前mods总数:', len(d['mods']))
