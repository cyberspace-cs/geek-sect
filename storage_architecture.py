"""
极客宗 · 多层数据存储架构
=========================
设计目标：高并发刷题 + 向量检索 + 会话缓存 + 持久化

存储层级：
  L1  Redis      → 热数据缓存（每日一题、用户修为、排行榜）
  L2  SQLite    → 持久化主库（错题本、刷题记录、成就）
  L3  Chroma     → 向量检索（知识点语义搜索、相似题推荐）
  L4  Qdrant     → 生产级向量库（扩展用）
  L5  Milvus     → 大规模向量库（扩展用）

ORM：SQLAlchemy 2.0
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict, Any


class StorageTier(str, Enum):
    L1_REDIS = "L1: 热数据缓存"
    L2_SQLITE = "L2: 持久化主库"
    L3_CHROMA = "L3: 向量检索"
    L4_QDRANT = "L4: 生产向量库"
    L5_MILVUS = "L5: 大规模向量库"


@dataclass
class StorageNode:
    name: str
    tier: StorageTier
    use_case: str
    data_type: str
    ttl: Optional[str] = None
    consistency: str = "最终一致"


# 存储架构节点定义
STORAGE_ARCHITECTURE: List[StorageNode] = [
    StorageNode(
        name="Redis",
        tier=StorageTier.L1_REDIS,
        use_case="每日一题、用户修为缓存、排行榜、会话",
        data_type="K-V / Sorted Set / Hash",
        ttl="1h ~ 24h",
        consistency="弱一致",
    ),
    StorageNode(
        name="SQLite + SQLAlchemy",
        tier=StorageTier.L2_SQLITE,
        use_case="错题本、刷题记录、成就系统、用户数据",
        data_type="关系型（用户/题目/错题/成就）",
        consistency="强一致",
    ),
    StorageNode(
        name="Chroma",
        tier=StorageTier.L3_CHROMA,
        use_case="知识点语义搜索、相似题推荐、错题聚类",
        data_type="向量 + 元数据",
        consistency="最终一致",
    ),
    StorageNode(
        name="Qdrant",
        tier=StorageTier.L4_QDRANT,
        use_case="生产级向量检索（高并发）",
        data_type="向量 + Payload 过滤",
        consistency="最终一致",
    ),
    StorageNode(
        name="Milvus",
        tier=StorageTier.L5_MILVUS,
        use_case="十万级以上向量（大规模题库）",
        data_type="分布式向量索引",
        consistency="最终一致",
    ),
]


# 数据读写路径示例
READ_PATHS: Dict[str, List[str]] = {
    "获取每日一题": [
        "L1 Redis 查缓存",
        "→ 命中直接返回",
        "→ 未命中 L2 SQLite 查题目",
        "→ 写回 L1 Redis (TTL 24h)",
    ],
    "提交错题": [
        "L2 SQLite 写错题记录（强一致）",
        "→ L1 Redis 清除用户修为缓存",
        "→ L3 Chroma 存错题向量（异步）",
    ],
    "相似题推荐": [
        "L3 Chroma 向量检索 top_k=10",
        "→ L2 SQLite 补全题目详情",
        "→ L1 Redis 缓存结果 5min",
    ],
    "获取排行榜": [
        "L1 Redis ZSet 直接取 top 100",
        "→ 未命中则从 L2 聚合后写回",
    ],
}


if __name__ == "__main__":
    print("=" * 60)
    print("🏛️  极客宗 · 多层数据存储架构")
    print("=" * 60)
    print()

    for node in STORAGE_ARCHITECTURE:
        print(f"📦 {node.name}")
        print(f"   层级：{node.tier.value}")
        print(f"   用途：{node.use_case}")
        print(f"   数据：{node.data_type}")
        if node.ttl:
            print(f"   TTL：{node.ttl}")
        print(f"   一致性：{node.consistency}")
        print()

    print("=" * 60)
    print("📖 典型读写路径")
    print("=" * 60)
    for action, path in READ_PATHS.items():
        print(f"\n🔹 {action}")
        for step in path:
            print(f"   {step}")
