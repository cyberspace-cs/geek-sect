"""
L1 · Redis 热数据缓存层
========================
- 优先使用真实 Redis
- 无 Redis 时降级为内存字典（带 TTL）
- 支持：get / set / delete / expire
"""

import time
import json
import os
from typing import Any, Optional, Dict


class MemoryCache:
    """内存缓存降级实现（模拟 Redis）"""

    def __init__(self):
        self._data: Dict[str, tuple[Any, Optional[float]]] = {}

    def get(self, key: str) -> Optional[str]:
        if key not in self._data:
            return None
        value, expire_at = self._data[key]
        if expire_at and time.time() > expire_at:
            del self._data[key]
            return None
        return value

    def set(self, key: str, value: str, ex: Optional[int] = None):
        expire_at = time.time() + ex if ex else None
        self._data[key] = (value, expire_at)

    def delete(self, key: str):
        if key in self._data:
            del self._data[key]

    def exists(self, key: str) -> bool:
        return self.get(key) is not None

    def flush_all(self):
        self._data.clear()


class RedisCache:
    """真实 Redis 客户端"""

    def __init__(self, url: str):
        import redis
        self._client = redis.from_url(url, decode_responses=True)

    def get(self, key: str) -> Optional[str]:
        return self._client.get(key)

    def set(self, key: str, value: str, ex: Optional[int] = None):
        self._client.set(key, value, ex=ex)

    def delete(self, key: str):
        self._client.delete(key)

    def exists(self, key: str) -> bool:
        return bool(self._client.exists(key))

    def zadd(self, key: str, mapping: Dict[str, float]):
        self._client.zadd(key, mapping)

    def zrange(self, key: str, start: int, end: int, desc: bool = True):
        if desc:
            return self._client.zrevrange(key, start, end, withscores=True)
        return self._client.zrange(key, start, end, withscores=True)


def create_cache():
    """根据环境变量自动选择缓存实现"""
    redis_url = os.getenv("REDIS_URL", "")
    if redis_url:
        try:
            return RedisCache(redis_url)
        except Exception as e:
            print(f"⚠️  Redis 连接失败，降级为内存缓存: {e}")
    return MemoryCache()
