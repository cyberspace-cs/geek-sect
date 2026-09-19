p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加学习报告页 CSS
report_css = '''
  /* 学习报告页 */
  .report-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
  }
  .report-title { font-size: 16px; font-weight: 700; margin-bottom: 16px; }
  .progress-bar-bg {
    height: 8px;
    background: rgba(255,255,255,.08);
    border-radius: 999px;
    overflow: hidden;
    margin: 8px 0;
  }
  .progress-bar-fill {
    height: 100%;
    border-radius: 999px;
  }
  .stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .stat-box {
    background: rgba(255,255,255,.03);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
  }
  .stat-box-num { font-size: 24px; font-weight: 800; color: var(--brand); }
  .stat-box-label { font-size: 12px; color: var(--ink-3); margin-top: 4px; }
  .topic-bar { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
  .topic-name { width: 80px; font-size: 13px; color: var(--ink-2); flex-shrink: 0; }
  .topic-bar-bg { flex: 1; height: 8px; background: rgba(255,255,255,.08); border-radius: 999px; overflow: hidden; }
  .topic-bar-fill { height: 100%; background: linear-gradient(90deg, var(--brand), var(--brand-2)); border-radius: 999px; }
  .topic-pct { width: 40px; font-size: 12px; color: var(--ink-3); text-align: right; }
'''

# 插入到 </style> 之前
c = c.replace('</style>', report_css + '</style>')

# 2. 加学习报告页 HTML
report_html = '''
  <!-- 学习报告页 -->
  <div id="page-report" style="display:none">
    <div class="section-title">修炼报告 · 码道人评点</div>

    <div class="report-card">
      <div class="report-title">📊 总览</div>
      <div class="stat-grid">
        <div class="stat-box">
          <div class="stat-box-num" id="report-total">0</div>
          <div class="stat-box-label">累计刷题</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-num" id="report-acc">0%</div>
          <div class="stat-box-label">正确率</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-num" id="report-streak">0</div>
          <div class="stat-box-label">连续天数</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-num" id="report-realm">筑基</div>
          <div class="stat-box-label">当前境界</div>
        </div>
      </div>
    </div>

    <div class="report-card">
      <div class="report-title">🎯 分类掌握度</div>
      <div id="report-cats"></div>
    </div>

    <div class="report-card">
      <div class="report-title">🐛 Bug分布</div>
      <div id="report-wrong-topics"></div>
    </div>

    <div class="report-card">
      <div class="report-title">💪 本周Commit趋势</div>
      <div id="report-weekly"></div>
    </div>
  </div>
'''

# 插入到排行榜页之前
c = c.replace('<!-- 排行榜页 -->', report_html + '\n  <!-- 排行榜页 -->')

# 3. 在首页功能网格加"修炼报告"入口
old_features = '''    <div class="section-title">进阶修炼</div>
    <div class="feature-grid">
      <div class="feature-card" onclick="showPage('wrong', this)">
        <div class="feature-icon">🐛</div>
        <div class="feature-title">Bug录</div>
        <div class="feature-desc">错题复盘</div>
      </div>
      <div class="feature-card" onclick="showPage('chat', this)">
        <div class="feature-icon">💬</div>
        <div class="feature-title">请教宗主</div>
        <div class="feature-desc">AI答疑解惑</div>
      </div>
      <div class="feature-card" onclick="startExam()">
        <div class="feature-icon">⚔️</div>
        <div class="feature-title">宗门大比</div>
        <div class="feature-desc">模拟考试</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">
        <div class="feature-icon">🏆</div>
        <div class="feature-title">论道堂</div>
        <div class="feature-desc">排行榜</div>
      </div>
    </div>'''

new_features = '''    <div class="section-title">进阶修炼</div>
    <div class="feature-grid">
      <div class="feature-card" onclick="showPage('wrong', this)">
        <div class="feature-icon">🐛</div>
        <div class="feature-title">Bug录</div>
        <div class="feature-desc">错题复盘</div>
      </div>
      <div class="feature-card" onclick="showPage('chat', this)">
        <div class="feature-icon">💬</div>
        <div class="feature-title">请教宗主</div>
        <div class="feature-desc">AI答疑解惑</div>
      </div>
      <div class="feature-card" onclick="startExam()">
        <div class="feature-icon">⚔️</div>
        <div class="feature-title">宗门大比</div>
        <div class="feature-desc">模拟考试</div>
      </div>
      <div class="feature-card" onclick="showPage('report', this)">
        <div class="feature-icon">📊</div>
        <div class="feature-title">修炼报告</div>
        <div class="feature-desc">学习数据统计</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">
        <div class="feature-icon">🏆</div>
        <div class="feature-title">论道堂</div>
        <div class="feature-desc">排行榜</div>
      </div>
    </div>'''
