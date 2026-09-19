content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>极客宗 · 修炼系统</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  :root {
    --bg: #0a0a12;
    --surface: #12121e;
    --surface-2: #1a1a2e;
    --line: rgba(255,255,255,.08);
    --brand: #00ff88;
    --brand-2: #00ccff;
    --danger: #ff6b6b;
    --warning: #ffb84d;
    --ink: #e8e8f0;
    --ink-2: #b0b0c0;
    --ink-3: #666680;
  }
  body {
    background: var(--bg);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    line-height: 1.6;
    min-height: 100vh;
  }
  .container { max-width: 480px; margin: 0 auto; padding: 0 16px 80px; }
  .header {
    padding: 24px 0;
    text-align: center;
    border-bottom: 1px solid var(--line);
    margin-bottom: 24px;
  }
  .header h1 {
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--brand), var(--brand-2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .header p { color: var(--ink-3); font-size: 14px; margin-top: 4px; }
  .coach-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
    display: flex;
    gap: 16px;
    align-items: center;
  }
  .coach-avatar {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--brand), var(--brand-2));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    flex-shrink: 0;
    box-shadow: 0 0 20px rgba(0,255,136,.3);
  }
  .coach-info { flex: 1; }
  .coach-name { font-size: 18px; font-weight: 700; color: var(--brand); }
  .coach-title { font-size: 12px; color: var(--ink-3); }
  .coach-line { font-size: 14px; color: var(--ink-2); margin-top: 6px; font-style: italic; }
  .realm-card {
    background: rgba(0,255,136,.05);
    border: 1px solid rgba(0,255,136,.2);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
  }
  .realm-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
  }
  .realm-badge {
    font-size: 16px;
    font-weight: 700;
    padding: 4px 16px;
    border: 1px solid var(--brand);
    border-radius: 999px;
    color: var(--brand);
    background: rgba(0,255,136,.1);
  }
  .realm-exp { font-size: 14px; color: var(--ink-2); }
  .exp-bar {
    height: 8px;
    background: rgba(255,255,255,.08);
    border-radius: 999px;
    overflow: hidden;
    margin-bottom: 10px;
  }
  .exp-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--brand), var(--brand-2));
    border-radius: 999px;
    box-shadow: 0 0 10px rgba(0,255,136,.5);
    transition: width .6s ease;
  }
  .realm-desc { font-size: 12px; color: var(--ink-3); }
  .stats-row {
    display: flex;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 16px 0;
    margin-bottom: 24px;
  }
  .stat-item { flex: 1; text-align: center; }
  .stat-num { font-size: 24px; font-weight: 800; color: var(--brand); }
  .stat-label { font-size: 12px; color: var(--ink-3); margin-top: 2px; }
  .stat-divider { width: 1px; background: var(--line); }
  .section-title {
    font-size: 16px;
    font-weight: 700;
    margin: 0 0 16px;
    padding-left: 12px;
    border-left: 3px solid var(--brand);
  }
  .cat-list { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
  .cat-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    cursor: pointer;
    transition: all .2s;
  }
  .cat-card:hover { border-color: rgba(0,255,136,.4); transform: translateY(-2px); }
  .cat-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
  }
  .cat-meta { flex: 1; }
  .cat-name { font-size: 16px; font-weight: 700; }
  .cat-desc { font-size: 12px; color: var(--ink-3); margin-top: 2px; }
  .cat-count { font-size: 14px; font-weight: 600; color: var(--brand); }
  .feature-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 24px;
  }
  .feature-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 20px;
    cursor: pointer;
    transition: all .2s;
    text-align: center;
  }
  .feature-card:hover { border-color: rgba(0,255,136,.4); }
  .feature-icon { font-size: 32px; margin-bottom: 8px; }
  .feature-title { font-size: 14px; font-weight: 700; }
  .feature-desc { font-size: 11px; color: var(--ink-3); margin-top: 4px; }
  .quiz-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .quiz-progress { font-size: 14px; color: var(--ink-2); }
  .quiz-bar {
    height: 4px;
    background: rgba(255,255,255,.08);
    border-radius: 999px;
    overflow: hidden;
    margin-bottom: 20px;
  }
  .quiz-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--brand), var(--brand-2));
    transition: width .3s ease;
  }
  .question-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
  }
  .question-meta {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }
  .tag {
    font-size: 11px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 999px;
  }
  .tag-cat { background: rgba(0,204,255,.15); color: var(--brand-2); }
  .tag-diff { background: rgba(255,184,77,.15); color: var(--warning); }
  .tag-type { background: rgba(255,255,255,.08); color: var(--ink-2); }
  .question-stem { font-size: 16px; line-height: 1.8; margin-bottom: 20px; }
  .options { display: flex; flex-direction: column; gap: 10px; }
  .option {
    padding: 14px 16px;
    border: 1px solid var(--line);
    border-radius: 12px;
    cursor: pointer;
    transition: all .2s;
    display: flex;
    gap: 12px;
    align-items: center;
  }
  .option:hover { border-color: rgba(0,255,136,.3); }
  .option.selected { border-color: var(--brand); background: rgba(0,255,136,.1); }
  .option.correct { border-color: var(--brand); background: rgba(0,255,136,.15); }
  .option.wrong { border-color: var(--danger); background: rgba(255,107,107,.15); }
  .option-label {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: var(--surface-2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: 700;
    flex-shrink: 0;
  }
  .option-text { flex: 1; font-size: 14px; }
  .quiz-footer {
    display: flex;
    gap: 12px;
    margin-top: 20px;
  }
  .btn {
    flex: 1;
    padding: 14px;
    border: none;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    transition: all .2s;
  }
  .btn-primary {
    background: linear-gradient(135deg, var(--brand), var(--brand-2));
    color: #0a0a12;
  }
  .btn-primary:disabled { opacity: .5; cursor: not-allowed; }
  .btn-ghost {
    background: transparent;
    color: var(--ink);
    border: 1px solid var(--line);
  }
  .explain-box {
    margin-top: 16px;
    padding: 16px;
    background: rgba(0,255,136,.05);
    border-left: 3px solid var(--brand);
    border-radius: 8px;
    font-size: 14px;
    color: var(--ink-2);
    line-height: 1.8;
  }
  .wrong-list { display: flex; flex-direction: column; gap: 12px; }
  .wrong-item {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 16px;
  }
  .wrong-stem { font-size: 14px; margin-bottom: 8px; line-height: 1.6; }
  .wrong-meta { font-size: 12px; color: var(--ink-3); }
  .chat-messages {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 80px;
  }
  .msg {
    max-width: 85%;
    padding: 12px 16px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.6;
  }
  .msg-user {
    align-self: flex-end;
    background: linear-gradient(135deg, var(--brand), var(--brand-2));
    color: #0a0a12;
    border-bottom-right-radius: 4px;
  }
  .msg-bot {
    align-self: flex-start;
    background: var(--surface);
    border: 1px solid var(--line);
    border-bottom-left-radius: 4px;
  }
  .chat-input-bar {
    position: fixed;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 480px;
    padding: 12px 16px;
    background: var(--bg);
    border-top: 1px solid var(--line);
    display: flex;
    gap: 8px;
  }
  .chat-input {
    flex: 1;
    padding: 10px 16px;
    border: 1px solid var(--line);
    border-radius: 24px;
    background: var(--surface);
    color: var(--ink);
    font-size: 14px;
    outline: none;
  }
  .chat-send {
    width: 44px;
    height: 44px;
    border: none;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--brand), var(--brand-2));
    color: #0a0a12;
    font-weight: 700;
    cursor: pointer;
  }
  .tab-bar {
    position: fixed;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 480px;
    display: flex;
    background: var(--bg);
    border-top: 1px solid var(--line);
    padding: 8px 0;
  }
  .tab-item {
    flex: 1;
    text-align: center;
    padding: 6px 0;
    cursor: pointer;
    color: var(--ink-3);
    font-size: 11px;
  }
  .tab-item.active { color: var(--brand); }
  .tab-icon { font-size: 20px; margin-bottom: 2px; }
  .toast {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: var(--surface-2);
    padding: 12px 24px;
    border-radius: 12px;
    border: 1px solid var(--line);
    z-index: 999;
    font-size: 14px;
  }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>⚡ 极客宗</h1>
    <p>勤耕不辍 · 天道酬勤</p>
  </div>

  <div id="page-home">
    <div class="coach-card">
      <div class="coach-avatar">👨‍💻</div>
      <div class="coach-info">
        <div class="coach-name">码道人 <span class="coach-title">· 宗主</span></div>
        <div class="coach-line" id="coach-line">"来了？今天的 LeetCode 刷了吗？"</div>
      </div>
    </div>
    <div class="realm-card">
      <div class="realm-top">
        <div class="realm-badge" id="realm-badge">筑基</div>
        <div class="realm-exp" id="realm-exp">修为 0</div>
      </div>
      <div class="exp-bar">
        <div class="exp-fill" id="exp-fill" style="width: 0%"></div>
      </div>
      <div class="realm-desc" id="realm-desc">初入极客宗，Hello World 入门</div>
    </div>
    <div class="stats-row">
      <div class="stat-item">
        <div class="stat-num" id="stat-streak">0</div>
        <div class="stat-label">连续Commit</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-num" id="stat-today">0</div>
        <div class="stat-label">今日提交</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-num" id="stat-wrong">0</div>
        <div class="stat-label">Bug待除</div>
      </div>
    </div>
    <div class="section-title">选择修炼区域</div>
    <div class="cat-list" id="cat-list"></div>
    <div class="section-title">进阶修炼</div>
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
    </div>
  </div>

  <div id="page-quiz" style="display:none">
    <div class="quiz-header">
      <div class="quiz-progress" id="quiz-progress">第 1 / 30 题</div>
      <button class="btn btn-ghost" style="flex:0;padding:8px 16px;font-size:13px" onclick="showPage('home', null)">返回</button>
    </div>
    <div class="quiz-bar">
      <div class="quiz-bar-fill" id="quiz-bar-fill" style="width: 0%"></div>
    </div>
    <div class="question-card">
      <div class="question-meta" id="question-meta"></div>
      <div class="question-stem" id="question-stem"></div>
      <div class="options" id="options"></div>
      <div class="explain-box" id="explain-box" style="display:none"></div>
    </div>
    <div class="quiz-footer">
      <button class="btn btn-ghost" id="btn-prev" onclick="prevQuestion()">上一题</button>
      <button class="btn btn-primary" id="btn-submit" onclick="submitAnswer()">提交答案</button>
      <button class="btn btn-primary" id="btn-next" onclick="nextQuestion()" style="display:none">下一题</button>
    </div>
  </div>

  <div id="page-wrong" style="display:none">
    <div class="section-title">Bug录 · 待修复</div>
    <div class="wrong-list" id="wrong-list"></div>
  </div>

  <div id="page-chat" style="display:none">
    <div class="section-title">请教宗主 · 码道人</div>
    <div class="chat-messages" id="chat-messages"></div>
    <div class="chat-input-bar">
      <input type="text" class="chat-input" id="chat-input" placeholder="输入你的问题..." onkeydown="if(event.key==='Enter')sendChat()">
      <button class="chat-send" onclick="sendChat()">↑</button>
    </div>
  </div>

  <div id="page-rank" style="display:none">
    <div class="section-title">论道堂 · 排行榜</div>
    <div class="cat-list" id="rank-list"></div>
  </div>
