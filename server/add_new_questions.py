import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'coach.db')

# 系统设计 + 数据库 新增题目
NEW_QUESTIONS = [
    # === 系统设计专题 ===
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "设计一个短链接系统，生成短码通常不采用下列哪种方案？", "opts": ["哈希算法如MD5取前6位", "自增ID转62进制", "随机字符串生成", "直接用原URL做短码"], "answer": [3], "explain": "短码必须短且唯一，直接用原URL会很长，完全失去短链接意义。", "topic": "系统设计·短链系统", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "多选题", "stem": "设计一个亿级用户的秒杀系统，下列哪些措施是必要的？（多选）", "opts": ["前端静态化+CDN", "库存预热到Redis", "数据库悲观锁兜底", "直接扣数据库库存"], "answer": [0, 1, 2], "explain": "秒杀必须前端静态化、库存预热Redis、DB锁兜底；直接扣DB扛不住并发。", "topic": "系统设计·秒杀", "difficulty": "hard"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "分布式ID生成方案中，Snowflake算法不包含下列哪个部分？", "opts": ["时间戳", "机器ID", "序列号", "数据库自增ID"], "answer": [3], "explain": "Snowflake由时间戳+机器ID+序列号组成，不依赖数据库自增，保证分布式唯一且趋势递增。", "topic": "系统设计·分布式ID", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "设计一个消息队列系统，保证消息不丢失的关键措施不包括？", "opts": ["生产端确认机制", "Broker持久化", "消费端手动ACK", "开启消息压缩"], "answer": [3], "explain": "消息压缩只是节省带宽/存储，与可靠性无关；生产确认、Broker持久化、手动ACK才是不丢失的关键。", "topic": "系统设计·消息队列", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "多选题", "stem": "缓存穿透、缓存击穿、缓存雪崩的区别，下列说法正确的有？（多选）", "opts": ["穿透是查不存在的数据", "击穿是热点key过期", "雪崩是大量key同时过期", "三者完全一样"], "answer": [0, 1, 2], "explain": "穿透=查不存在数据，击穿=热点key突然失效，雪崩=大面积同时失效；三者成因不同。", "topic": "系统设计·缓存", "difficulty": "hard"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "限流算法中，适合应对突发流量的是？", "opts": ["固定窗口计数器", "滑动窗口", "漏桶算法", "令牌桶算法"], "answer": [3], "explain": "令牌桶允许突发流量，只要桶里有令牌就能处理；漏桶平滑输出，固定窗口有临界问题。", "topic": "系统设计·限流", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "微服务架构中，网关不承担下列哪个职责？", "opts": ["路由转发", "鉴权认证", "服务注册", "限流熔断"], "answer": [2], "explain": "网关负责路由、鉴权、限流、日志；服务注册发现由注册中心（Nacos/Consul）负责。", "topic": "系统设计·微服务", "difficulty": "easy"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "多选题", "stem": "分布式事务常见解决方案有哪些？（多选）", "opts": ["两阶段提交2PC", "TCC（Try-Confirm-Cancel）", "本地消息表+最终一致性", "直接用数据库事务跨服务"], "answer": [0, 1, 2], "explain": "分布式事务常用2PC、TCC、本地消息表、Saga；跨服务不能用本地数据库事务。", "topic": "系统设计·分布式事务", "difficulty": "hard"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "设计一个Feed流系统，关注数远大于粉丝数，适合用哪种模式？", "opts": ["推模式（写扩散）", "拉模式（读扩散）", "推拉结合", "都不行"], "answer": [1], "explain": "大V粉丝多，推模式要写几千次不现实；拉模式在用户查看时实时拉取，适合大V场景。", "topic": "系统设计·Feed流", "difficulty": "hard"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "CAP理论中，分布式注册中心ZooKeeper更偏向哪种选择？", "opts": ["CP（一致性+分区容错）", "AP（可用性+分区容错）", "CA（一致性+可用性）", "三者都满足"], "answer": [0], "explain": "ZooKeeper是CP系统，分区时会拒绝服务保证一致性；Eureka是AP。", "topic": "系统设计·CAP", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "多选题", "stem": "设计一个支付系统，下列哪些是必须考虑的？（多选）", "opts": ["幂等性保证", "对账机制", "异常重试", "直接把用户密码明文存数据库"], "answer": [0, 1, 2], "explain": "支付必须幂等、对账、重试；密码绝不能明文存储。", "topic": "系统设计·支付", "difficulty": "hard"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "设计一个分布式文件系统，小文件问题的典型解决方案是？", "opts": ["每个小文件单独一个块", "小文件合并成大文件块", "拒绝存储小文件", "压缩成zip"], "answer": [1], "explain": "HDFS等对小文件不友好，NameNode元数据压力大；通常把小文件合并成大文件块存储。", "topic": "系统设计·存储", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "搜索引擎倒排索引的核心思想是？", "opts": ["从文档找词", "从词找文档", "按文档ID排序", "按时间排序"], "answer": [1], "explain": "倒排索引是词到文档列表的映射，给定关键词快速找到包含它的所有文档。", "topic": "系统设计·搜索", "difficulty": "medium"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "多选题", "stem": "数据库分库分表后，会带来哪些问题？（多选）", "opts": ["跨库JOIN困难", "分布式ID问题", "分布式事务问题", "单表查询变快"], "answer": [0, 1, 2], "explain": "分库分表解决单表性能，但引入跨库JOIN、分布式ID、分布式事务、跨库排序等复杂度。", "topic": "系统设计·分库分表", "difficulty": "hard"},
    {"cat": "大厂", "src": "系统设计面试题", "type": "单选题", "stem": "设计一个秒杀商品详情页，最合理的静态资源缓存策略是？", "opts": ["每次实时从数据库查", "CDN缓存静态页+Redis缓存商品数据", "直接返回写死的HTML", "用户自己缓存"], "answer": [1], "explain": "静态页走CDN，动态数据走Redis，分层缓存扛住秒杀流量。", "topic": "系统设计·高并发", "difficulty": "medium"},

    # === 数据库专题 ===
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MySQL InnoDB存储引擎，下列哪种索引是聚簇索引？", "opts": ["主键索引", "普通二级索引", "唯一索引", "联合索引"], "answer": [0], "explain": "InnoDB主键就是聚簇索引，数据按主键组织存储；二级索引叶子节点存主键值。", "topic": "数据库·索引", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "多选题", "stem": "下列哪些情况会导致索引失效？（多选）", "opts": ["对索引列做函数运算", "索引列使用!=或<>", "前导模糊查询like '%xx'", "联合索引不满足最左前缀"], "answer": [0, 1, 2, 3], "explain": "函数运算、不等于、前模糊、违反最左前缀，都会导致索引失效。", "topic": "数据库·索引", "difficulty": "hard"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MySQL事务隔离级别中，哪个级别可以避免幻读？", "opts": ["读未提交", "读已提交", "可重复读", "串行化"], "answer": [3], "explain": "标准定义下只有串行化能完全避免幻读；InnoDB RR级别通过间隙锁部分解决。", "topic": "数据库·事务", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MySQL中，DELETE和TRUNCATE的区别，下列说法错误的是？", "opts": ["DELETE可以带WHERE", "TRUNCATE是DDL语句", "TRUNCATE可以回滚", "TRUNCATE重置自增ID"], "answer": [2], "explain": "TRUNCATE是DDL，自动提交不能回滚；DELETE是DML可以回滚，可带条件，不重置自增ID。", "topic": "数据库·SQL", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "B+树索引相比B树索引，下列哪个不是它的优势？", "opts": ["非叶子节点不存数据", "叶子节点链表相连", "查询稳定且范围查询快", "单节点能存更少key"], "answer": [3], "explain": "B+树非叶子不存数据，单节点能存更多key，树更矮IO更少；范围查询靠叶子链表。", "topic": "数据库·索引", "difficulty": "hard"},
    {"cat": "大厂", "src": "数据库面试题", "type": "多选题", "stem": "关于Redis持久化，下列说法正确的有？（多选）", "opts": ["RDB是快照，恢复快", "AOF是日志，数据更安全", "RDB可能丢失最后一次快照后数据", "AOF文件一定比RDB小"], "answer": [0, 1, 2], "explain": "RDB快但可能丢数据，AOF安全但文件通常更大；二者各有优劣，生产常用混合持久化。", "topic": "数据库·Redis", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "Redis的String类型底层编码不包括下列哪种？", "opts": ["int", "embstr", "raw", "list"], "answer": [3], "explain": "String底层有int、embstr、raw三种编码；list是独立的类型。", "topic": "数据库·Redis", "difficulty": "hard"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MySQL慢查询日志排查中，explain看到type=ALL说明？", "opts": ["使用了聚簇索引", "全表扫描", "使用了覆盖索引", "使用了索引范围扫描"], "answer": [1], "explain": "type=ALL是全表扫描，性能最差；type从好到差：system > const > eq_ref > ref > range > index > ALL。", "topic": "数据库·性能优化", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "多选题", "stem": "下列哪些是MySQL主从同步的常见模式？（多选）", "opts": ["异步复制", "半同步复制", "全同步复制", "不需要复制"], "answer": [0, 1, 2], "explain": "MySQL主从有异步、半同步、全同步三种；异步性能高但可能丢数据，全同步最安全但慢。", "topic": "数据库·主从复制", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MVCC多版本并发控制，依赖下列哪个组件实现？", "opts": ["Redo Log", "Undo Log", "Binlog", "Relay Log"], "answer": [1], "explain": "MVCC通过Undo Log保存历史版本，结合Read View实现快照读，解决读写冲突。", "topic": "数据库·MVCC", "difficulty": "hard"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "SQL优化中，避免SELECT *的主要原因是？", "opts": ["写字麻烦", "减少数据传输和内存，可能利用覆盖索引", "语法错误", "数据库不支持"], "answer": [1], "explain": "SELECT *传输多余字段，浪费IO和网络；只查需要的字段，更容易命中覆盖索引，避免回表。", "topic": "数据库·SQL优化", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MySQL行锁与表锁的区别，下列说法正确的是？", "opts": ["行锁粒度大，并发低", "表锁粒度小，并发高", "InnoDB支持行锁，也支持表锁", "MyISAM支持行锁"], "answer": [2], "explain": "InnoDB默认行锁，但也可锁表；MyISAM只有表锁。行锁粒度小并发高，表锁粒度大并发低。", "topic": "数据库·锁", "difficulty": "medium"},
    {"cat": "大厂", "src": "数据库面试题", "type": "多选题", "stem": "下列哪些属于Redis的常见应用场景？（多选）", "opts": ["缓存热点数据", "分布式锁", "排行榜", "持久化存储订单全量数据"], "answer": [0, 1, 2], "explain": "Redis适合缓存、分布式锁、排行榜、计数器；全量订单数据存MySQL，Redis不适合持久化海量数据。", "topic": "数据库·Redis", "difficulty": "easy"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "数据库范式中，第三范式(3NF)要求消除？", "opts": ["部分依赖", "传递依赖", "完全依赖", "主键依赖"], "answer": [1], "explain": "1NF原子性，2NF消除部分依赖，3NF消除传递依赖，BCNF消除主属性对码的部分和传递依赖。", "topic": "数据库·范式", "difficulty": "hard"},
    {"cat": "大厂", "src": "数据库面试题", "type": "单选题", "stem": "MySQL中，undo log和redo log的区别，下列说法正确的是？", "opts": ["undo log是重做日志，redo log是回滚日志", "undo log用于事务回滚和MVCC，redo log用于崩溃恢复", "二者作用完全相同", "redo log保存在表空间"], "answer": [1], "explain": "undo log回滚+MVCC，redo log重做日志保证持久性，崩溃后前滚恢复数据。", "topic": "数据库·日志", "difficulty": "hard"},
]

# 连接数据库
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 获取当前最大ID
cur.execute('SELECT MAX(id) FROM questions')
max_id = cur.fetchone()[0] or 0

print(f'Current max ID: {max_id}')
print(f'Adding {len(NEW_QUESTIONS)} new questions...')

# 插入新题目
for i, q in enumerate(NEW_QUESTIONS):
    qid = max_id + i + 1
    opts_json = json.dumps(q['opts'], ensure_ascii=False)
    answer_json = json.dumps(q['answer'], ensure_ascii=False)

    cur.execute('''
        INSERT INTO questions (id, cat, src, type, stem, opts, answer, explain, topic, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        qid,
        q['cat'],
        q['src'],
        q['type'],
        q['stem'],
        opts_json,
        answer_json,
        q['explain'],
        q['topic'],
        q['difficulty']
    ))

conn.commit()

# 验证
cur.execute('SELECT COUNT(*) FROM questions')
total = cur.fetchone()[0]
print(f'Total questions now: {total}')

cur.execute("SELECT COUNT(*) FROM questions WHERE topic LIKE '%系统设计%' OR topic LIKE '%数据库%'")
sd_count = cur.fetchone()[0]
print(f'System design + DB questions: {sd_count}')

conn.close()
print('Done!')
