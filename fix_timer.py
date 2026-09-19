p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 把返回按钮的 onclick 改成 exitQuiz()
c = c.replace(
    'onclick="showPage(\'home\', null)">返回</button>',
    'onclick="exitQuiz()">返回</button>'
)

# 2. 加 exitQuiz 函数，放在 submitExam 函数之前
old_submit = 'function submitExam() {'
new_exit = '''function exitQuiz() {
  // 停止计时器并移除
  if (examTimerInterval) {
    clearInterval(examTimerInterval);
    examTimerInterval = null;
  }
  const timerEl = document.getElementById('exam-timer');
  if (timerEl) timerEl.remove();

  // 重置模考模式
  window.examMode = false;

  // 返回首页
  showPage('home', null);
}

function submitExam() {'''

c = c.replace(old_submit, new_exit)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed: exit quiz stops timer and hides it')
print(f'New length: {len(c)} chars')
