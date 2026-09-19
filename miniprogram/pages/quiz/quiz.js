// pages/quiz/quiz.js
const app = getApp();

Page({
  data: {
    cat: '',
    questions: [],
    cur: 0,
    q: {},
    abc: ['A', 'B', 'C', 'D', 'E', 'F'],
    selected: [],
    showAnswer: false,
    correctCount: 0,
    // 新增：计时与统计
    seconds: 0,
    timer: null,
    perQTime: [],       // 每题用时
    qStartTs: 0,
    // 新增：结果页
    showResult: false,
    accuracy: 0,
    avgTime: 0,
    // 新增：收藏
    favorites: []
  },

  onLoad(opt) {
    const cat = opt.cat || '考研';
    this.setData({ cat });
    wx.setNavigationBarTitle({ title: cat + ' · 刷题' });
    this.load(cat);
    this.loadFavorites();
  },

  onUnload() {
    if (this.data.timer) clearInterval(this.data.timer);
  },

  loadFavorites() {
    const fav = wx.getStorageSync('coach_fav_' + this.data.cat) || [];
    this.setData({ favorites: fav });
  },

  saveFavorite(qid) {
    let fav = wx.getStorageSync('coach_fav_' + this.data.cat) || [];
    if (fav.includes(qid)) {
      fav = fav.filter(x => x !== qid);
      wx.showToast({ title: '已取消收藏', icon: 'none' });
    } else {
      fav.push(qid);
      wx.showToast({ title: '已收藏', icon: 'success' });
    }
    wx.setStorageSync('coach_fav_' + this.data.cat, fav);
    this.setData({ favorites: fav });
  },

  isFav(qid) {
    return this.data.favorites.includes(qid);
  },

  async load(cat) {
    try {
      const list = await app.request('/api/questions?cat=' + cat);
      const questions = list.map(q => ({
        ...q,
        options: JSON.parse(q.opts || '[]'),
        answer: JSON.parse(q.answer || '[]'),
        wrongAdded: false
      }));
      this.setData({ questions });
      this.startTimer();
      this.render(0);
    } catch (e) {
      wx.showToast({ title: '加载失败', icon: 'none' });
    }
  },

  startTimer() {
    if (this.data.timer) clearInterval(this.data.timer);
    const t = setInterval(() => {
      this.setData({ seconds: this.data.seconds + 1 });
    }, 1000);
    this.setData({ timer: t });
  },

  render(i) {
    const elapsed = Math.round((Date.now() - this.data.qStartTs) / 1000);
    const perQTime = this.data.perQTime.slice();
    if (this.data.qStartTs > 0) perQTime.push(elapsed);
    this.setData({
      cur: i,
      q: this.data.questions[i],
      selected: [],
      showAnswer: false,
      qStartTs: Date.now(),
      perQTime
    });
  },

  onSelect(e) {
    if (this.data.showAnswer) return;
    const i = e.currentTarget.dataset.i;
    const q = this.data.q;
    const selected = this.data.selected.slice();
    if (q.type === '多选题') {
      selected[i] = !selected[i];
    } else {
      // 单选 / 判断：只能选一个
      for (let k = 0; k < selected.length; k++) selected[k] = false;
      selected[i] = true;
    }
    this.setData({ selected });
  },

  isCorrect(i) {
    return this.data.q.answer.includes(i);
  },

  submit() {
    const { q, selected, questions, cur } = this.data;
    const picked = selected.map((s, i) => (s ? i : -1)).filter(i => i >= 0).sort();
    const ans = q.answer.slice().sort();
    const right = JSON.stringify(picked) === JSON.stringify(ans);

    const qs = questions.slice();
    qs[cur] = { ...q, wrongAdded: false };
    let correctCount = this.data.correctCount + (right ? 1 : 0);
    let coachComment = '';
    let expGain = 0;

    if (right) {
      expGain = 10;
      coachComment = app.randomPraise();
      app.addExp(expGain);
    } else {
      coachComment = app.randomScold();
    }

    this.setData({
      showAnswer: true,
      questions: qs,
      correctCount,
      coachComment,
      expGain
    });

    // 答错自动加入错题本
    if (!right) this.addWrong(true);
    this.recordDone(1);
  },

  async addWrong(silent) {
    const uid = app.getUserId();
    const q = this.data.q;
    if (q.wrongAdded) return;
    try {
      await app.request('/api/wrong-book', 'POST', { user_id: uid, question_id: q.id });
      const qs = this.data.questions.slice();
      qs[this.data.cur] = { ...qs[this.data.cur], wrongAdded: true };
      this.setData({ questions: qs });
      if (!silent) wx.showToast({ title: '已加入错题本', icon: 'success' });
    } catch (e) {}
  },

  prev() { if (this.data.cur > 0) this.render(this.data.cur - 1); },
  next() { if (this.data.cur < this.data.questions.length - 1) this.render(this.data.cur + 1); },

  async finish() {
    const uid = app.getUserId();
    const { cat, questions, correctCount } = this.data;
    try {
      await app.request('/api/quiz/record', 'POST', {
        user_id: uid, cat, total: questions.length, correct: correctCount
      });
    } catch (e) {}
    wx.showModal({
      title: '本轮完成',
      content: `共 ${questions.length} 题，答对 ${correctCount} 题。`,
      confirmText: '返回',
      showCancel: false,
      success: () => wx.navigateBack()
    });
  },

  // 本地累计今日刷题数（用于首页统计）
  recordDone(n) {
    const d = new Date();
    const p = (x) => (x < 10 ? '0' + x : '' + x);
    const key = 'coach_done_' + (d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()));
    const cur = wx.getStorageSync(key) || 0;
    wx.setStorageSync(key, cur + n);
  }
});
