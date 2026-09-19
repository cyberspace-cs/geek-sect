// app.js · 极客宗修炼 · 全局状态与世界观
// 环境配置：开发/生产切换
const ENV = 'prod'; // 'dev' 本地调试 | 'prod' 正式发布
const CONFIG = {
  dev: {
    baseUrl: 'http://127.0.0.1:8000',
    h5Url: 'http://127.0.0.1:8000/coach.html'
  },
  prod: {
    baseUrl: 'http://43.143.231.106:8000',
    h5Url: 'https://taoxie.vip/shuati-coach.html'
  }
};

// ===== 极客宗世界观设定 =====
const WORLDVIEW = {
  school: '极客宗',
  coach: {
    name: '码道人',
    title: '极客宗宗主',
    personality: '外冷内热，毒舌但护短',
    avatar: '👨‍💻',
    greetings: [
      '来了？今天的 LeetCode 刷了吗？',
      '别磨蹭，编译不等人。',
      '又来偷懒？昨天的 bug 复盘了？',
      '嗯，今日提交记录尚可，可一战。',
      '既入极客宗，便没有半途而废的道理。'
    ],
    praise: [
      '不错，有几分架构师的悟性。',
      '孺子可教，这段代码写得漂亮。',
      '嗯，这道题 bug 找得准。',
      '看来昨夜又肝了通宵。'
    ],
    scold: [
      '菜鸟！这等题也能写错？',
      '昨天刚 code review 过，今天就忘？',
      '你这代码是复制粘贴来的吧？',
      '罢了罢了，回去重写十遍。'
    ]
  },
  realms: [
    { min: 0, name: '筑基', desc: '初入极客宗，Hello World 入门', color: '#94a3b8' },
    { min: 50, name: '金丹', desc: '略通语法，可解简单算法题', color: '#22c55e' },
    { min: 150, name: '元婴', desc: '算法贯通，小有所成', color: '#3b82f6' },
    { min: 300, name: '化神', desc: '才学兼备，可任 Tech Lead', color: '#a855f7' },
    { min: 500, name: '渡劫', desc: '架构大师，大厂架构师水平', color: '#f59e0b' },
    { min: 800, name: '飞升', desc: '学究天人，一代 CTO', color: '#ef4444' }
  ],
  // 功能的极客化命名
  terms: {
    quiz: '打怪升级',
    wrong: 'Bug 录',
    checkin: '每日 Commit',
    chat: '请教宗主',
    report: '宗门大比',
    recommend: '导师辅导',
    community: '论道堂'
  }
};

App({
  globalData: {
    baseUrl: CONFIG[ENV].baseUrl,
    h5Url: CONFIG[ENV].h5Url,
    userId: null,
    userInfo: null,
    worldview: WORLDVIEW,
    exp: 0,           // 修为值
    level: '蒙童',    // 当前境界
    streak: 0         // 连续打坐天数
  },

  onLaunch() {
    const uid = wx.getStorageSync('coach_uid');
    if (uid) this.globalData.userId = uid;
    // 恢复修为数据
    this.globalData.exp = wx.getStorageSync('mo_exp') || 0;
    this.globalData.streak = wx.getStorageSync('mo_streak') || 0;
    this.updateLevel();
  },

  // 根据修为计算境界
  updateLevel() {
    const exp = this.globalData.exp;
    const realms = WORLDVIEW.realms;
    let current = realms[0];
    for (const r of realms) {
      if (exp >= r.min) current = r;
    }
    this.globalData.level = current.name;
    this.globalData.levelInfo = current;
  },

  // 增加修为
  addExp(n) {
    this.globalData.exp += n;
    wx.setStorageSync('mo_exp', this.globalData.exp);
    const oldLevel = this.globalData.level;
    this.updateLevel();
    if (this.globalData.level !== oldLevel) {
      wx.showToast({
        title: `突破！晋升${this.globalData.level}`,
        icon: 'none',
        duration: 2500
      });
    }
    return this.globalData.exp;
  },

  // 码道人随机台词
  randomGreeting() {
    const g = WORLDVIEW.coach.greetings;
    return g[Math.floor(Math.random() * g.length)];
  },

  randomPraise() {
    const p = WORLDVIEW.coach.praise;
    return p[Math.floor(Math.random() * p.length)];
  },

  randomScold() {
    const s = WORLDVIEW.coach.scold;
    return s[Math.floor(Math.random() * s.length)];
  },

  // 统一请求封装
  request(path, method = 'GET', data = {}) {
    const base = this.globalData.baseUrl;
    return new Promise((resolve, reject) => {
      wx.request({
        url: base + path,
        method,
        data,
        header: { 'Content-Type': 'application/json' },
        success: (res) => {
          if (res.statusCode >= 200 && res.statusCode < 300) resolve(res.data);
          else reject(res.data || new Error('HTTP ' + res.statusCode));
        },
        fail: (err) => reject(err)
      });
    });
  },

  async ensureUser() {
    if (this.globalData.userId) return this.globalData.userId;
    const uid = wx.getStorageSync('coach_uid');
    if (uid) { this.globalData.userId = uid; return uid; }
    try {
      const uname = 'wx_' + Date.now().toString(36);
      const r = await this.request('/api/register', 'POST', { username: uname, password: 'coach123' });
      this.globalData.userId = r.id;
      wx.setStorageSync('coach_uid', r.id);
      return r.id;
    } catch (e) {
      const tid = -Date.now();
      this.globalData.userId = tid;
      return tid;
    }
  },

  getUserId() {
    return this.globalData.userId;
  }
});
