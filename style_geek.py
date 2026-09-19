p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 配色替换：浅色系 -> 极客宗赛博风
color_replacements = [
    ('#3b5bdb', '#00ff88'),  # 主蓝 -> 荧光绿
    ('#5c7cfa', '#00ccff'),  # 浅蓝 -> 赛博青
    ('#eaf0ff', 'rgba(0,255,136,.1)'),  # 浅蓝背景 -> 半透明绿
    ('#0ca678', '#00ff88'),  # 青绿 -> 荧光绿
    ('#e3faf3', 'rgba(0,255,136,.1)'),  # 浅青绿背景 -> 半透明绿
    ('#f08c00', '#ffb84d'),  # 橙色 -> 警告黄
    ('#fff4e0', 'rgba(255,184,77,.1)'),  # 浅橙背景 -> 半透明黄
    ('#1a2340', '#e8e8f0'),  # 深色文字 -> 亮白
    ('#4a5578', '#b0b0c0'),  # 次要文字 -> 浅灰
    ('#8a94b0', '#666680'),  # 辅助文字 -> 暗灰
    ('#e8ecf5', 'rgba(255,255,255,.08)'),  # 浅边框 -> 半透明白
    ('#f5f7fb', '#0a0a12'),  # 背景色 -> 极夜黑
    ('#ffffff', '#12121e'),  # 卡片白色 -> 深空蓝黑
    ('#fff', '#12121e'),  # 卡片白色缩写
]

for old, new in color_replacements:
    c = c.replace(old, new)

# 文案替换
text_replacements = [
    ('墨先生', '码道人'),
    ('墨院', '极客宗'),
    ('心魔录', 'Bug录'),
    ('心魔', 'Bug'),
    ('墨教练', '码道人'),
    ('墨一', '长红'),
    ('墨二', '长青'),
    ('墨三', '长白'),
    ('墨四', '长玄'),
]

for old, new in text_replacements:
    c = c.replace(old, new)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Style and text replaced successfully')
print(f'New length: {len(c)} chars')
