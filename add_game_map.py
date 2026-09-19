p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加通关地图页面 CSS
old_css_end = '''  .quiz-header {'''

new_css = '''  /* ===== 通关地图 ===== */
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
  }

  .quiz-header {'''

c = c.replace(old_css_end, new_css, 1)

# 2. 加通关地图页面 HTML
old_map_page = '''    <!-- Bug录 -->'''

new_map_page = '''    <!-- 通关地图 -->
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
    </div>

    <!-- Bug录 -->'''

c = c.replace(old_map_page, new_map_page, 1)

# 3. 加底部导航的地图按钮
old_nav = '''    <div class="nav-item active" onclick="showPage('home', this)">
      <div class="nav-icon">🏠</div>
      <div class="nav-label">宗门</div>
    </div>'''

new_nav = '''    <div class="nav-item active" onclick="showPage('home', this)">
      <div class="nav-icon">🏠</div>
      <div class="nav-label">宗门</div>
    </div>
    <div class="nav-item" onclick="showPage('map', this)">
      <div class="nav-icon">🗺️</div>
      <div class="nav-label">通关</div>
    </div>'''

c = c.replace(old_nav, new_nav, 1)

# 4. 首页加快捷入口
old_home_start = '''    <div class="section-title">⚔️ 选择修炼方向</div>'''

new_home_start = '''    <div class="section-title">🗺️ 快速通关</div>
    <div class="cat-grid" style="margin-bottom:20px">
      <div class="cat-card" onclick="showPage('map', null)">
        <div class="cat-icon" style="background:rgba(0,255,136,.15)">🗺️</div>
        <div class="cat-meta">
          <div class="cat-name">通关地图</div>
          <div class="cat-desc">一步步打怪升级</div>
        </div>
      </div>
      <div class="cat-card" onclick="startQuiz('leetcode', this)">
        <div class="cat-icon" style="background:rgba(0,204,255,.15)">⚔️</div>
        <div class="cat-meta">
          <div class="cat-name">算法修炼</div>
          <div class="cat-desc">LeetCode 高频题</div>
        </div>
      </div>
    </div>

    <div class="section-title">⚔️ 选择修炼方向</div>'''

c = c.replace(old_home_start, new_home_start, 1)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added game map page')
print(f'New length: {len(c)} chars')
