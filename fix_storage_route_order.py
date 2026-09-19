p = r'D:\download\project\TX-budddy\hacker-edition\server\main.py'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 先把末尾的 storage 代码删掉
old_storage_block = '''
# ================================================================
# 极客宗 · 多层存储层 API
# ================================================================
from storage import storage

@app.get("/api/storage/stats")
def storage_stats():
    """获取多层存储层运行状态"""
    stats = storage.get_stats()
    has_redis = hasattr(storage.cache, '_client')
    return {
        "tiers": {
            "L1_redis": "✅ 运行中 (真实 Redis)" if has_redis else "⚡ 内存缓存（降级）",
            "L2_sqlite": "✅ 运行中 (SQLite 持久化)",
            "L3_chroma": f"🔮 已初始化 ({stats['vector_count']} 条向量)" if stats['vector_count'] > 0 else "💤 未初始化（懒加载）",
        },
        "stats": stats,
        "architecture": [
            {"tier": "L1", "name": "Redis", "use_case": "热数据缓存"},
            {"tier": "L2", "name": "SQLite", "use_case": "持久化主库"},
            {"tier": "L3", "name": "Chroma", "use_case": "向量检索"},
        ]
    }

@app.post("/api/storage/warmup")
def storage_warmup():
    """预热向量库"""
    storage.vector.init()
    return {"ok": True, "message": "向量库已初始化"}


# ================================================================
# 启动入口
# ================================================================'''

c = c.replace(old_storage_block, '''
# ================================================================
# 启动入口
# ================================================================''', 1)

# 把 storage 代码加到 mount 之前
old_mount = '''_STATIC_DIR = os.getenv("STATIC_DIR", os.path.dirname(DB_DIR))
app.mount("/", StaticFiles(directory=_STATIC_DIR, html=True), name="static")'''

new_mount = '''
# ================================================================
# 极客宗 · 多层存储层 API
# ================================================================
from storage import storage

@app.get("/api/storage/stats")
def storage_stats():
    """获取多层存储层运行状态"""
    stats = storage.get_stats()
    has_redis = hasattr(storage.cache, '_client')
    return {
        "tiers": {
            "L1_redis": "✅ 运行中 (真实 Redis)" if has_redis else "⚡ 内存缓存（降级）",
            "L2_sqlite": "✅ 运行中 (SQLite 持久化)",
            "L3_chroma": f"🔮 已初始化 ({stats['vector_count']} 条向量)" if stats['vector_count'] > 0 else "💤 未初始化（懒加载）",
        },
        "stats": stats,
        "architecture": [
            {"tier": "L1", "name": "Redis", "use_case": "热数据缓存"},
            {"tier": "L2", "name": "SQLite", "use_case": "持久化主库"},
            {"tier": "L3", "name": "Chroma", "use_case": "向量检索"},
        ]
    }

@app.post("/api/storage/warmup")
def storage_warmup():
    """预热向量库"""
    storage.vector.init()
    return {"ok": True, "message": "向量库已初始化"}


_STATIC_DIR = os.getenv("STATIC_DIR", os.path.dirname(DB_DIR))
app.mount("/", StaticFiles(directory=_STATIC_DIR, html=True), name="static")'''

c = c.replace(old_mount, new_mount)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed: moved storage routes before StaticFiles mount')
print(f'New length: {len(c)} chars')
