// pages/dashboard/dashboard.js · AI 修炼仪表盘
const app = getApp();

// AI 教练团队角色设定 · 极客宗四大长老
const AGENT_TEAM = [
  {
    id: 'diagnost',
    name: 'Bug猎人·长红',
    role: '错题归因分析',
    icon: '🔍',
    color: '#3b82f6',
    desc: '分析你的错题模式，找出知识盲区'
  },
  {
    id: 'analyst',
    name: '数据巫师·长青',
    role: '知识图谱建模',
    icon: '🕸️',
    color: '#8b5cf6',
    desc: '构建你的掌握度图谱，可视化强弱项'
  },
  {
    id: 'strategist',
    name: '架构宗师·长白',
    role: '学习路径规划',
    icon: '🗺️',
    color: '#10b981',
    desc: '制定个性化修炼路径，效率最大化'
  },
  {
    id: 'lecturer',
    name: '布道师·长玄',
    role: '定制讲题生成',
    icon: '📖',
    color: '#f59e0b',
    desc: '针对薄弱点生成专属讲解与变式题'
  }
];

Page({
  data: {
    team: AGENT_TEAM,
    activeStep: 0,
    teamStatus: ['idle', 'idle', 'idle', 'idle'], // idle / running / done
    teamLogs: [],
    // 知识掌握度（模拟数据，后续接真实后端）
    knowledgeRadar: [
      { subject: '数学', value: 65 },
      { subject: '英语', value: 78 },
      { subject: '政治', value: 45 },
      { subject: '专业课', value: 60 },
      { subject: '算法', value: 55 },
      { subject: '系统设计', value: 40 }
    ],
    weakPoints: [
      { name: '动态规划', mastery: 25, count: 12, level: '危险' },
      { name: '操作系统进程', mastery: 30, count: 8, level: '警告' },
      { name: '英语长难句', mastery: 45, count: 6, level: '警告' },
      { name: '马原辩证法', mastery: 50, count: 5, level: '注意' }
    ],
    recommendPath: [
      { step: 1, title: '攻克动态规划', detail: '先学背包问题，再刷 15 道经典题', exp: 80 },
      { step: 2, title: '操作系统进程同步', detail: 'PV操作经典模型 + 错题复盘', exp: 60 },
      { step: 3, title: '英语长难句拆解', detail: '每日 5 句精读，积累 30 天', exp: 40 }
    ],
    analyzing: false
  },

  onLoad() {
    this.runAnalysis();
  },

  // 模拟多智能体协作分析过程
  async runAnalysis() {
    this.setData({ analyzing: true, teamLogs: [], teamStatus: ['running', 'idle', 'idle', 'idle'] });

    const logs = [
      { agent: 0, text: '长红开始扫描错题库...', time: '0.1s' },
      { agent: 0, text: '发现 47 道错题，归类为 12 个知识点', time: '1.2s' },
      { agent: 0, text: '动态规划错误率最高：75%', time: '2.1s' },
      { agent: 1, text: '长青开始构建知识图谱...', time: '2.3s' },
      { agent: 1, text: '已建模 6 个学科、24 个知识点节点', time: '3.8s' },
      { agent: 1, text: '掌握度雷达图生成完毕', time: '4.5s' },
      { agent: 2, text: '长白开始规划最优路径...', time: '4.7s' },
      { agent: 2, text: '基于遗忘曲线，优先攻克高权重弱项', time: '5.8s' },
      { agent: 2, text: '推荐路径生成：3 步走，预计 7 天见效', time: '6.5s' },
      { agent: 3, text: '长玄准备定制讲题...', time: '6.7s' },
      { agent: 3, text: '已为「动态规划」生成 3 道变式题', time: '7.5s' },
      { agent: 3, text: '分析完成！查看下方报告', time: '8.0s' }
    ];

    for (let i = 0; i < logs.length; i++) {
      await this.delay(600);
      const log = logs[i];
      const newLogs = this.data.teamLogs.concat([log]);
      const newStatus = [...this.data.teamStatus];
      // 标记当前 agent 为 running，前一个为 done
      newStatus[log.agent] = 'running';
      if (log.agent > 0) newStatus[log.agent - 1] = 'done';
      if (i === logs.length - 1) newStatus[log.agent] = 'done';
      this.setData({ teamLogs: newLogs, teamStatus: newStatus });
    }

    this.setData({ analyzing: false });
  },

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  },

  goQuiz(e) {
    const topic = e.currentTarget.dataset.topic;
    wx.navigateTo({ url: '/pages/quiz/quiz?cat=' + topic });
  },

  onShareAppMessage() {
    return {
      title: '我的 AI 修炼报告 · 极客宗修炼',
      path: '/pages/dashboard/dashboard'
    };
  }
});
