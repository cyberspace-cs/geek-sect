"""
极客宗 · 多层数据存储层
=========================
L1: Redis 热缓存（降级为内存字典）
L2: SQLite + SQLAlchemy 持久化
L3: Chroma 向量检索
"""

from .manager import StorageManager, storage

__all__ = ["StorageManager", "storage"]
