p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加成就页 CSS
ach_css = '''
  /* 成就页 */
  .ach-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .ach-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    transition: all .2s;
  }
  .ach-card.unlocked {
    border-color: rgba(255,184,77,.4);
    background: rgba(255,184,77,.05);
  }
  .ach-icon { font-size: 36px; margin-bottom: 8px; opacity: .3; }
  .ach-card.unlocked .ach-icon { opacity: 1; }
  .ach-name { font-size: 14px; font-weight: 700; }
  .ach-desc { font-size: 11px; color: var(--ink-3); margin-top: 4px; }
'''

c = c.replace('</style>', ach_css + '</style>')

# 2. 加成就页 HTML
ach_html = '''
  <!-- 成就页 -->
  <div id="page-achievement" style="display:none">
    <div class="section-title">🏅 成就堂 · 里程碑</div>
    <div class="ach-grid" id="ach-list"></div>
  </div>
'''

# 插入到排行榜页之前
rank_start = c.find('<div id="page-rank"')
if rank_start > 0:
    c = c[:rank_start] + ach_html + c[rank_start:]

# 3. 在首页功能网格加"成就堂"入口
old_feat = '''      <div class="feature-card" onclick="showPage('report', this)">
        <div class="feature-icon">📊</div>
        <div class="feature-title">修炼报告</div>
        <div class="feature-desc">学习数据统计</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">'''

new_feat = '''      <div class="feature-card" onclick="showPage('report', this)">
        <div class="feature-icon">📊</div>
        <div class="feature-title">修炼报告</div>
        <div class="feature-desc">学习数据统计</div>
      </div>
      <div class="feature-card" onclick="showPage('achievement', this)">
        <div class="feature-icon">🏅</div>
        <div class="feature-title">成就堂</div>
        <div class="feature-desc">里程碑徽章</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">'''

c = c.replace(old_feat, new_feat)

# 4. 加成就 JS
ach_js = '''
const ACHIEVEMENTS = [
  { id: 'first_commit', name: 'Hello World', desc: '完成第一次刷题', icon: '🌱', check: () => parseInt(localStorage.getItem('geek_total_done') || '0') >= 1 },
  { id: 'ten_commit', name: '入门者', desc: '累计刷题10道', icon: '📝', check: () => parseInt(localStorage.getItem('geek_total_done') || '0') >= 10 },
  { id: 'hundred_commit', name: '勤奋修炼', desc: '累计刷题100道', icon: '💪', check: () => parseInt(localStorage.getItem('geek_total_done') || '0') >= 100 },
  { id: 'thousand_commit', name: '刷题狂魔', desc: '累计刷题1000道', icon: '🔥', check: () => parseInt(localStorage.getItem('geek_total_done') || '0') >= 1000 },
  { id: 'seven_streak', name: '七日之痒', desc: '连续打卡7天', icon: '📅', check: () => streak >= 7 },
  { id: 'thirty_streak', name: '月度坚持', desc: '连续打卡30天', icon: '⏰', check: () => streak >= 30 },
  { id: 'first_daily', name: '每日一题', desc: '完成第一次每日一题', icon: '✨', check: () => localStorage.getItem('geek_daily_done') === 'true' },
  { id: 'exam_pass', name: '初入宗门', desc: '宗门大比及格', icon: '⚔️', check: () => localStorage.getItem('geek_exam_pass') === 'true' },
  { id: 'first_realm', name: '筑基成功', desc: '达到金丹境界', icon: '⭐', check: () => exp >= 50 },
  { id: 'master_realm', name: '化神大成', desc: '达到化神境界', icon: '👑', check: () => exp >= 300 },
];

function loadAchievements() {
  const unlocked = new Set(JSON.parse(localStorage.getItem('geek_achievements') || '[]'));
  document.getElementById('ach-list').innerHTML = ACHIEVEMENTS.map(ach => {
    const isUnlocked = unlocked.has(ach.id) || ach.check();
    if (isUnlocked && !unlocked.has(ach.id)) {
      unlocked.add(ach.id);
      localStorage.setItem('geek_achievements', JSON.stringify([...unlocked]));
    }
    return `
      <div class="ach-card ${isUnlocked ? 'unlocked' : ''}">
        <div class="ach-icon">${ach.icon}</div>
        <div class="ach-name">${ach.name}</div>
        <div class="ach-desc">${ach.desc}</div>
      </div>
    `;
  }).join('');
}
'''

# 插入到 loadReport 函数之前
c = c.replace('async function loadReport()', ach_js + '\nasync function loadReport()')

# 5. 修改 showPage，加载成就页
old_show = '''  if (page === 'report') loadReport();'''
new_show = '''  if (page === 'report') loadReport();
  if (page === 'achievement') loadAchievements();'''
c = c.replace(old_show, new_show)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added achievements feature')
print(f'New length: {len(c)} chars')
