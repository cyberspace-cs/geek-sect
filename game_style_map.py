p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 升级通关地图 CSS - 游戏风格
old_map_css = """  /* ===== 通关地图（冠军同款像素风） ===== */
  .map-container {
    padding: 20px 0;
    overflow-x: auto;
  }
  .map-path {
    position: relative;
    padding: 40px 20px;
  }
  .map-node {
    position: relative;
    width: 100px;
    height: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    margin: 0 auto 70px;
    cursor: pointer;
    border: 4px solid #000;
    border-radius: 12px;
    box-shadow: 6px 8px 0 #000;
    transition: all 0.1s;
    user-select: none;
  }
  .map-node:active {
    transform: translate(4px, 6px);
    box-shadow: 2px 2px 0 #000;
  }
  .map-node.locked {
    background: #1a1a2e;
    border: 4px solid #333;
    color: #555;
    box-shadow: 6px 8px 0 #111;
  }
  .map-node.current {
    background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
    border: 4px solid #000;
    color: #000;
    animation: bounce 1s infinite;
  }
  .map-node.completed {
    background: #00ff88;
    border: 4px solid #000;
    color: #000;
  }
  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }
  .map-node-label {
    position: absolute;
    bottom: -38px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 13px;
    font-weight: 900;
    white-space: nowrap;
    color: #fff;
    text-shadow: 2px 2px 0 #000;
  }
  .map-connector {
    width: 8px;
    height: 50px;
    background: repeating-linear-gradient(
      to bottom,
      #00ff88 0px,
      #00ff88 10px,
      #000 10px,
      #000 15px
    );
    margin: -50px auto 20px;
    border-left: 2px solid #000;
    border-right: 2px solid #000;
  }
  .map-badge {
    position: absolute;
    top: -12px;
    right: -12px;
    background: #ffd166;
    color: #000;
    font-size: 12px;
    font-weight: 900;
    width: 32px;
    height: 32px;
    border: 3px solid #000;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 2px 2px 0 #000;
  }

  /* 通关按钮（冠军同款） */
  .btn-pixel {
    background: #00ff88;
    border: 4px solid #000;
    color: #000;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 900;
    box-shadow: 6px 8px 0 #000;
    cursor: pointer;
    transition: all 0.1s;
    user-select: none;
  }
  .btn-pixel:active {
    transform: translate(4px, 6px);
    box-shadow: 2px 2px 0 #000;
  }
  .btn-pixel-gold {
    background: #ffd166;
  }"""

new_map_css = """  /* ===== 通关地图（冠军游戏风格） ===== */
  .game-map-shell {
    background: #1a1a2e;
    border: 4px solid #000;
    border-radius: 16px;
    box-shadow: 8px 10px 0 #000;
    overflow: hidden;
    margin: 0 -10px;
  }
  .game-hud {
    background: #fff7e8;
    border-bottom: 4px solid #000;
    padding: 12px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 900;
    color: #07142e;
  }
  .game-hud-left {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .game-hud-logo {
    width: 36px;
    height: 36px;
    background: #00ff88;
    border: 3px solid #000;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  .game-hud-right {
    display: flex;
    gap: 12px;
    align-items: center;
    font-size: 14px;
  }
  .game-hearts {
    color: #e73535;
    font-size: 18px;
    text-shadow: 1px 2px 0 #000;
  }
  .game-stars {
    color: #ffd166;
    text-shadow: 1px 2px 0 #000;
  }

  .game-levels {
    padding: 30px 20px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
  .game-level-card {
    background: #fff7e8;
    border: 4px solid #000;
    border-radius: 12px;
    box-shadow: 6px 8px 0 #000;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.1s;
    position: relative;
    user-select: none;
  }
  .game-level-card:active {
    transform: translate(4px, 6px);
    box-shadow: 2px 2px 0 #000;
  }
  .game-level-card.locked {
    background: #2a2a3e;
    color: #666;
    box-shadow: 6px 8px 0 #111;
    cursor: not-allowed;
  }
  .game-level-card.current {
    background: linear-gradient(135deg, #00ff88 0%, #00ccff 100%);
    animation: gamebounce 1.5s infinite;
  }
  .game-level-card.completed {
    background: #00ff88;
  }
  @keyframes gamebounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }
  .game-level-emoji {
    font-size: 48px;
    margin-bottom: 8px;
  }
  .game-level-name {
    font-size: 16px;
    font-weight: 900;
    color: #07142e;
    text-shadow: 1px 2px 0 rgba(255,255,255,0.5);
  }
  .game-level-card.locked .game-level-name {
    color: #888;
  }
  .game-level-desc {
    font-size: 11px;
    color: #627087;
    margin-top: 4px;
  }
  .game-level-badge {
    position: absolute;
    top: -12px;
    right: -12px;
    background: #ffd166;
    color: #000;
    font-size: 12px;
    font-weight: 900;
    padding: 4px 10px;
    border: 3px solid #000;
    border-radius: 20px;
    box-shadow: 2px 2px 0 #000;
  }
  .game-level-card.completed .game-level-badge {
    background: #10b981;
    color: #fff;
  }

  .game-levels-row {
    grid-column: span 2;
    display: flex;
    justify-content: center;
    margin-top: 10px;
  }

  /* 通关按钮（冠军同款） */
  .btn-pixel {
    background: #00ff88;
    border: 4px solid #000;
    color: #000;
    padding: 14px 28px;
    font-size: 16px;
    font-weight: 900;
    box-shadow: 6px 8px 0 #000;
    cursor: pointer;
    transition: all 0.1s;
    user-select: none;
  }
  .btn-pixel:active {
    transform: translate(4px, 6px);
    box-shadow: 2px 2px 0 #000;
  }
  .btn-pixel-gold {
    background: #ffd166;
  }
  .btn-pixel-coral {
    background: #ff6b57;
    color: #fff;
  }"""

