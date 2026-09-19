p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加知识图谱页 HTML
km_html = '''
  <!-- 知识图谱页 -->
  <div id="page-knowledge" style="display:none">
    <div class="section-title">🗺️ 知识图谱 · 你的修炼版图</div>
    <div class="report-card">
      <div class="report-title">🎯 知识点掌握度</div>
      <div id="km-topics"></div>
    </div>
    <div class="report-card">
      <div class="report-title">⚠️ 薄弱知识点</div>
      <div id="km-weak"></div>
    </div>
  </div>
'''

# 插入到成就页之前
ach_start = c.find('<div id="page-achievement"')
if ach_start > 0:
    c = c[:ach_start] + km_html + c[ach_start:]

# 2. 在首页功能网格加"知识图谱"入口
old_feat2 = '''      <div class="feature-card" onclick="showPage('achievement', this)">
        <div class="feature-icon">🏅</div>
        <div class="feature-title">成就堂</div>
        <div class="feature-desc">里程碑徽章</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">'''

new_feat2 = '''      <div class="feature-card" onclick="showPage('achievement', this)">
        <div class="feature-icon">🏅</div>
        <div class="feature-title">成就堂</div>
        <div class="feature-desc">里程碑徽章</div>
      </div>
      <div class="feature-card" onclick="showPage('knowledge', this)">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">知识图谱</div>
        <div class="feature-desc">修炼版图</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">'''

c = c.replace(old_feat2, new_feat2)

# 3. 加知识图谱 JS
km_js = '''
async function loadKnowledgeMap() {
  // 模拟数据（实际应该从后端错题统计）
  const topics = [
    { name: '数据结构', mastered: 85 },
    { name: '算法设计', mastered: 72 },
    { name: '操作系统', mastered: 68 },
    { name: '计算机网络', mastered: 90 },
    { name: '数据库', mastered: 55 },
    { name: '系统设计', mastered: 45 },
    { name: '前端基础', mastered: 78 },
    { name: '后端开发', mastered: 60 },
  ];

  // 掌握度排序
  topics.sort((a, b) => b.mastered - a.mastered);

  document.getElementById('km-topics').innerHTML = topics.map(t => `
    <div class="topic-bar">
      <div class="topic-name">${t.name}</div>
      <div class="topic-bar-bg">
        <div class="topic-bar-fill" style="width: ${t.mastered}%; background: ${t.mastered >= 80 ? 'linear-gradient(90deg, #00ff88, #00ccff)' : t.mastered >= 60 ? 'linear-gradient(90deg, #ffb84d, #ff9800)' : 'linear-gradient(90deg, #ff6b6b, #ff4444)'}"></div>
      </div>
      <div class="topic-pct">${t.mastered}%</div>
    </div>
  `).join('');

  // 薄弱知识点
  const weakTopics = topics.filter(t => t.mastered < 60);
  if (weakTopics.length === 0) {
    document.getElementById('km-weak').innerHTML = '<div style="text-align:center;color:var(--ink-3);padding:20px">暂无薄弱知识点，继续保持！</div>';
  } else {
    document.getElementById('km-weak').innerHTML = weakTopics.map(t => `
      <div class="cat-card" style="margin-bottom:8px">
        <div class="cat-icon" style="background:rgba(255,107,107,.15)">⚠️</div>
        <div class="cat-meta">
          <div class="cat-name">${t.name}</div>
          <div class="cat-desc">掌握度仅 ${t.mastered}%，建议多刷相关题目</div>
        </div>
        <div class="cat-count" style="color:var(--danger)">待提升</div>
      </div>
    `).join('');
  }
}
'''

# 插入到 loadAchievements 函数之前
c = c.replace('const ACHIEVEMENTS = [', km_js + '\nconst ACHIEVEMENTS = [')

# 4. 修改 showPage，加载知识图谱页
old_show2 = '''  if (page === 'achievement') loadAchievements();'''
new_show2 = '''  if (page === 'achievement') loadAchievements();
  if (page === 'knowledge') loadKnowledgeMap();'''
c = c.replace(old_show2, new_show2)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added knowledge map feature')
print(f'New length: {len(c)} chars')
