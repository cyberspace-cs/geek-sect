p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 修复 CATS 数组，加上算法和系统设计
old_cats = '''const CATS = [
  { key: '考研', name: '考研', emoji: '🎓', desc: '数学·英语·政治·专业课', color: '#3b82f6' },
  { key: '考公', name: '考公', emoji: '🏛️', desc: '行测·申论·常识判断', color: '#10b981' },
  { key: '大厂', name: '大厂', emoji: '💻', desc: '算法·系统·前端·后端', color: '#8b5cf6' }
];'''

new_cats = '''const CATS = [
  { key: '考研', name: '考研', emoji: '🎓', desc: '数学·英语·政治·专业课', color: '#3b82f6' },
  { key: '考公', name: '考公', emoji: '🏛️', desc: '行测·申论·常识判断', color: '#10b981' },
  { key: '大厂', name: '大厂', emoji: '💻', desc: '算法·系统·前端·后端', color: '#8b5cf6' },
  { key: 'leetcode', name: '算法', emoji: '⚔️', desc: 'LeetCode 高频题详解', color: '#00ff88' },
  { key: 'sys_design', name: '系统设计', emoji: '🏗️', desc: '高并发·微服务·分布式', color: '#00ccff' }
];'''

c = c.replace(old_cats, new_cats)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed: added leetcode and sys_design to CATS array')
print(f'New length: {len(c)} chars')