c = c.replace(old_map_css, new_map_css)

# 2. 重写通关地图页面 HTML
old_map_html = """  <!-- 通关地图页面 -->
  <div id="page-map" style="display:none">
    <div class="page-title" style="text-shadow: 3px 3px 0 #000;">🗺️ 极客宗通关地图</div>
    <div style="text-align:center;font-size:14px;color:#ffd166;margin-bottom:30px;font-weight:900;text-shadow: 2px 2px 0 #000;">
      从筑基开始，一路打怪升级，飞升成仙
    </div>

    <div class="map-container">
      <div class="map-path">

        <!-- 第1关：筑基期 -->
        <div class="map-node completed" onclick="startQuiz('考研', this)">
          🌱
          <div class="map-badge">✓</div>
          <div class="map-node-label">第1关 · 筑基期</div>
        </div>
        <div class="map-connector"></div>

        <!-- 第2关：金丹期 -->
        <div class="map-node current" onclick="startQuiz('leetcode', this)">
          ⚔️
          <div class="map-badge">!</div>
          <div class="map-node-label">第2关 · 金丹期</div>
        </div>
        <div class="map-connector"></div>

        <!-- 第3关：元婴期 -->
        <div class="map-node locked" onclick="showToast('通关上一关解锁！')">
          🏗️
          <div class="map-node-label">第3关 · 元婴期</div>
        </div>
        <div class="map-connector"></div>

        <!-- 第4关：化神期 -->
        <div class="map-node locked" onclick="showToast('通关上一关解锁！')">
          🤖
          <div class="map-node-label">第4关 · 化神期</div>
        </div>
        <div class="map-connector"></div>

        <!-- 第5关：渡劫期 -->
        <div class="map-node locked" onclick="showToast('通关上一关解锁！')">
          🌌
          <div class="map-node-label">第5关 · 渡劫期</div>
        </div>
        <div class="map-connector"></div>

        <!-- 第6关：飞升 -->
        <div class="map-node locked" onclick="showToast('最终挑战！')">
          🚀
          <div class="map-node-label">第6关 · 飞升</div>
        </div>

      </div>
    </div>

    <div style="margin-top:50px;padding:20px;background:#1a1a2e;border:4px solid #000;box-shadow:6px 8px 0 #000;border-radius:12px">
      <div style="font-size:15px;font-weight:900;color:#ffd166;margin-bottom:10px;text-shadow:2px 2px 0 #000">💡 通关规则</div>
      <ul style="font-size:13px;color:#fff;line-height:2;padding-left:20px;margin:0">
        <li>每关连续答对 20 题即可解锁下一关</li>
        <li>错题自动进入 Bug录，反复刷直到全对</li>
        <li>通关 = 真实掌握，不是背答案</li>
      </ul>
      <div style="text-align:center;margin-top:16px">
        <button class="btn-pixel btn-pixel-gold" onclick="startQuiz('leetcode', this)">
          ⚔️ 开始挑战当前关卡
        </button>
      </div>
    </div>
  </div>"""