</div>

<div class="tab-bar">
  <div class="tab-item active" onclick="showPage('home', this)">
    <div class="tab-icon">🏠</div>
    首页
  </div>
  <div class="tab-item" onclick="showPage('wrong', this)">
    <div class="tab-icon">🐛</div>
    Bug录
  </div>
  <div class="tab-item" onclick="showPage('chat', this)">
    <div class="tab-icon">💬</div>
    宗主
  </div>
  <div class="tab-item" onclick="showPage('rank', this)">
    <div class="tab-icon">🏆</div>
    论道
  </div>
</div>

<script>
const API = '';
let userId = localStorage.getItem('geek_uid') || 'demo_' + Date.now().toString(36);
let exp = parseInt(localStorage.getItem('geek_exp') || '0');
let streak = parseInt(localStorage.getItem('geek_streak') || '0');
let currentQuestions = [];
let currentQIndex = 0;
let selectedOptions = [];
let answered = false;

const REALMS = [
  { min: 0, name: '筑基', desc: '初入极客宗，Hello World 入门', color: '#94a3b8' },
  { min: 50, name: '金丹', desc: '略通语法，可解简单算法题', color: '#22c55e' },
  { min: 150, name: '元婴', desc: '算法贯通，小有所成', color: '#3b82f6' },
  { min: 300, name: '化神', desc: '才学兼备，可任 Tech Lead', color: '#a855f7' },
  { min: 500, name: '渡劫', desc: '架构大师，大厂架构师水平', color: '#f59e0b' },
  { min: 800, name: '飞升', desc: '学究天人，一代 CTO', color: '#ef4444' }
];

