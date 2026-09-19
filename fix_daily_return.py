p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 修复 exitQuiz 函数，确保正确返回首页并更新导航状态
old_exit = '''function exitQuiz() {
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
}'''

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

  // 重置答题状态
  selectedOption = null;
  answerSubmitted = false;

  // 返回首页并更新导航
  showPage('home', null);
  document.querySelectorAll('.nav-item').forEach(x => x.classList.remove('active'));
  document.querySelector('.nav-item')?.classList.add('active');
}'''

c = c.replace(old_exit, new_exit)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed: daily quiz return button')
print(f'New length: {len(c)} chars')
