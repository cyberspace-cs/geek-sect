p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 升级通关地图 CSS，改成冠军游戏同款风格
old_map_css = '''  /* ===== 通关地图 ===== */
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
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin: 0 auto 60px;
    transition: all 0.3s;
    cursor: pointer;
  }
  .map-node.locked {
    background: #1a1a2e;
    border: 2px dashed #333;
    color: #555;
  }
  .map-node.current {
    background: rgba(0,255,136,.15);
    border: 2px solid var(--brand);
    color: var(--brand);
    box-shadow: 0 0 30px rgba(0,255,136,.3);
    animation: pulse 2s infinite;
  }
  .map-node.completed {
    background: rgba(0,255,136,.2);
    border: 2px solid var(--brand);
    color: var(--brand);
  }
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 20px rgba(0,255,136,.3); }
    50% { box-shadow: 0 0 40px rgba(0,255,136,.6); }
  }
  .map-node-label {
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
    white-space: nowrap;
    color: var(--ink-2);
  }
  .map-connector {
    width: 2px;
    height: 40px;
    background: linear-gradient(to bottom, var(--brand), #333);
    margin: -40px auto 20px;
  }
  .map-badge {
    position: absolute;
    top: -5px;
    right: -5px;
    background: var(--warning);
    color: #000;
    font-size: 10px;
    font-weight: 700;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }'''

new_map_css = '''  /* ===== 通关地图（冠军同款像素风） ===== */
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
  }'''

c = c.replace(old_map_css, new_map_css)

# 2. 升级通关地图页面 HTML
old_map_html = '''    <!-- 通关地图 -->
    <div class="page" id="page-map">
      <div class="page-title">🗺️ 极客宗通关地图</div>
      <div style="text-align:center;font-size:13px;color:var(--ink-3);margin-bottom:20px">
        从筑基开始，一路打怪升级，飞升成仙
      </div>

      <div class="map-container">
        <div class="map-path">

          <!-- 第1关：筑基期 -->
          <div class="map-node completed" onclick="startQuiz('kaoyan', this)">
            🌱
            <div class="map-node-label">筑基期 · 计算机基础</div>
            <div class="map-badge">1/3</div>
          </div>
          <div class="map-connector"></div>

          <!-- 第2关：金丹期 -->
          <div class="map-node current" onclick="startQuiz('leetcode', this)">
            ⚔️
            <div class="map-node-label">金丹期 · 算法修炼</div>
          </div>
          <div class="map-connector"></div>

          <!-- 第3关：元婴期 -->
          <div class="map-node locked" onclick="showToast('通关上一关解锁！')">
            🏗️
            <div class="map-node-label">元婴期 · 系统设计</div>
          </div>
          <div class="map-connector"></div>

          <!-- 第4关：化神期 -->
          <div class="map-node locked" onclick="showToast('通关上一关解锁！')">
            🤖
            <div class="map-node-label">化神期 · Agent 框架</div>
          </div>
          <div class="map-connector"></div>

          <!-- 第5关：渡劫期 -->
          <div class="map-node locked" onclick="showToast('通关上一关解锁！')">
            🌌
            <div class="map-node-label">渡劫期 · RSI 前沿</div>
          </div>
          <div class="map-connector"></div>

          <!-- 第6关：飞升 -->
          <div class="map-node locked" onclick="showToast('最终挑战！')">
            🚀
            <div class="map-node-label">飞升 · 开源贡献</div>
          </div>

        </div>
      </div>

      <div style="margin-top:40px;padding:16px;background:rgba(0,255,136,.05);border-radius:12px">
        <div style="font-size:13px;font-weight:700;color:var(--brand);margin-bottom:8px">💡 通关规则</div>
        <ul style="font-size:12px;color:var(--ink-2);line-height:1.8;padding-left:16px;margin:0">
          <li>每关连续答对 20 题即可解锁下一关</li>
          <li>错题自动进入 Bug录，反复刷直到全对</li>
          <li>通关 = 真实掌握，不是背答案</li>
        </ul>
      </div>
    </div>'''

new_map_html = '''    <!-- 通关地图 -->
    <div class="page" id="page-map">
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
    </div>'''

c = c.replace(old_map_html, new_map_html)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Upgraded map to champion pixel style!')
print(f'New length: {len(c)} chars')
