// pages/chat/chat.js · 问教练（转发到后端 /api/chat → Hermes Agent）
const app = getApp();

Page({
  data: {
    messages: [],   // { role: 'user' | 'assistant', content: string }
    input: '',
    loading: false
  },

  onInput(e) {
    this.setData({ input: e.detail.value });
  },

  async send() {
    const text = (this.data.input || '').trim();
    if (!text || this.data.loading) return;

    const history = this.data.messages.concat([{ role: 'user', content: text }]);
    this.setData({ messages: history, input: '', loading: true });

    try {
      const res = await app.request('/api/chat', 'POST', {
        system: '你是「极客宗」宗主码道人，一位外冷内热、毒舌但护短的AI导师。用极客/程序员的黑话风格，用通俗中文回答用户关于题目、知识点、复习方法与备考规划的问题。可以用「bug」「commit」「debug」「编译」等程序员术语类比，必要时给出具体例子。偶尔毒舌吐槽，但最后总会给鼓励。',
        messages: history.map(m => ({ role: m.role, content: m.content }))
      });
      const reply = (res && res.reply) ? res.reply : '（暂无回复）';
      this.setData({
        messages: this.data.messages.concat([{ role: 'assistant', content: reply }]),
        loading: false
      });
    } catch (e) {
      this.setData({
        messages: this.data.messages.concat([{ role: 'assistant', content: '网络开小差了，稍后再试～' }]),
        loading: false
      });
      wx.showToast({ title: '请求失败', icon: 'none' });
    }
  }
});