new_map_html = """  <!-- 通关地图页面（冠军游戏风格） -->
  <div id="page-map" style="display:none">
    <div class="page-title" style="text-shadow: 3px 3px 0 #000;">🗺️ 极客宗 · 修炼之路</div>

    <div class="game-map-shell">
      <!-- 顶部 HUD -->
      <div class="game-hud">
        <div class="game-hud-left">
          <div class="game-hud-logo">⚔️</div>
          <b>极客宗</b>
        </div>
        <div class="game-hud-right">
          <span class="game-stars">⭐ <span id="map-stars">0</span></span>
          <span class="game-hearts">♥♥♥</span>
        </div>
      </div>

      <!-- 关卡选择 -->
      <div class="game-levels">

        <!-- 第1关：筑基期 -->
        <div class="game-level-card completed" onclick="startQuiz('考研', this)">
          <div class="game-level-badge">✓ 已通关</div>
          <div class="game-level-emoji">🌱</div>
          <div class="game-level-name">第1关 · 筑基期</div>
          <div class="game-level-desc">计算机基础入门</div>
        </div>

        <!-- 第2关：金丹期 -->
        <div class="game-level-card current" onclick="startQuiz('leetcode', this)">
          <div class="game-level-badge">🔥 当前</div>
          <div class="game-level-emoji">⚔️</div>
          <div class="game-level-name">第2关 · 金丹期</div>
          <div class="game-level-desc">LeetCode 算法修炼</div>
        </div>

        <!-- 第3关：元婴期 -->
        <div class="game-level-card locked" onclick="showToast('通关第2关解锁！')">
          <div class="game-level-emoji">🏗️</div>
          <div class="game-level-name">第3关 · 元婴期</div>
          <div class="game-level-desc">系统设计进阶</div>
        </div>

        <!-- 第4关：化神期 -->
        <div class="game-level-card locked" onclick="showToast('通关第3关解锁！')">
          <div class="game-level-emoji">🤖</div>
          <div class="game-level-name">第4关 · 化神期</div>
          <div class="game-level-desc">Agent 框架实战</div>
        </div>

        <!-- 第5关：渡劫期 -->
        <div class="game-level-card locked" onclick="showToast('通关第4关解锁！')">
          <div class="game-level-emoji">🌌</div>
          <div class="game-level-name">第5关 · 渡劫期</div>
          <div class="game-level-desc">RSI 前沿技术</div>
        </div>

        <!-- 第6关：飞升 -->
        <div class="game-level-card locked" onclick="showToast('最终挑战！')">
          <div class="game-level-emoji">🚀</div>
          <div class="game-level-name">第6关 · 飞升</div>
          <div class="game-level-desc">开源贡献 PR</div>
        </div>

        <div class="game-levels-row">
          <button class="btn-pixel btn-pixel-gold" onclick="startQuiz('leetcode', this)">
            ⚔️ 立即挑战当前关卡
          </button>
        </div>

      </div>
    </div>

    <div style="margin-top:24px;padding:16px;background:#1a1a2e;border:4px solid #000;box-shadow:6px 8px 0 #000;border-radius:12px">
      <div style="font-size:14px;font-weight:900;color:#ffd166;margin-bottom:8px;text-shadow:2px 2px 0 #000">💡 修炼规则</div>
      <ul style="font-size:12px;color:#fff;line-height:1.8;padding-left:18px;margin:0">
        <li>每关连续答对 20 题即可解锁下一关</li>
        <li>错题自动进入 Bug录，反复刷直到全对</li>
        <li>通关 = 真实掌握，不是背答案</li>
      </ul>
    </div>
  </div>"""

c = c.replace(old_map_html, new_map_html)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Rewrote map as game-style!')
print(f'New length: {len(c)} chars')
