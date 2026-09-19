// pages/index/index.js · 极客宗修炼主页
const app = getApp();

Page({
  data: {
    coachGreeting: '',
    realmName: '蒙童',
    realmDesc: '',
    realmColor: '#94a3b8',
    exp: 0,
    nextExp: 50,
    expProgress: 0,
    streak: 0,
    totalQuestions: 0,
    doneToday: 0,
    wrongCount: 0,
    cats: [
      { key: '考研', name: '考研', emoji: '🎓', bg: 'linear-gradient(135deg,#1e3a5f,#2d5a8f)', desc: '数学·英语·政治·专业课', count: 0 },
      { key: '考公', name: '考公', emoji: '🏛️', bg: 'linear-gradient(135deg,#1a4d3a,#2d7a5a)', desc: '行测·申论·常识判断', count: 0 },
      { key: '大厂', name: '大厂', emoji: '💻', bg: 'linear-gradient(135deg,#4a2d6f,#6f4a9f)', desc: '算法·系统·前端·后端', count: 0 }
    ]
  },

  onShow() {
    this.refresh();
  },

  async refresh() {
    const uid = await app.ensureUser();
    this.setData({
      coachGreeting: app.randomGreeting(),
      exp: app.globalData.exp,
      realmName: app.globalData.level,
      realmDesc: app.globalData.levelInfo?.desc || '',
      realmColor: app.globalData.levelInfo?.color || '#94a3b8'
    });
    this.calcProgress();

    try {
      const [all, kaoyan, kaogong, dachang, streak, wrong] = await Promise.all([
        app.request('/api/questions'),
        app.request('/api/questions?cat=考研'),
        app.request('/api/questions?cat=考公'),
        app.request('/api/questions?cat=大厂'),
        app.request('/api/streak/' + uid),
        app.request('/api/wrong-book/' + uid)
      ]);
      const cats = this.data.cats.map(c => {
        const map = { '考研': kaoyan, '考公': kaogong, '大厂': dachang };
        return { ...c, count: (map[c.key] || []).length };
      });
      this.setData({
        totalQuestions: all.length,
        cats,
        streak: streak.streak || 0,
        wrongCount: wrong.length || 0
      });
      this.countToday();
    } catch (e) {
      // 后端不可用时不影响本地展示
    }
  },

  calcProgress() {
    const realms = app.globalData.worldview.realms;
    const exp = this.data.exp;
    let cur = realms[0], next = realms[1];
    for (let i = 0; i < realms.length; i++) {
      if (exp >= realms[i].min) {
        cur = realms[i];
        next = realms[i + 1] || null;
      }
    }
    if (!next) {
      this.setData({ expProgress: 100, nextExp: '已至巅峰' });
    } else {
      const range = next.min - cur.min;
      const done = exp - cur.min;
      this.setData({
        expProgress: Math.min(100, Math.round(done / range * 100)),
        nextExp: next.min - exp
      });
    }
  },

  countToday() {
    const key = 'coach_done_' + this.fmtDate(new Date());
    const n = wx.getStorageSync(key) || 0;
    this.setData({ doneToday: n });
  },

  fmtDate(d) {
    const p = (x) => (x < 10 ? '0' + x : '' + x);
    return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate());
  },

  startQuiz(e) {
    const cat = e.currentTarget.dataset.cat;
    wx.navigateTo({ url: '/pages/quiz/quiz?cat=' + cat });
  },

  openDashboard() {
    wx.navigateTo({ url: '/pages/dashboard/dashboard' });
  },

  openExam() {
    wx.navigateTo({ url: '/pages/exam/exam' });
  },

  openChat() {
    wx.navigateTo({ url: '/pages/chat/chat' });
  },

  openWeb() {
    wx.navigateTo({ url: '/pages/webview/webview?type=home' });
  },

  goMine() {
    wx.switchTab({ url: '/pages/mine/mine' });
  }
});