c = c.replace(old_features, new_features)

# 4. 加学习报告 JS
report_js = '''
async function loadReport() {
  // 模拟数据（实际应该从后端拿）
  const totalQuestions = parseInt(localStorage.getItem('geek_total_done') || '0');
  const totalCorrect = parseInt(localStorage.getItem('geek_total_correct') || '0');
  const acc = totalQuestions > 0 ? Math.round(totalCorrect / totalQuestions * 100) : 0;

  document.getElementById('report-total').textContent = totalQuestions;
  document.getElementById('report-acc').textContent = acc + '%';
  document.getElementById('report-streak').textContent = streak;
  document.getElementById('report-realm').textContent = getCurrentRealm().name;

  // 分类掌握度（模拟数据，实际从后端错题统计）
  document.getElementById('report-cats').innerHTML = CATS.map((cat, i) => {
    const pct = 60 + Math.floor(Math.random() * 35);
    return `
      <div class="topic-bar">
        <div class="topic-name">${cat.name}</div>
        <div class="topic-bar-bg">
          <div class="topic-bar-fill" style="width: ${pct}%"></div>
        </div>
        <div class="topic-pct">${pct}%</div>
      </div>
    `;
  }).join('');

  // Bug分布
  document.getElementById('report-wrong-topics').innerHTML = `
    <div style="text-align:center;color:var(--ink-3);padding:20px">
      暂无足够数据，继续刷题积累 Bug 记录后可分析
    </div>
  `;

  // 本周Commit趋势
  const days = ['一','二','三','四','五','六','日'];
  const today = new Date().getDay();
  let barsHtml = '';
  for (let i = 6; i >= 0; i--) {
    const d = new Date();
    d.setDate(d.getDate() - i);
    const key = 'geek_done_' + d.toISOString().slice(0,10);
    const count = parseInt(localStorage.getItem(key) || '0');
    const h = Math.min(100, count * 10);
    const dayLabel = i === 0 ? '今天' : '周' + days[d.getDay() === 0 ? 6 : d.getDay() - 1];
    barsHtml += `
      <div style="display:flex;flex-direction:column;align-items:center;flex:1">
        <div style="font-size:10px;color:var(--ink-3);margin-bottom:4px">${count}题</div>
        <div style="width:24px;height:${Math.max(8, h)}px;background:linear-gradient(180deg, var(--brand), var(--brand-2));border-radius:4px 4px 0 0"></div>
        <div style="font-size:10px;color:var(--ink-3);margin-top:4px">${dayLabel}</div>
      </div>
    `;
  }
  document.getElementById('report-weekly').innerHTML = `
    <div style="display:flex;gap:8px;align-items:flex-end;height:100px">${barsHtml}</div>
  `;
}
'''

# 插入到 loadRank 函数之前
c = c.replace('function loadRank()', report_js + '\nfunction loadRank()')

# 5. 修改 showPage，加载报告时调用 loadReport
old_showpage = '''  if (page === 'wrong') loadWrong();
  if (page === 'rank') loadRank();
  if (page === 'home') renderHome();'''
new_showpage = '''  if (page === 'wrong') loadWrong();
  if (page === 'rank') loadRank();
  if (page === 'report') loadReport();
  if (page === 'home') renderHome();'''
c = c.replace(old_showpage, new_showpage)

# 6. 修改 submitAnswer，累计统计
old_submit2 = '''  addTodayCount(1);

  // 每日一题额外奖励'''
new_submit2 = '''  addTodayCount(1);

  // 累计统计
  const totalDone = parseInt(localStorage.getItem('geek_total_done') || '0') + 1;
  localStorage.setItem('geek_total_done', totalDone);
  if (correct) {
    const totalCorrect = parseInt(localStorage.getItem('geek_total_correct') || '0') + 1;
    localStorage.setItem('geek_total_correct', totalCorrect);
  }

  // 每日一题额外奖励'''
c = c.replace(old_submit2, new_submit2)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added study report feature')
print(f'New length: {len(c)} chars')
