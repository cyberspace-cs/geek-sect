p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 修复 showPage 里的类名（tab-item，不是 nav-item）
old_show_nav = """  document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active'));
  if (tabEl) tabEl.classList.add('active');"""
new_show_nav = """  document.querySelectorAll('.tab-item').forEach(t => t.classList.remove('active'));
  if (tabEl) tabEl.classList.add('active');"""
c = c.replace(old_show_nav, new_show_nav)

# 2. 修复 exitQuiz 里的类名
old_exit_nav = """  document.querySelectorAll('.nav-item').forEach(x => x.classList.remove('active'));
  document.querySelector('.nav-item')?.classList.add('active');"""
new_exit_nav = """  document.querySelectorAll('.tab-item').forEach(x => x.classList.remove('active'));
  document.querySelector('.tab-item')?.classList.add('active');"""
c = c.replace(old_exit_nav, new_exit_nav)

# 3. 在 page-rank 后面插入通关地图页面 HTML
old_page_rank_end = """<div id="page-rank" style="display:none">
    <div class="section-title">论道堂 · 排行榜</div>
    <div class="cat-list" id="rank-list"></div>
  </div>"""

new_pages_end = """<div id="page-rank" style="display:none">
    <div class="section-title">论道堂 · 排行榜</div>
    <div class="cat-list" id="rank-list"></div>
  </div>

  <!-- 通关地图页面 -->
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

c = c.replace(old_page_rank_end, new_pages_end)

# 4. 底部导航加上「通关」按钮
old_tab_bar = """<div class="tab-bar">
  <div class="tab-item active" onclick="showPage('home', this)">
    <div class="tab-icon">🏠</div>
    首页
  </div>
  <div class="tab-item" onclick="showPage('wrong', this)">
    <div class="tab-icon">🐛</div>
    Bug录
  </div>
  <div class="tab-item" onclick="showPage('chat', this)">
    <div class="tab-icon">💬</div>
    宗主
  </div>
  <div class="tab-item" onclick="showPage('rank', this)">
    <div class="tab-icon">🏆</div>
    论道
  </div>
</div>"""

new_tab_bar = """<div class="tab-bar">
  <div class="tab-item active" onclick="showPage('home', this)">
    <div class="tab-icon">🏠</div>
    首页
  </div>
  <div class="tab-item" onclick="showPage('map', this)">
    <div class="tab-icon">🗺️</div>
    通关
  </div>
  <div class="tab-item" onclick="showPage('wrong', this)">
    <div class="tab-icon">🐛</div>
    Bug录
  </div>
  <div class="tab-item" onclick="showPage('chat', this)">
    <div class="tab-icon">💬</div>
    宗主
  </div>
  <div class="tab-item" onclick="showPage('rank', this)">
    <div class="tab-icon">🏆</div>
    论道
  </div>
</div>"""

c = c.replace(old_tab_bar, new_tab_bar)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed everything!')
print(f'New length: {len(c)} chars')
