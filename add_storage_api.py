p = r'D:\download\project\TX-budddy\hacker-edition\server\main.py'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

old = '''# ================================================================
# 启动入口
# ================================================================
if __name__ == "__main__":
    import uvicorn
    _port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=_port, reload=True)'''

new = '''# ================================================================
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
# ================================================================
if __name__ == "__main__":
    import uvicorn
    _port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=_port, reload=True)'''

c = c.replace(old, new)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added storage API endpoints')
print(f'New length: {len(c)} chars')
