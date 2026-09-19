p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 在首页加每日一题卡片
home_addition = '''
    <div class="section-title">今日修炼任务</div>
    <div class="cat-list" style="margin-bottom: 24px;">
      <div class="cat-card" onclick="startDailyQuestion()" style="border-color: var(--warning); background: rgba(255,184,77,.05)">
        <div class="cat-icon" style="background: rgba(255,184,77,.2)">📅</div>
        <div class="cat-meta">
          <div class="cat-name">每日一题</div>
          <div class="cat-desc">每日一题，额外 +20 修为奖励</div>
        </div>
        <div class="cat-count" id="daily-status">未完成</div>
      </div>
    </div>
'''

# 插入到"选择修炼区域"之前
c = c.replace('<div class="section-title">选择修炼区域</div>', home_addition + '<div class="section-title">选择修炼区域</div>')

# 2. 加每日一题相关 JS
daily_js = '''
let dailyDone = localStorage.getItem('geek_daily_' + new Date().toISOString().slice(0,10)) === 'done';

function checkDailyStatus() {
  const today = new Date().toISOString().slice(0,10);
  dailyDone = localStorage.getItem('geek_daily_' + today) === 'done';
  const el = document.getElementById('daily-status');
  if (el) el.textContent = dailyDone ? '✓ 已完成' : '未完成';
}

async function startDailyQuestion() {
  showPage('quiz', null);
  try {
    const res = await fetch(API + '/api/questions/sample?limit=1');
    const data = await res.json();
    currentQuestions = data.map(parseQuestion);
    currentQIndex = 0;
    renderQuestion();
    // 标记是每日一题模式
    window.dailyMode = true;
  } catch (e) {
    alert('加载失败: ' + e.message);
    showPage('home', null);
  }
}
'''

# 插入到 startQuiz 函数之前
c = c.replace('async function startQuiz(cat)', daily_js + '\nasync function startQuiz(cat)')

# 3. 修改 submitAnswer，加每日一题奖励
old_submit = "  addTodayCount(1);\n  renderHome();\n\n  // 切换按钮\n  document.getElementById('btn-submit').style.display = 'none';\n  document.getElementById('btn-next').style.display = 'block';"
new_submit = '''  addTodayCount(1);

  // 每日一题额外奖励
  if (window.dailyMode && correct) {
    exp += 10; // 额外奖励
    localStorage.setItem('geek_exp', exp);
    localStorage.setItem('geek_daily_' + new Date().toISOString().slice(0,10), 'done');
    showToast('+20 修为！每日一题完成奖励');
  }
  window.dailyMode = false;

  renderHome();
  checkDailyStatus();

  // 切换按钮
  document.getElementById('btn-submit').style.display = 'none';
  document.getElementById('btn-next').style.display = 'block';'''
c = c.replace(old_submit, new_submit)

# 4. 初始化时检查每日一题状态
old_init = "renderHome();\nrenderCats();"
new_init = "renderHome();\nrenderCats();\ncheckDailyStatus();"
c = c.replace(old_init, new_init)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Upgraded geek.html with daily question feature')
print(f'New length: {len(c)} chars')
