p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 修改 user_id 生成方式，改成数字
old_uid = "let userId = localStorage.getItem('geek_uid') || 'demo_' + Date.now().toString(36);"
new_uid = "let userId = parseInt(localStorage.getItem('geek_uid') || '0') || Math.floor(Math.random() * 100000) + 1000; localStorage.setItem('geek_uid', userId);"
c = c.replace(old_uid, new_uid)

# 2. 同时加载错题本的时候，用 user_id
old_load = "const res = await fetch(API + '/api/wrong-book/' + userId);"
new_load = "const res = await fetch(API + '/api/wrong-book/' + parseInt(userId));"
c = c.replace(old_load, new_load)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed user_id to be numeric')
print(f'New length: {len(c)} chars')
