p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 修改 chat-input-bar 的 bottom 值，避开底部导航栏
old_chat_bar = '''  .chat-input-bar {
    position: fixed;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 480px;
    padding: 12px 16px;
    background: var(--bg);
    border-top: 1px solid var(--line);
    display: flex;
    gap: 8px;
  }'''

new_chat_bar = '''  .chat-input-bar {
    position: fixed;
    bottom: 60px; /* 避开底部导航栏 */
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 480px;
    padding: 12px 16px;
    background: var(--bg);
    border-top: 1px solid var(--line);
    display: flex;
    gap: 8px;
    z-index: 99;
  }'''

c = c.replace(old_chat_bar, new_chat_bar)

# 2. 增加 chat-messages 的底部 margin
old_chat_msgs = '''  .chat-messages {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 80px;
  }'''

new_chat_msgs = '''  .chat-messages {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 140px; /* 避开输入框 + 底部导航 */
  }'''

c = c.replace(old_chat_msgs, new_chat_msgs)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed chat input bar position')
print(f'New length: {len(c)} chars')
