p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加模考页 CSS
exam_css = '''
  /* 模考页 */
  .exam-setup {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
  }
  .exam-title { font-size: 18px; font-weight: 700; margin-bottom: 16px; }
  .exam-options { display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px; }
  .exam-option {
    padding: 14px 16px;
    border: 1px solid var(--line);
    border-radius: 12px;
    cursor: pointer;
    transition: all .2s;
  }
  .exam-option:hover { border-color: rgba(0,255,136,.3); }
  .exam-option.selected { border-color: var(--brand); background: rgba(0,255,136,.1); }
  .exam-option-name { font-size: 15px; font-weight: 700; }
  .exam-option-desc { font-size: 12px; color: var(--ink-3); margin-top: 2px; }

  .exam-timer {
    position: fixed;
    top: 16px;
    right: 16px;
    background: rgba(255,107,107,.15);
    border: 1px solid var(--danger);
    border-radius: 12px;
    padding: 8px 16px;
    font-size: 16px;
    font-weight: 700;
    color: var(--danger);
    z-index: 100;
  }

  .exam-result-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 32px 24px;
    text-align: center;
    margin-bottom: 20px;
  }
  .result-score { font-size: 56px; font-weight: 800; color: var(--brand); }
  .result-label { font-size: 14px; color: var(--ink-3); margin-bottom: 24px; }
  .result-stats { display: flex; gap: 16px; margin-bottom: 24px; }
  .result-stat { flex: 1; }
  .result-stat-num { font-size: 20px; font-weight: 700; }
  .result-stat-label { font-size: 12px; color: var(--ink-3); }
  .result-grade {
    display: inline-block;
    padding: 6px 20px;
    border-radius: 999px;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 16px;
  }
'''

# 插入到 </style> 之前
c = c.replace('</style>', exam_css + '</style>')

# 2. 加模考设置页和结果页 HTML
exam_html = '''
  <!-- 模考设置页 -->
  <div id="page-exam-setup" style="display:none">
    <div class="section-title">宗门大比 · 选择试卷</div>
    <div class="exam-setup">
      <div class="exam-title">选择试炼类别</div>
      <div class="exam-options" id="exam-cats"></div>
    </div>
    <div class="quiz-footer">
      <button class="btn btn-primary" onclick="startExamNow()">开始试炼</button>
    </div>
  </div>

  <!-- 模考结果页 -->
  <div id="page-exam-result" style="display:none">
    <div class="section-title">试炼结果</div>
    <div class="exam-result-card">
      <div class="result-grade" id="result-grade">甲</div>
      <div class="result-score" id="result-score">85</div>
      <div class="result-label">分 · 正确率</div>
      <div class="result-stats">
        <div class="result-stat">
          <div class="result-stat-num" style="color:var(--brand)" id="result-correct">32</div>
          <div class="result-stat-label">答对</div>
        </div>
        <div class="result-stat">
          <div class="result-stat-num" style="color:var(--danger)" id="result-wrong">8</div>
          <div class="result-stat-label">答错</div>
        </div>
        <div class="result-stat">
          <div class="result-stat-num" style="color:var(--brand-2)" id="result-time">42</div>
          <div class="result-stat-label">用时(分钟)</div>
        </div>
      </div>
      <div style="font-size:14px;color:var(--ink-2)" id="result-comment">宗主点评：尚可，继续修炼！</div>
    </div>
    <div class="quiz-footer">
      <button class="btn btn-ghost" onclick="showPage('home', null)">返回首页</button>
      <button class="btn btn-primary" onclick="reviewWrong()">查看错题</button>
    </div>
  </div>
'''

# 插入到排行榜页之前
c = c.replace('<!-- 排行榜页 -->', exam_html + '\n  <!-- 排行榜页 -->')

