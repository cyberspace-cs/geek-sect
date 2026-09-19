p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 在 Bug录页面加"开始重练"按钮
old_wrong_page = '''  <!-- 错题本页 -->
  <div id="page-wrong" style="display:none">
    <div class="section-title">Bug录 · 待修复</div>
    <div class="wrong-list" id="wrong-list"></div>
  </div>'''

new_wrong_page = '''  <!-- 错题本页 -->
  <div id="page-wrong" style="display:none">
    <div class="section-title">Bug录 · 待修复</div>
    <div class="quiz-footer" style="margin-bottom: 20px; margin-top: 0;">
      <button class="btn btn-primary" onclick="startWrongReview()">开始重练 Bug</button>
    </div>
    <div class="wrong-list" id="wrong-list"></div>
  </div>'''

c = c.replace(old_wrong_page, new_wrong_page)

# 2. 加错题重练 JS
wrong_js = '''
async function startWrongReview() {
  showPage('quiz', null);
  try {
    const res = await fetch(API + '/api/wrong-book/' + userId);
    const data = await res.json();
    if (!data.length) {
      alert('Bug录是空的，继续保持！');
      showPage('wrong', null);
      return;
    }
    currentQuestions = data.map(w => parseQuestion(w.question));
    currentQIndex = 0;
    window.wrongReviewMode = true;
    renderQuestion();
  } catch (e) {
    alert('加载失败: ' + e.message);
    showPage('wrong', null);
  }
}
'''

# 插入到 startDailyQuestion 之后
c = c.replace('async function startQuiz(cat)', wrong_js + '\nasync function startQuiz(cat)')

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added wrong review feature')
print(f'New length: {len(c)} chars')
