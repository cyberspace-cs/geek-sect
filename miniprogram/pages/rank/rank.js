// pages/rank/rank.js · 论道堂排行榜
const app = getApp();

Page({
  data: {
    tab: 'week', // week / total / friends
    rankList: [
      { rank: 1, name: 'Bug终结者', realm: '飞升', exp: 980, avatar: '👑' },
      { rank: 2, name: '代码诗人', realm: '渡劫', exp: 760, avatar: '🎨' },
      { rank: 3, name: '算法狂魔', realm: '渡劫', exp: 680, avatar: '⚡' },
      { rank: 4, name: '架构大师', realm: '化神', exp: 520, avatar: '🏗️' },
      { rank: 5, name: '你', realm: '筑基', exp: 120, avatar: '🧑‍💻', isSelf: true },
      { rank: 6, name: 'CR战神', realm: '金丹', exp: 98, avatar: '🔍' },
      { rank: 7, name: '并发小王子', realm: '金丹', exp: 76, avatar: '🧵' },
      { rank: 8, name: 'SQL剑客', realm: '筑基', exp: 45, avatar: '🗡️' },
      { rank: 9, name: 'Git侠', realm: '筑基', exp: 23, avatar: '🌿' },
      { rank: 10, name: 'Hello World', realm: '筑基', exp: 5, avatar: '👶' }
    ],
    myRank: 5
  },

  switchTab(e) {
    const tab = e.currentTarget.dataset.tab;
    this.setData({ tab });
    // 模拟切换不同榜单
    if (tab === 'total') {
      this.setData({
        rankList: this.data.rankList.map((r, i) => ({ ...r, exp: Math.round(r.exp * 3.5) }))
      });
    } else if (tab === 'week') {
      this.setData({
        rankList: this.data.rankList.map((r, i) => ({ ...r, exp: Math.round(r.exp / 3.5 + Math.random() * 50) }))
      });
    } else {
      // friends
      this.setData({
        rankList: this.data.rankList.filter((r, i) => i < 5 || r.isSelf)
      });
    }
  },

  onShareAppMessage() {
    return {
      title: '极客宗论道堂 · 看看你排第几',
      path: '/pages/rank/rank'
    };
  }
});