const CATS = [
  { key: '考研', name: '考研', emoji: '🎓', desc: '数学·英语·政治·专业课', color: '#3b82f6' },
  { key: '考公', name: '考公', emoji: '🏛️', desc: '行测·申论·常识判断', color: '#10b981' },
  { key: '大厂', name: '大厂', emoji: '💻', desc: '算法·系统·前端·后端', color: '#8b5cf6' }
];

const GREETINGS = [
  '来了？今天的 LeetCode 刷了吗？',
  '别磨蹭，编译不等人。',
  '又来偷懒？昨天的 bug 复盘了？',
  '嗯，今日提交记录尚可，可一战。',
  '既入极客宗，便没有半途而废的道理。'
];

function getCurrentRealm() {
  let cur = REALMS[0];
  for (const r of REALMS) if (exp >= r.min) cur = r;
  return cur;
}

function renderHome() {
  const realm = getCurrentRealm();
  document.getElementById('realm-badge').textContent = realm.name;
  document.getElementById('realm-exp').textContent = '修为 ' + exp;
  document.getElementById('realm-desc').textContent = realm.desc;
  document.getElementById('stat-streak').textContent = streak;
  document.getElementById('stat-today').textContent = getTodayCount();
  document.getElementById('coach-line').textContent = '"' + GREETINGS[Math.floor(Math.random() * GREETINGS.length)] + '"';
  const nextRealm = REALMS.find(r => r.min > exp);
  if (nextRealm) {
    const curIdx = REALMS.indexOf(realm);
    const range = nextRealm.min - REALMS[curIdx].min;
    const done = exp - REALMS[curIdx].min;
    document.getElementById('exp-fill').style.width = Math.min(100, done / range * 100) + '%';
  } else {
    document.getElementById('exp-fill').style.width = '100%';
  }
}

