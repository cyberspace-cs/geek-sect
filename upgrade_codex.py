p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 找到宗门典籍页，在末尾加新的卡片
old_codex_end = '''    <div class="codex-card">
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

  </div>'''

new_codex_end = '''    <div class="codex-card">
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
          <div style="font-weight:700;margin-bottom:8px">📖 数据库八股</div>
          <div style="font-size:12px;color:var(--ink-3);line-height:1.8">
            • 索引：B+树/聚簇/覆盖/最左前缀<br>
            • 事务：ACID/MVCC/隔离级别<br>
            • 锁：行锁/表锁/间隙锁<br>
            • Redis：持久化/数据结构/分布式锁
          </div>
        </div>
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🏗️ 系统设计思维修炼</div>
      <div style="font-size:13px;line-height:1.8;color:var(--ink-2);margin-bottom:16px">
        系统设计不是背答案，而是<b>从需求到架构的推导过程</b>。掌握以下思维模型：
      </div>

      <div style="background:rgba(0,255,136,.05);padding:16px;border-radius:12px;margin-bottom:12px">
        <div style="font-weight:700;color:var(--brand);margin-bottom:8px">📐 四步设计法</div>
        <div style="font-size:12px;color:var(--ink-3);line-height:1.8">
          1. <b>需求澄清</b>：功能需求 + 非功能需求（QPS/延迟/可用性）<br>
          2. <b>容量估算</b>：读QPS/写QPS/存储量/带宽<br>
          3. <b>高层设计</b>：客户端→网关→服务→存储，画核心组件<br>
          4. <b>深入设计</b>：选数据结构、设计API、扩展性、容错
        </div>
      </div>

      <div style="background:rgba(0,204,255,.05);padding:16px;border-radius:12px;margin-bottom:12px">
        <div style="font-weight:700;color:var(--brand-2);margin-bottom:8px">🔑 核心设计权衡</div>
        <div style="font-size:12px;color:var(--ink-3);line-height:1.8">
          • <b>CAP</b>：分布式系统选CP还是AP？<br>
          • <b>缓存 vs DB</b>：读多写少用缓存，写多了要考虑一致性<br>
          • <b>同步 vs 异步</b>：同步简单但慢，异步快但复杂<br>
          • <b>强一致 vs 最终一致</b>：金融要强一致，社交可以最终一致
        </div>
      </div>

      <div style="background:rgba(255,184,77,.05);padding:16px;border-radius:12px">
        <div style="font-weight:700;color:var(--warning);margin-bottom:8px">🧩 必练经典题</div>
        <div style="font-size:12px;color:var(--ink-3);line-height:1.8">
          1. 设计短链接系统<br>
          2. 设计秒杀系统<br>
          3. 设计Feed流（微博/朋友圈）<br>
          4. 设计分布式ID生成器<br>
          5. 设计限流器<br>
          6. 设计排行榜（Redis ZSet）<br>
          7. 设计消息队列<br>
          8. 设计文件系统（网盘）<br>
          9. 设计支付系统<br>
          10. 设计分布式爬虫
        </div>
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🔥 2026 热门开源项目贡献路线</div>
      <div style="font-size:13px;line-height:1.8;color:var(--ink-2);margin-bottom:16px">
        从 Good First Issue 开始，逐步深入核心模块，每贡献一个PR都是一次修为提升！
      </div>

      <div style="background:rgba(0,255,136,.05);padding:16px;border-radius:12px;margin-bottom:12px">
        <div style="font-weight:700;color:var(--brand);margin-bottom:8px">🌱 入门级（适合刚上手）</div>
        <div style="font-size:12px;color:var(--ink-3);line-height:2">
          • <b>Dify</b>（144K星）：低代码Agent平台，文档完善，issue友好<br>
          • <b>Langflow</b>：可视化LLM流程编排，前端/文档任务多<br>
          • <b>Flowise</b>：拖拽式AI workflow，TS项目，适合前端同学<br>
          • <b>Awesome-LLM</b>：各种教程、示例项目，先从写文档开始
        </div>
      </div>

      <div style="background:rgba(0,204,255,.05);padding:16px;border-radius:12px;margin-bottom:12px">
        <div style="font-weight:700;color:var(--brand-2);margin-bottom:8px">⚔️ 进阶级（有一定基础）</div>
        <div style="font-size:12px;color:var(--ink-3);line-height:2">
          • <b>LangGraph</b>（34M月下载）：生产级Agent编排，图状态机<br>
          • <b>CrewAI</b>：多Agent协作框架，角色分工模式<br>
          • <b>AutoGen/AG2</b>：微软多Agent框架，研究向<br>
          • <b>Smolagents</b>：HuggingFace极简Agent，代码量小易读
        </div>
      </div>

      <div style="background:rgba(168,85,247,.05);padding:16px;border-radius:12px">
        <div style="font-weight:700;color:#a855f7;margin-bottom:8px">🚀 前沿级（挑战RSI方向）</div>
        <div style="font-size:12px;color:var(--ink-3);line-height:2">
          • <b>DeepSeek Harness</b>（229K星）：一切皆插件的Agent运行框架<br>
          • <b>OpenClaw</b>（390K星）：最火的OSS Agent框架<br>
          • <b>RSIAgent</b>：递归自进化Agent框架，学术+工业结合<br>
          • <b>browser-use</b>：浏览器自动化Agent，115K星，方向火
        </div>
      </div>
    </div>

  </div>'''

c = c.replace(old_codex_end, new_codex_end)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Upgraded codex with system design thinking and GitHub project guide')
print(f'New length: {len(c)} chars')
