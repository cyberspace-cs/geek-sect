p = r'D:\download\project\TX-budddy\hacker-edition\server\main.py'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

old = '''@app.get("/api/questions", response_model=list[QuestionOut])
def list_questions(cat: str | None = None):
    """获取题库列表，可按分类筛选：考研/考公/大厂"""
    conn = get_db()
    if cat and cat != "all":
        rows = conn.execute("SELECT * FROM questions WHERE cat=? ORDER BY id", (cat,)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM questions ORDER BY id").fetchall()
    conn.close()
    return [dict(r) for r in rows]'''

new = '''@app.get("/api/questions", response_model=list[QuestionOut])
def list_questions(cat: str | None = None, limit: int = 50, offset: int = 0):
    """获取题库列表，可按分类筛选：考研/考公/大厂，支持分页"""
    conn = get_db()
    if cat and cat != "all":
        rows = conn.execute("SELECT * FROM questions WHERE cat=? ORDER BY id LIMIT ? OFFSET ?", (cat, limit, offset)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM questions ORDER BY id LIMIT ? OFFSET ?", (limit, offset)).fetchall()
    conn.close()
    return [dict(r) for r in rows]'''

if old in c:
    c = c.replace(old, new)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print('API updated successfully')
else:
    print('Old pattern not found')
