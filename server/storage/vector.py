"""
L3 · Chroma 向量检索层
========================
- 知识点语义搜索
- 相似题推荐
- 错题聚类
"""

import os
from typing import List, Dict, Optional


class VectorStore:
    """向量存储层（Chroma 实现）"""

    def __init__(self, persist_dir: str = "./chroma_db"):
        self._client = None
        self._collection = None
        self._persist_dir = persist_dir
        self._initialized = False

    def init(self):
        """懒初始化 Chroma"""
        if self._initialized:
            return

        try:
            import chromadb
            from chromadb.config import Settings

            self._client = chromadb.PersistentClient(
                path=self._persist_dir,
                settings=Settings(anonymized_telemetry=False)
            )
            self._collection = self._client.get_or_create_collection(
                name="questions",
                metadata={"hnsw:space": "cosine"}
            )
            self._initialized = True
            print(f"✅ Chroma 向量库已初始化: {self._collection.count()} 条")
        except ImportError:
            print("⚠️  chromadb 未安装，向量检索降级为 SQL LIKE 搜索")
        except Exception as e:
            print(f"⚠️  Chroma 初始化失败: {e}")

    def add_question(self, q_id: int, text: str, metadata: Dict):
        """添加题目到向量库"""
        if not self._initialized:
            self.init()
            if not self._initialized:
                return

        try:
            self._collection.upsert(
                ids=[str(q_id)],
                documents=[text],
                metadatas=[metadata]
            )
        except Exception as e:
            print(f"⚠️  添加向量失败: {e}")

    def search_similar(self, query: str, top_k: int = 10, filter_dict: Optional[Dict] = None) -> List[Dict]:
        """语义搜索相似题目"""
        if not self._initialized:
            self.init()
            if not self._initialized:
                return []

        try:
            results = self._collection.query(
                query_texts=[query],
                n_results=top_k,
                where=filter_dict
            )
            hits = []
            for i in range(len(results["ids"][0])):
                hits.append({
                    "id": results["ids"][0][i],
                    "text": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i],
                })
            return hits
        except Exception as e:
            print(f"⚠️  向量搜索失败: {e}")
            return []

    def count(self) -> int:
        if not self._initialized:
            return 0
        try:
            return self._collection.count()
        except:
            return 0


# 全局单例
vector_store = VectorStore()
