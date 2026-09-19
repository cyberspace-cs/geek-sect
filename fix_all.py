p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 修复 showPage 函数，确保底部导航正确
old_show = '''function showPage(page, tabEl) {
  document.querySelectorAll('[id^="page-"]').forEach(p => p.style.display = 'none');
  document.getElementById('page-' + page).style.display = 'block';
  document.querySelectorAll('.tab-item').forEach(t => t.classList.remove('active'));
  if (tabEl) tabEl.classList.add('active');
  if (page === 'wrong') loadWrong();
  if (page === 'rank') loadRank();'''

new_show = '''function showPage(page, tabEl) {
  document.querySelectorAll('[id^="page-"]').forEach(p => p.style.display = 'none');
  document.getElementById('page-' + page).style.display = 'block';
  document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active'));
  if (tabEl) tabEl.classList.add('active');
  if (page === 'wrong') loadWrong();
  if (page === 'rank') loadRank();'''

c = c.replace(old_show, new_show)

# 确保 renderCats 在页面加载完成后执行
old_init = '''renderHome();
renderCats();
checkDailyStatus();
checkGithubBinding();'''

new_init = '''renderHome();
renderCats();
checkDailyStatus();
checkGithubBinding();
console.log('极客宗初始化完成！分类数:', CATS.length);'''

c = c.replace(old_init, new_init)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed: navigation and render functions')
print(f'New length: {len(c)} chars')