# 3. 改 startExam 函数
old_start_exam = "function startExam() {\n  alert('宗门大比即将开启！先从简单的刷题开始吧~');\n}"
new_start_exam = '''let examSelectedCat = null;
let examStartTime = 0;
let examAnswers = [];
let examTimerInterval = null;

function startExam() {
  showPage('exam-setup', null);
  document.getElementById('exam-cats').innerHTML = CATS.map(c => `
    <div class="exam-option" data-cat="${c.key}" onclick="selectExamCat('${c.key}', this)">
      <div class="exam-option-name">${c.emoji} ${c.name}大比</div>
      <div class="exam-option-desc">50题 · 90分钟 · 正确率≥60% 才算合格</div>
    </div>
  `).join('');
}

function selectExamCat(cat, el) {
  examSelectedCat = cat;
  document.querySelectorAll('.exam-option').forEach(o => o.classList.remove('selected'));
  el.classList.add('selected');
}

async function startExamNow() {
  if (!examSelectedCat) {
    alert('请先选择试炼类别！');
    return;
  }
  showPage('quiz', null);
  try {
    const res = await fetch(API + '/api/questions/sample?cat=' + encodeURIComponent(examSelectedCat) + '&limit=50');
    const data = await res.json();
    currentQuestions = data.map(parseQuestion);
    currentQIndex = 0;
    examAnswers = new Array(currentQuestions.length).fill(null);
    examStartTime = Date.now();
    window.examMode = true;

    // 启动计时器
    let timeLeft = 90 * 60;
    if (examTimerInterval) clearInterval(examTimerInterval);
    examTimerInterval = setInterval(() => {
      timeLeft--;
      const m = Math.floor(timeLeft / 60);
      const s = timeLeft % 60;
      let timerEl = document.getElementById('exam-timer');
      if (!timerEl) {
        timerEl = document.createElement('div');
        timerEl.id = 'exam-timer';
        timerEl.className = 'exam-timer';
        document.body.appendChild(timerEl);
      }
      timerEl.textContent = `⏱ ${m}:${s.toString().padStart(2,'0')}`;
      if (timeLeft <= 0) {
        clearInterval(examTimerInterval);
        submitExam();
      }
    }, 1000);

    renderQuestion();
  } catch (e) {
    alert('加载失败: ' + e.message);
    showPage('home', null);
  }
}

function submitExam() {
  if (examTimerInterval) clearInterval(examTimerInterval);
  const timerEl = document.getElementById('exam-timer');
  if (timerEl) timerEl.remove();

  let correct = 0;
  let answeredCount = 0;
  examAnswers.forEach((ans, i) => {
    if (ans !== null) {
      answeredCount++;
      const q = currentQuestions[i];
      const ansArr = ans.sort();
      const rightArr = q.answer.slice().sort();
      if (JSON.stringify(ansArr) === JSON.stringify(rightArr)) correct++;
    }
  });

  const score = Math.round(correct / currentQuestions.length * 100);
  const usedTime = Math.round((Date.now() - examStartTime) / 60000);

  // 更新修为
  const expGain = Math.round(score / 10);
  exp += expGain;
  localStorage.setItem('geek_exp', exp);

  // 评级
  let grade, comment;
  if (score >= 90) { grade = '甲上'; comment = '宗主点评：天资卓越，可入真传弟子之列！'; }
  else if (score >= 80) { grade = '甲'; comment = '宗主点评：不错！略有疏漏，再细一点便完美。'; }
  else if (score >= 70) { grade = '乙'; comment = '宗主点评：尚可，基础尚可，细节仍需打磨。'; }
  else if (score >= 60) { grade = '丙'; comment = '宗主点评：刚过及格线，回去多刷几道题再来！'; }
  else { grade = '丁'; comment = '宗主点评：哎...出去别说你是我极客宗的人。'; }

  document.getElementById('result-grade').textContent = grade;
  document.getElementById('result-grade').style.color = score >= 60 ? 'var(--brand)' : 'var(--danger)';
  document.getElementById('result-score').textContent = score;
  document.getElementById('result-correct').textContent = correct;
  document.getElementById('result-wrong').textContent = currentQuestions.length - correct;
  document.getElementById('result-time').textContent = usedTime;
  document.getElementById('result-comment').textContent = comment;

  window.examMode = false;
  showPage('exam-result', null);
  renderHome();
}

function reviewWrong() {
  showPage('wrong', null);
}
'''
c = c.replace(old_start_exam, new_start_exam)

# 4. 修改 submitAnswer，记录模考答案
old_submit_answer = '''  // 切换按钮
  document.getElementById('btn-submit').style.display = 'none';
  document.getElementById('btn-next').style.display = 'block';
}'''
new_submit_answer = '''  // 记录模考答案
  if (window.examMode) {
    examAnswers[currentQIndex] = picked;
  }

  // 切换按钮
  document.getElementById('btn-submit').style.display = 'none';
  document.getElementById('btn-next').style.display = 'block';
}'''
c = c.replace(old_submit_answer, new_submit_answer)

# 5. 修改 nextQuestion，最后一题自动交卷
old_next = '''function nextQuestion() {
  if (currentQIndex < currentQuestions.length - 1) {
    currentQIndex++;
    renderQuestion();
  } else {
    showToast('本轮完成！');
    showPage('home', null);
  }
}'''
new_next = '''function nextQuestion() {
  if (currentQIndex < currentQuestions.length - 1) {
    currentQIndex++;
    renderQuestion();
  } else {
    if (window.examMode) {
      submitExam();
    } else {
      showToast('本轮完成！');
      showPage('home', null);
    }
  }
}'''
c = c.replace(old_next, new_next)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added exam (宗门大比) feature')
print(f'New length: {len(c)} chars')
