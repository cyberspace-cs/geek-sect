p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 在宗门典籍页最顶部加存储架构卡片
old_codex = '''    <div class="codex-card">
      <div class="codex-title">🛠️ GitHub 项目修炼（刷项目 = 真实 Commit）</div>'''

new_codex = '''    <div class="codex-card">
      <div class="codex-title">🏛️ 系统设计：极客宗数据存储架构</div>
      <div style="font-size:12px;color:var(--ink-3);margin-bottom:16px">五层存储 · 读写分离 · 冷热分离 · 面试必考</div>

      <!-- 存储层级图 -->
      <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:20px">

        <div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(255,107,107,.08);border-left:3px solid var(--danger);border-radius:0 8px 8px 0">
          <div style="font-size:20px">⚡</div>
          <div style="flex:1">
            <div style="font-size:13px;font-weight:700">L1 · Redis 热数据缓存</div>
            <div style="font-size:11px;color:var(--ink-3);margin-top:2px">每日一题 · 用户修为 · 排行榜 · 会话 · TTL 1h~24h</div>
          </div>
          <div style="font-size:11px;color:var(--danger);font-weight:600">弱一致</div>
        </div>

        <div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(0,255,136,.08);border-left:3px solid var(--brand);border-radius:0 8px 8px 0">
          <div style="font-size:20px">🗄️</div>
          <div style="flex:1">
            <div style="font-size:13px;font-weight:700">L2 · SQLite + SQLAlchemy 持久化主库</div>
            <div style="font-size:11px;color:var(--ink-3);margin-top:2px">错题本 · 刷题记录 · 成就系统 · 用户数据 · ORM 2.0</div>
          </div>
          <div style="font-size:11px;color:var(--brand);font-weight:600">强一致</div>
        </div>

        <div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(0,204,255,.08);border-left:3px solid var(--accent);border-radius:0 8px 8px 0">
          <div style="font-size:20px">🔮</div>
          <div style="flex:1">
            <div style="font-size:13px;font-weight:700">L3 · Chroma 向量检索（本地）</div>
            <div style="font-size:11px;color:var(--ink-3);margin-top:2px">知识点语义搜索 · 相似题推荐 · 错题聚类 · Embedding</div>
          </div>
          <div style="font-size:11px;color:var(--accent);font-weight:600">最终一致</div>
        </div>

        <div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(255,193,7,.08);border-left:3px solid var(--warning);border-radius:0 8px 8px 0">
          <div style="font-size:20px">🚀</div>
          <div style="flex:1">
            <div style="font-size:13px;font-weight:700">L4 · Qdrant 生产级向量库</div>
            <div style="font-size:11px;color:var(--ink-3);margin-top:2px">高并发向量检索 · Payload 过滤 · 生产环境替换 Chroma</div>
          </div>
          <div style="font-size:11px;color:var(--warning);font-weight:600">最终一致</div>
        </div>

        <div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(156,39,176,.08);border-left:3px solid #9c27b0;border-radius:0 8px 8px 0">
          <div style="font-size:20px">🌌</div>
          <div style="flex:1">
            <div style="font-size:13px;font-weight:700">L5 · Milvus 大规模向量库</div>
            <div style="font-size:11px;color:var(--ink-3);margin-top:2px">十万级以上向量 · 分布式索引 · 超大规模题库</div>
          </div>
          <div style="font-size:11px;color:#9c27b0;font-weight:600">最终一致</div>
        </div>

      </div>

      <!-- 典型读写路径 -->
      <div style="margin-bottom:16px">
        <div style="font-size:14px;font-weight:700;margin-bottom:10px">📖 典型读写路径</div>

        <div style="background:rgba(255,255,255,.03);border-radius:8px;padding:10px;margin-bottom:8px">
          <div style="font-size:12px;font-weight:700;margin-bottom:6px">🔹 获取每日一题</div>
          <div style="font-size:11px;color:var(--ink-2);line-height:1.8">
            ① Redis 查缓存 → 命中直接返回<br>
            ② 未命中 → SQLite 查题目<br>
            ③ 写回 Redis（TTL 24h）
          </div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:8px;padding:10px;margin-bottom:8px">
          <div style="font-size:12px;font-weight:700;margin-bottom:6px">🔹 提交错题</div>
          <div style="font-size:11px;color:var(--ink-2);line-height:1.8">
            ① SQLite 写错题记录（强一致）<br>
            ② Redis 清除用户修为缓存<br>
            ③ Chroma 存错题向量（异步）
          </div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:8px;margin-bottom:8px;padding:10px">
          <div style="font-size:12px;font-weight:700;margin-bottom:6px">🔹 相似题推荐</div>
          <div style="font-size:11px;color:var(--ink-2);line-height:1.8">
            ① Chroma 向量检索 top_k=10<br>
            ② SQLite 补全题目详情<br>
            ③ Redis 缓存结果 5min
          </div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:8px;padding:10px">
          <div style="font-size:12px;font-weight:700;margin-bottom:6px">🔹 获取排行榜</div>
          <div style="font-size:11px;color:var(--ink-2);line-height:1.8">
            ① Redis ZSet 直接取 top 100<br>
            ② 未命中 → SQLite 聚合后写回
          </div>
        </div>
      </div>

      <!-- 面试要点 -->
      <div style="padding:12px;background:rgba(0,204,255,.05);border-radius:8px">
        <div style="font-size:13px;font-weight:700;color:var(--accent);margin-bottom:8px">💡 面试加分点</div>
        <ul style="font-size:12px;color:var(--ink-2);line-height:1.8;padding-left:16px;margin:0">
          <li>为什么用 Redis？ → 高并发、低延迟、支持 ZSet 排序</li>
          <li>为什么用向量库？ → 语义搜索比 LIKE 快 100 倍</li>
          <li>缓存穿透怎么办？ → 布隆过滤器 / 空值缓存</li>
          <li>缓存击穿怎么办？ → 互斥锁 / 永不过期</li>
          <li>缓存雪崩怎么办？ → 随机 TTL / 多级缓存</li>
        </ul>
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🛠️ GitHub 项目修炼（刷项目 = 真实 Commit）</div>'''

c = c.replace(old_codex, new_codex)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added storage architecture card')
print(f'New length: {len(c)} chars')