function getTodayCount() {
  const key = 'geek_done_' + new Date().toISOString().slice(0,10);
  return localStorage.getItem(key) || 0;
}

function addTodayCount(n) {
  const key = 'geek_done_' + new Date().toISOString().slice(0,10);
  localStorage.setItem(key, parseInt(localStorage.getItem(key) || '0') + n);
}

function renderCats() {
  document.getElementById('cat-list').innerHTML = CATS.map(c => `
    <div class="cat-card" onclick="startQuiz('${c.key}')">
      <div class="cat-icon" style="background:${c.color}22">${c.emoji}</div>
      <div class="cat-meta">
        <div class="cat-name">${c.name}历练</div>
        <div class="cat-desc">${c.desc}</div>
      </div>
      <div class="cat-count">→</div>
    </div>
  `).join('');
}

function showPage(page, tabEl) {
  document.querySelectorAll('[id^="page-"]').forEach(p => p.style.display = 'none');
  document.getElementById('page-' + page).style.display = 'block';
  document.querySelectorAll('.tab-item').forEach(t => t.classList.remove('active'));
  if (tabEl) tabEl.classList.add('active');
  if (page === 'wrong') loadWrong();
  if (page === 'rank') loadRank();
  if (page === 'home') renderHome();
}

function parseQuestion(q) {
  return {
    ...q,
    opts: typeof q.opts === 'string' ? JSON.parse(q.opts) : q.opts,
    answer: typeof q.answer === 'string' ? JSON.parse(q.answer) : q.answer
  };
}

