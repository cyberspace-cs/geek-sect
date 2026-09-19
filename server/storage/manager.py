"""
极客宗 · 统一存储管理器
=========================
统一管理 L1~L3 存储层
"""

import json
import time
from typing import Any, Optional, Dict

from .cache import create_cache
from .vector import vector_store


class StorageManager:
    """多层存储统一入口"""

    def __init__(self):
        self.cache = create_cache()
        self.vector = vector_store
        self._stats = {
            "cache_hits": 0,
            "cache_misses": 0,
            "db_queries": 0,
        }

    # ---------- L1 缓存层 ----------

    def cache_get(self, key: str) -> Optional[Any]:
        """从 L1 缓存读取"""
        raw = self.cache.get(key)
        if raw is not None:
            self._stats["cache_hits"] += 1
            try:
                return json.loads(raw)
            except:
                return raw
        self._stats["cache_misses"] += 1
        return None

    def cache_set(self, key: str, value: Any, ttl: int = 300):
        """写入 L1 缓存"""
        raw = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
        self.cache.set(key, raw, ex=ttl)

    def cache_delete(self, key: str):
        """删除缓存（写穿）"""
        self.cache.delete(key)

    def cache_invalidate_user(self, user_id: int):
        """失效用户相关缓存"""
        prefixes = [
            f"user:{user_id}:profile",
            f"user:{user_id}:wrong_book",
            f"user:{user_id}:achievements",
            f"user:{user_id}:report",
        ]
        for p in prefixes:
            self.cache.delete(p)

    # ---------- L2 持久化层 ----------

    def db_query(self, query_fn):
        """L2 数据库查询（带统计）"""
        self._stats["db_queries"] += 1
        return query_fn()

    # ---------- L3 向量层 ----------

    def vector_search(self, query: str, top_k: int = 10, cat: Optional[str] = None):
        """L3 向量语义搜索"""
        filter_dict = {"cat": cat} if cat else None
        return self.vector.search_similar(query, top_k=top_k, filter_dict=filter_dict)

    # ---------- 典型业务场景 ----------

    def get_daily_question(self, date_str: str, db_query_fn):
        """
        获取每日一题：
        ① 先查 L1 缓存
        ② 未命中查 L2 DB
        ③ 写回 L1 缓存（TTL 24h）
        """
        key = f"daily:{date_str}"
        cached = self.cache_get(key)
        if cached:
            return cached, "cache"

        question = self.db_query(db_query_fn)
        if question:
            self.cache_set(key, question, ttl=86400)
        return question, "db"

    def get_user_profile(self, user_id: int, db_query_fn):
        """获取用户资料：带缓存"""
        key = f"user:{user_id}:profile"
        cached = self.cache_get(key)
        if cached:
            return cached, "cache"

        profile = self.db_query(db_query_fn)
        if profile:
            self.cache_set(key, profile, ttl=60)
        return profile, "db"

    def get_wrong_book(self, user_id: int, db_query_fn):
        """获取错题本：带缓存"""
        key = f"user:{user_id}:wrong_book"
        cached = self.cache_get(key)
        if cached:
            return cached, "cache"

        book = self.db_query(db_query_fn)
        self.cache_set(key, book, ttl=30)
        return book, "db"

    def invalidate_wrong_book(self, user_id: int):
        """错题变更后失效缓存"""
        self.cache_invalidate_user(user_id)

    # ---------- 统计 ----------

    def get_stats(self):
        """存储层统计信息"""
        total = self._stats["cache_hits"] + self._stats["cache_misses"]
        hit_rate = (self._stats["cache_hits"] / total * 100) if total > 0 else 0
        return {
            **self._stats,
            "cache_hit_rate": f"{hit_rate:.1f}%",
            "vector_count": self.vector.count(),
        }


# 全局单例
storage = StorageManager()
