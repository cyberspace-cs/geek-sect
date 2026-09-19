// pages/exam/exam.js · 宗门大比（模考）
const app = getApp();

Page({
  data: {
    stage: 'home', // home / countdown / running / result
    cat: '考研',
    timeLeft: 600, // 10分钟
    questions: [],
    current: 0,
    answers: [],
    score: 0,
    correctCount: 0,
    totalCount: 0,
    rank: null
  },

  onLoad() {
    // 初始化
  },

  startExam(e) {
    const cat = e.currentTarget.dataset.cat || this.data.cat;
    this.setData({ cat, stage: 'countdown' });
    this.countdown(3);
  },

  countdown(n) {
    if (n <= 0) {
      this.beginExam();
      return;
    }
    this.setData({ countNum: n });
    setTimeout(() => this.countdown(n - 1), 800);
  },

  async beginExam() {
    try {
      const list = await app.request('/api/questions?cat=' + this.data.cat);
      const questions = list.slice(0, 20).map(q => ({
        ...q,
        options: JSON.parse(q.opts || '[]'),
        answer: JSON.parse(q.answer || '[]')
      }));
      this.setData({
        stage: 'running',
        questions,
        totalCount: questions.length,
        answers: new Array(questions.length).fill(null)
      });
      this.startTimer();
    } catch (e) {
      wx.showToast({ title: '加载试题失败', icon: 'none' });
      this.setData({ stage: 'home' });
    }
  },

  startTimer() {
    this.timer = setInterval(() => {
      const t = this.data.timeLeft - 1;
      this.setData({ timeLeft: t });
      if (t <= 0) this.finishExam();
    }, 1000);
  },

  selectAnswer(e) {
    const { i } = e.currentTarget.dataset;
    const answers = [...this.data.answers];
    answers[this.data.current] = i;
    this.setData({ answers });
  },

  nextQuestion() {
    if (this.data.current < this.data.questions.length - 1) {
      this.setData({ current: this.data.current + 1 });
    }
  },

  prevQuestion() {
    if (this.data.current > 0) {
      this.setData({ current: this.data.current - 1 });
    }
  },

  finishExam() {
    clearInterval(this.timer);
    const { questions, answers } = this.data;
    let correct = 0;
    questions.forEach((q, i) => {
      if (answers[i] !== null && q.answer.includes(answers[i])) correct++;
    });
    const score = Math.round(correct / questions.length * 100);

    // 加修为
    const expGain = Math.round(score / 10);
    app.addExp(expGain);

    // 模拟排名
    const rank = Math.max(1, Math.round(100 - score + Math.random() * 20));

    this.setData({
      stage: 'result',
      correctCount: correct,
      score,
      rank,
      expGain
    });
  },

  onUnload() {
    if (this.timer) clearInterval(this.timer);
  }
});