async function startQuiz(cat) {
  showPage('quiz', null);
  try {
    const res = await fetch(API + '/api/questions/sample?cat=' + encodeURIComponent(cat) + '&limit=30');
    const data = await res.json();
    currentQuestions = data.map(parseQuestion);
    currentQIndex = 0;
    renderQuestion();
  } catch (e) {
    alert('加载失败: ' + e.message);
    showPage('home', null);
  }
}

function renderQuestion() {
  const q = currentQuestions[currentQIndex];
  if (!q) return;
  answered = false;
  selectedOptions = new Array(q.opts.length).fill(false);
  document.getElementById('quiz-progress').textContent = `第 ${currentQIndex + 1} / ${currentQuestions.length} 题`;
  document.getElementById('quiz-bar-fill').style.width = ((currentQIndex + 1) / currentQuestions.length * 100) + '%';
  document.getElementById('btn-prev').disabled = currentQIndex === 0;
  document.getElementById('btn-prev').style.opacity = currentQIndex === 0 ? 0.5 : 1;
  document.getElementById('btn-submit').style.display = 'block';
  document.getElementById('btn-next').style.display = 'none';
  const diffMap = { easy: '简单', medium: '中等', hard: '困难' };
  document.getElementById('question-meta').innerHTML = `
    <span class="tag tag-cat">${q.cat}</span>
    <span class="tag tag-diff">${diffMap[q.difficulty] || q.difficulty}</span>
    <span class="tag tag-type">${q.type}</span>
  `;
  document.getElementById('question-stem').textContent = q.stem;
  document.getElementById('explain-box').style.display = 'none';
  document.getElementById('options').innerHTML = q.opts.map((opt, i) => `
    <div class="option" data-i="${i}" onclick="selectOption(${i})">
      <div class="option-label">${String.fromCharCode(65 + i)}</div>
      <div class="option-text">${opt}</div>
    </div>
  `).join('');
}

function selectOption(i) {
  if (answered) return;
  const q = currentQuestions[currentQIndex];
  if (q.type === '多选题') {
    selectedOptions[i] = !selectedOptions[i];
  } else {
    selectedOptions = selectedOptions.map((_, idx) => idx === i);
  }
  document.querySelectorAll('.option').forEach((el, idx) => {
    el.classList.toggle('selected', selectedOptions[idx]);
  });
}

function submitAnswer() {
  if (answered) return;
  const q = currentQuestions[currentQIndex];
  const picked = selectedOptions.map((s, i) => s ? i : -1).filter(i => i >= 0).sort();
  const ans = q.answer.slice().sort();
  const correct = JSON.stringify(picked) === JSON.stringify(ans);
  answered = true;
  document.querySelectorAll('.option').forEach((el, idx) => {
    el.classList.remove('selected');
    if (q.answer.includes(idx)) el.classList.add('correct');
    else if (selectedOptions[idx]) el.classList.add('wrong');
  });
  document.getElementById('explain-box').style.display = 'block';
  document.getElementById('explain-box').innerHTML = `<strong style="color:var(--brand)">💡 解析：</strong>${q.explain}`;
  if (correct) {
    exp += 10;
    localStorage.setItem('geek_exp', exp);
    showToast('✓ 正确！+10 修为');
  } else {
    showToast('✗ 错误，已加入Bug录');
    fetch(API + '/api/wrong-book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, question_id: q.id })
    }).catch(() => {});
  }
  addTodayCount(1);
  renderHome();
  document.getElementById('btn-submit').style.display = 'none';
  document.getElementById('btn-next').style.display = 'block';
}

