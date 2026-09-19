p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 在通关地图的挑战按钮旁边加一个「玩冠军游戏」按钮
old_button = """        <div class="game-levels-row">
          <button class="btn-pixel btn-pixel-gold" onclick="startQuiz('leetcode', this)">
            ⚔️ 立即挑战当前关卡
          </button>
        </div>"""

new_button = """        <div class="game-levels-row" style="flex-direction:column;gap:12px">
          <button class="btn-pixel btn-pixel-gold" onclick="startQuiz('leetcode', this)">
            ⚔️ 立即挑战当前关卡
          </button>
          <button class="btn-pixel btn-pixel-coral" onclick="window.open('/game/index.html', '_blank')">
            🎮 玩冠军游戏 · 地铁旅团
          </button>
        </div>"""

c = c.replace(old_button, new_button)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added game link button!')
print(f'New length: {len(c)} chars')
