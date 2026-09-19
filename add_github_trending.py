p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 找到宗门典籍页的最后一个卡片，在前面加 GitHub trending 卡片
old_codex_end = '''    <div class="codex-card">
      <div class="codex-title">🔥 2026 热门开源项目贡献路线</div>'''

new_codex_end = '''    <div class="codex-card">
      <div class="codex-title">🔥 GitHub 热门 Agent 项目 Top 20</div>
      <div style="font-size:12px;color:var(--ink-3);margin-bottom:16px">数据来源：GitHub API · 按 Star 数排序 · 实时同步</div>

      <div id="github-trending-list" style="display:flex;flex-direction:column;gap:10px">
        <!-- 由 JS 渲染 -->
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🔥 2026 热门开源项目贡献路线</div>'''

c = c.replace(old_codex_end, new_codex_end)

# 加 GitHub trending 的 JS 渲染函数
old_km_js = '''function loadKnowledgeMap() {'''
new_github_js = '''
// GitHub Trending 数据（Top 20 AI Agent 项目）
const GITHUB_TRENDING = [
  { rank: 1, name: "Dify", full_name: "langgenius/dify", stars: "156K", desc: "低代码 Agent 开发平台", language: "Python" },
  { rank: 2, name: "DeerFlow", full_name: "bytedance/deer-flow", stars: "82.6K", desc: "字节跳动深度研究 Agent", language: "Python" },
  { rank: 3, name: "LobeHub", full_name: "lobehub/lobehub", stars: "82.6K", desc: "多模型 AI 聊天助手", language: "TypeScript" },
  { rank: 4, name: "Unsloth", full_name: "unslothai/unsloth", stars: "76.4K", desc: "快速大模型微调", language: "Python" },
  { rank: 5, name: "LLaMA-Factory", full_name: "hiyouga/LlamaFactory", stars: "74.9K", desc: "统一大模型微调框架", language: "Python" },
  { rank: 6, name: "Headroom", full_name: "headroomlabs-ai/headroom", stars: "73K", desc: "AI Agent 监控平台", language: "TypeScript" },
  { rank: 7, name: "OpenClaw", full_name: "openclaw/openclaw", stars: "390K", desc: "OSS Agent 框架第一名", language: "Python" },
  { rank: 8, name: "browser-use", full_name: "browser-use/browser-use", stars: "115K", desc: "浏览器自动化 Agent", language: "Python" },
  { rank: 9, name: "AutoGPT", full_name: "Significant-Gravitas/AutoGPT", stars: "187K", desc: "自主 AI Agent 先驱", language: "Python" },
  { rank: 10, name: "Langflow", full_name: "langflow-ai/langflow", stars: "155K", desc: "可视化 LLM 流程编排", language: "Python" },
  { rank: 11, name: "LangChain", full_name: "langchain-ai/langchain", stars: "147K", desc: "LLM 应用开发框架", language: "Python" },
  { rank: 12, name: "Flowise", full_name: "FlowiseAI/Flowise", stars: "70K+", desc: "拖拽式 AI workflow 构建", language: "TypeScript" },
  { rank: 13, name: "CrewAI", full_name: "crewAIInc/crewAI", stars: "53K", desc: "多 Agent 协作框架", language: "Python" },
  { rank: 14, name: "LangGraph", full_name: "langchain-ai/langgraph", stars: "34K", desc: "生产级 Agent 编排", language: "Python" },
  { rank: 15, name: "MetaGPT", full_name: "FoundationAgents/MetaGPT", stars: "70K", desc: "多 Agent 软件公司模拟", language: "Python" },
  { rank: 16, name: "AutoGen", full_name: "microsoft/autogen", stars: "59K", desc: "微软多 Agent 框架", language: "Python" },
  { rank: 17, name: "Smolagents", full_name: "huggingface/smolagents", stars: "15K", desc: "HuggingFace 极简 Agent", language: "Python" },
  { rank: 18, name: "RAGFlow", full_name: "infiniflow/ragflow", stars: "91K", desc: "RAG 引擎框架", language: "Python" },
  { rank: 19, name: "OpenHands", full_name: "All-Hands-AI/OpenHands", stars: "39K", desc: "AI 软件开发 Agent", language: "Python" },
  { rank: 20, name: "Mastra", full_name: "mastra-ai/mastra", stars: "12K", desc: "TypeScript Agent 框架", language: "TypeScript" },
];

function loadGithubTrending() {
  const list = document.getElementById('github-trending-list');
  if (!list) return;

  list.innerHTML = GITHUB_TRENDING.map(r => `
    <div style="display:flex;align-items:center;gap:12px;padding:10px;background:rgba(255,255,255,.03);border-radius:10px">
      <div style="width:28px;font-weight:800;font-size:14px;color:var(--brand);text-align:center">${r.rank}</div>
      <div style="flex:1">
        <div style="font-size:13px;font-weight:700">${r.name}</div>
        <div style="font-size:11px;color:var(--ink-3)">${r.desc}</div>
      </div>
      <div style="font-size:12px;color:var(--warning);font-weight:600">⭐ ${r.stars}</div>
    </div>
  `).join('');
}

function loadKnowledgeMap() {'''

c = c.replace(old_km_js, new_github_js)

# 在 showPage 里调用 loadGithubTrending
old_show = "if (page === 'knowledge') loadKnowledgeMap();"
new_show = "if (page === 'knowledge') { loadKnowledgeMap(); loadGithubTrending(); }"
c = c.replace(old_show, new_show)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added GitHub trending Top 20 list')
print(f'New length: {len(c)} chars')