function prevQuestion() {
  if (currentQIndex > 0) {
    currentQIndex--;
    renderQuestion();
  }
}

function nextQuestion() {
  if (currentQIndex < currentQuestions.length - 1) {
    currentQIndex++;
    renderQuestion();
  } else {
    showToast('本轮完成！');
    showPage('home', null);
  }
}

async function loadWrong() {
  try {
    const res = await fetch(API + '/api/wrong-book/' + userId);
    const data = await res.json();
    const list = document.getElementById('wrong-list');
    if (!data.length) {
      list.innerHTML = '<div style="text-align:center;color:var(--ink-3);padding:40px">暂无Bug记录，继续保持！</div>';
      return;
    }
    list.innerHTML = data.map(w => `
      <div class="wrong-item">
        <div class="wrong-stem">${w.question?.stem || '错题'}</div>
        <div class="wrong-meta">${w.question?.cat || ''} · ${w.question?.topic || ''}</div>
      </div>
    `).join('');
  } catch (e) {
    document.getElementById('wrong-list').innerHTML = '<div style="color:var(--danger)">加载失败</div>';
  }
}

async function sendChat() {
  const input = document.getElementById('chat-input');
  const text = input.value.trim();
  if (!text) return;
  input.value = '';
  const messages = document.getElementById('chat-messages');
  messages.innerHTML += `<div class="msg msg-user">${text}</div>`;
  messages.scrollTop = messages.scrollHeight;
  try {
    const res = await fetch(API + '/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        system: '你是极客宗宗主码道人，毒舌但护短的AI导师。用程序员黑话风格回答问题。',
        messages: [{ role: 'user', content: text }]
      })
    });
    const data = await res.json();
    messages.innerHTML += `<div class="msg msg-bot">${data.reply || '暂无回复'}</div>`;
    messages.scrollTop = messages.scrollHeight;
  } catch (e) {
    messages.innerHTML += `<div class="msg msg-bot">网络开小差了...</div>`;
  }
}

function loadRank() {
  const rankData = [
    { rank: 1, name: 'Bug终结者', realm: '飞升', exp: 980, avatar: '👑' },
    { rank: 2, name: '代码诗人', realm: '渡劫', exp: 760, avatar: '🎨' },
    { rank: 3, name: '算法狂魔', realm: '渡劫', exp: 680, avatar: '⚡' },
    { rank: 4, name: '架构大师', realm: '化神', exp: 520, avatar: '🏗️' },
    { rank: 5, name: '你', realm: '筑基', exp: exp, avatar: '🧑‍💻', isSelf: true },
    { rank: 6, name: 'CR战神', realm: '金丹', exp: 98, avatar: '🔍' },
  ];
  document.getElementById('rank-list').innerHTML = rankData.map(r => `
    <div class="cat-card" style="${r.isSelf ? 'border-color:var(--brand)' : ''}">
      <div class="cat-icon">${r.avatar}</div>
      <div class="cat-meta">
        <div class="cat-name">${r.name}</div>
        <div class="cat-desc">${r.realm} · 修为 ${r.exp}</div>
      </div>
      <div class="cat-count">#${r.rank}</div>
    </div>
  `).join('');
}

function startExam() {
  alert('宗门大比即将开启！先从简单的刷题开始吧~');
}

function showToast(msg) {
  const t = document.createElement('div');
  t.className = 'toast';
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 1500);
}

renderHome();
renderCats();
</script>
</body>
</html>
'''

with open(r'D:\download\project\TX-budddy\hacker-edition\geek.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('geek.html written successfully')
print(f'Length: {len(content)} chars')
