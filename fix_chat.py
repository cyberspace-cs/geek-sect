p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 在 showPage 函数里，进入聊天页时初始化欢迎消息
old_show = '''  if (page === 'knowledge') loadKnowledgeMap();
  if (page === 'home') renderHome();'''

new_show = '''  if (page === 'knowledge') loadKnowledgeMap();
  if (page === 'chat') initChat();
  if (page === 'home') renderHome();'''

c = c.replace(old_show, new_show)

# 加 initChat 函数
chat_init_js = '''
function initChat() {
  const messages = document.getElementById('chat-messages');
  if (messages.children.length === 0) {
    messages.innerHTML = `
      <div class="msg msg-bot">👨‍💻 欢迎来到极客宗！我是码道人，有什么修炼上的困惑尽管问。</div>
    `;
  }
}
'''

# 插入到 sendChat 函数之前
c = c.replace('async function sendChat()', chat_init_js + '\nasync function sendChat()')

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed chat page init')
print(f'New length: {len(c)} chars')
