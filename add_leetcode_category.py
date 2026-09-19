p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加 LeetCode 分类选项
old_cats = '''        <div class="filter-chips">
          <button class="chip active" onclick="startQuiz('all', this)">全部</button>
          <button class="chip" onclick="startQuiz('kaoyan', this)">考研</button>
          <button class="chip" onclick="startQuiz('dachang', this)">大厂</button>
          <button class="chip" onclick="startQuiz('gongkao', this)">考公</button>
          <button class="chip" onclick="startQuiz('sys_design', this)">系统设计+数据库</button>
        </div>'''

new_cats = '''        <div class="filter-chips">
          <button class="chip active" onclick="startQuiz('all', this)">全部</button>
          <button class="chip" onclick="startQuiz('kaoyan', this)">考研</button>
          <button class="chip" onclick="startQuiz('dachang', this)">大厂</button>
          <button class="chip" onclick="startQuiz('gongkao', this)">考公</button>
          <button class="chip" onclick="startQuiz('sys_design', this)">系统设计</button>
          <button class="chip" onclick="startQuiz('leetcode', this)">算法·LeetCode</button>
        </div>'''

c = c.replace(old_cats, new_cats)

# 2. 修改 loadQuestions 函数，加 leetcode 筛选逻辑
old_load_q = '''async function loadQuestions(cat) {
  renderPageLoading();
  try {
    const res = await fetch(API + '/api/questions/sample?cat=' + cat + '&limit=30');'''

new_load_q = '''async function loadQuestions(cat) {
  renderPageLoading();
  try {
    if (cat === 'leetcode') {
      // LeetCode 分类：从大厂题库里筛选算法题
      const res0 = await fetch(API + '/api/questions/sample?cat=dachang&limit=200');
      const all = await res0.json();
      currentSet = all.filter(q =>
        q.topic && (
          q.topic.includes('算法') ||
          q.topic.includes('数据结构') ||
          q.topic.includes('数组') ||
          q.topic.includes('链表') ||
          q.topic.includes('栈') ||
          q.topic.includes('队列') ||
          q.topic.includes('树') ||
          q.topic.includes('哈希') ||
          q.topic.includes('动态规划')
        )
      ).slice(0, 30);
      if (currentSet.length === 0) {
        currentSet = all.slice(0, 30);
      }
      idx = 0;
      showPage('quiz', null);
      renderQuestion();
      return;
    }
    const res = await fetch(API + '/api/questions/sample?cat=' + cat + '&limit=30');'''

c = c.replace(old_load_q, new_load_q)

# 3. 加 GitHub 项目修炼模块到宗门典籍页
old_codex = '''    <div class="codex-card">
      <div class="codex-title">🔥 GitHub 热门 Agent 项目 Top 20</div>'''

new_codex = '''    <div class="codex-card">
      <div class="codex-title">🛠️ GitHub 项目修炼（刷项目 = 真实 Commit）</div>
      <div style="font-size:12px;color:var(--ink-3);margin-bottom:16px">每个项目都是一道「实战算法题」，读完代码 → 跑通本地 → 提第一个 PR = 一次真实 Commit</div>

      <div style="display:flex;flex-direction:column;gap:16px">
        <div style="padding:14px;background:rgba(0,255,136,.05);border-radius:10px">
          <div style="font-size:14px;font-weight:700;color:var(--brand);margin-bottom:10px">🌱 入门级（Good First Issue）</div>

          <div style="margin-bottom:12px">
            <div style="font-size:13px;font-weight:700">📦 awesome-agent-frameworks</div>
            <div style="font-size:12px;color:var(--ink-3);margin:4px 0">Agent 框架大全 · 适合入门</div>
            <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 修炼任务：</div>
            <ul style="font-size:12px;color:var(--ink-2);margin-top:4px;padding-left:16px">
              <li>添加一个新发现的 Agent 框架到列表</li>
              <li>修复一个 README 里的错别字</li>
              <li>添加一个新的分类标签</li>
            </ul>
          </div>

          <div>
            <div style="font-size:13px;font-weight:700">📦 browser-use</div>
            <div style="font-size:12px;color:var(--ink-3);margin:4px 0">浏览器自动化 Agent · 115K Star</div>
            <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 修炼任务：</div>
            <ul style="font-size:12px;color:var(--ink-2);margin-top:4px;padding-left:16px">
              <li>写一个新的 usage example</li>
              <li>修复一个文档错误</li>
              <li>添加一个新的 helper 函数</li>
            </ul>
          </div>
        </div>

        <div style="padding:14px;background:rgba(0,204,255,.05);border-radius:10px">
          <div style="font-size:14px;font-weight:700;color:var(--accent);margin-bottom:10px">⚔️ 进阶级（生产级框架）</div>

          <div style="margin-bottom:12px">
            <div style="font-size:13px;font-weight:700">📦 LangChain</div>
            <div style="font-size:12px;color:var(--ink-3);margin:4px 0">LLM 应用开发框架 · 147K Star</div>
            <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 修炼任务：</div>
            <ul style="font-size:12px;color:var(--ink-2);margin-top:4px;padding-left:16px">
              <li>给某个组件写单元测试</li>
              <li>添加一个新的 output parser</li>
              <li>改进错误提示信息</li>
            </ul>
          </div>

          <div>
            <div style="font-size:13px;font-weight:700">📦 CrewAI</div>
            <div style="font-size:12px;color:var(--ink-3);margin:4px 0">多 Agent 协作框架 · 53K Star</div>
            <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 修炼任务：</div>
            <ul style="font-size:12px;color:var(--ink-2);margin-top:4px;padding-left:16px">
              <li>添加一个新的 Agent role 示例</li>
              <li>改进文档中的示例代码</li>
            </ul>
          </div>
        </div>

        <div style="padding:14px;background:rgba(255,107,107,.05);border-radius:10px">
          <div style="font-size:14px;font-weight:700;color:var(--danger);margin-bottom:10px">🚀 前沿级（RSI / 自我改进）</div>

          <div>
            <div style="font-size:13px;font-weight:700">📦 RSI Agent 类项目</div>
            <div style="font-size:12px;color:var(--ink-3);margin:4px 0">Recursive Self-Improvement · 前沿方向</div>
            <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 修炼任务：</div>
            <ul style="font-size:12px;color:var(--ink-2);margin-top:4px;padding-left:16px">
              <li>读懂论文里的算法公式</li>
              <li>复现论文里的核心实验</li>
              <li>对比不同 RSI 实现的优劣</li>
            </ul>
          </div>
        </div>

      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🔥 GitHub 热门 Agent 项目 Top 20</div>'''

c = c.replace(old_codex, new_codex)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added LeetCode category and GitHub project practice module')
print(f'New length: {len(c)} chars')
