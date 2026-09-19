p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 加典籍页 CSS
codex_css = '''
  /* 宗门典籍页 */
  .codex-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
  }
  .codex-title { font-size: 16px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
  .roadmap-item {
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--line);
  }
  .roadmap-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
  .roadmap-stage {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    flex-shrink: 0;
  }
  .roadmap-content { flex: 1; }
  .roadmap-name { font-size: 14px; font-weight: 700; }
  .roadmap-desc { font-size: 12px; color: var(--ink-3); margin-top: 4px; line-height: 1.6; }
  .roadmap-tags { margin-top: 8px; display: flex; gap: 6px; flex-wrap: wrap; }
  .roadmap-tag {
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 999px;
    background: rgba(0,255,136,.1);
    color: var(--brand);
  }
'''

c = c.replace('</style>', codex_css + '</style>')

# 2. 加典籍页 HTML
codex_html = '''
  <!-- 宗门典籍页 -->
  <div id="page-codex" style="display:none">
    <div class="section-title">📜 宗门典籍 · 修炼路线图</div>

    <div class="codex-card">
      <div class="codex-title">⚡ Agent 框架修炼路线</div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(0,255,136,.15);color:var(--brand)">1</div>
        <div class="roadmap-content">
          <div class="roadmap-name">筑基期：轻量入门</div>
          <div class="roadmap-desc">从最简单的单 Agent 开始，理解工具调用、上下文管理、ReAct 循环</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">Smolagents</span>
            <span class="roadmap-tag">OpenAI Agents SDK</span>
            <span class="roadmap-tag">Claude Agent SDK</span>
          </div>
        </div>
      </div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(0,204,255,.15);color:var(--brand-2)">2</div>
        <div class="roadmap-content">
          <div class="roadmap-name">金丹期：多 Agent 协作</div>
          <div class="roadmap-desc">角色分工、任务委派、对话式协作，理解 Crew / Team 模式</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">CrewAI</span>
            <span class="roadmap-tag">AutoGen/AG2</span>
            <span class="roadmap-tag">MetaGPT</span>
          </div>
        </div>
      </div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(168,85,247,.15);color:#a855f7">3</div>
        <div class="roadmap-content">
          <div class="roadmap-name">元婴期：生产级编排</div>
          <div class="roadmap-desc">图状态机、持久化检查点、人在回路、可观测性，生产环境部署</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">LangGraph</span>
            <span class="roadmap-tag">Google ADK</span>
            <span class="roadmap-tag">Pydantic AI</span>
          </div>
        </div>
      </div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(255,184,77,.15);color:var(--warning)">4</div>
        <div class="roadmap-content">
          <div class="roadmap-name">化神期：Harness 定制</div>
          <div class="roadmap-desc">Agent 运行框架定制化，插件系统、多模型路由、沙箱执行</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">DeepSeek Harness</span>
            <span class="roadmap-tag">Claude Code Mods</span>
            <span class="roadmap-tag">MCP 协议</span>
          </div>
        </div>
      </div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(255,107,107,.15);color:var(--danger)">5</div>
        <div class="roadmap-content">
          <div class="roadmap-name">飞升期：RSI 递归自进化</div>
          <div class="roadmap-desc">Agent 自主改进自身、构建记忆、探索环境，自我迭代闭环</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">RSIAgent</span>
            <span class="roadmap-tag">Dream-RSI</span>
            <span class="roadmap-tag">NeoHorse-1</span>
          </div>
        </div>
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🧠 后训练技术修炼路线</div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(0,255,136,.15);color:var(--brand)">1</div>
        <div class="roadmap-content">
          <div class="roadmap-name">推理 RL：从 CoT 到 R1</div>
          <div class="roadmap-desc">SFT 冷启动 → RL 激发推理涌现，Aha Moment 现象</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">GRPO</span>
            <span class="roadmap-tag">DeepSeek-R1</span>
            <span class="roadmap-tag">DAPO</span>
          </div>
        </div>
      </div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(0,204,255,.15);color:var(--brand-2)">2</div>
        <div class="roadmap-content">
          <div class="roadmap-name">OPD：On-Policy 蒸馏</div>
          <div class="roadmap-desc">on-policy 采样 × per-token 蒸馏，信号密度是纯 RL 的 50-100 倍，2026 事实标准</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">MiMo-V2</span>
            <span class="roadmap-tag">GLM-5</span>
            <span class="roadmap-tag">DeepSeek-V4</span>
          </div>
        </div>
      </div>

      <div class="roadmap-item">
        <div class="roadmap-stage" style="background:rgba(168,85,247,.15);color:#a855f7">3</div>
        <div class="roadmap-content">
          <div class="roadmap-name">Agentic RL：多轮长程训练</div>
          <div class="roadmap-desc">工具调用、长程信用分配、多轮对话、异步流水线训练框架</div>
          <div class="roadmap-tags">
            <span class="roadmap-tag">GiGPO</span>
            <span class="roadmap-tag">ARPO</span>
            <span class="roadmap-tag">verl / AReal</span>
          </div>
        </div>
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🎯 八股文 & 算法修炼</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
        <div style="background:rgba(255,255,255,.03);padding:16px;border-radius:12px">
          <div style="font-weight:700;margin-bottom:8px">📚 算法修炼</div>
          <div style="font-size:12px;color:var(--ink-3);line-height:1.8">
            • 数据结构：树/图/哈希/堆<br>
            • 动态规划：背包/区间/状态机<br>
            • 图论：最短路径/拓扑/并查集<br>
            • 复杂度分析 & 贪心
          </div>
        </div>
        <div style="background:rgba(255,255,255,.03);padding:16px;border-radius:12px">
          <div style="font-weight:700;margin-bottom:8px">📖 八股修炼</div>
          <div style="font-size:12px;color:var(--ink-3);line-height:1.8">
            • 计算机网络：TCP/HTTP<br>
            • 操作系统：进程/内存/IO<br>
            • 数据库：索引/事务/锁<br>
            • 设计模式 & 系统设计
          </div>
        </div>
      </div>
    </div>

  </div>
'''

# 插入到知识图谱页之前
km_start = c.find('<div id="page-knowledge"')
if km_start > 0:
    c = c[:km_start] + codex_html + c[km_start:]

# 3. 在首页功能网格加"宗门典籍"入口
old_feat3 = '''      <div class="feature-card" onclick="showPage('knowledge', this)">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">知识图谱</div>
        <div class="feature-desc">修炼版图</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">'''

new_feat3 = '''      <div class="feature-card" onclick="showPage('knowledge', this)">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">知识图谱</div>
        <div class="feature-desc">修炼版图</div>
      </div>
      <div class="feature-card" onclick="showPage('codex', this)">
        <div class="feature-icon">📜</div>
        <div class="feature-title">宗门典籍</div>
        <div class="feature-desc">修炼路线图</div>
      </div>
      <div class="feature-card" onclick="showPage('rank', this)">'''

c = c.replace(old_feat3, new_feat3)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added codex (宗门典籍) page')
print(f'New length: {len(c)} chars')
