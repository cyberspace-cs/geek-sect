import sqlite3
conn = sqlite3.connect('/home/ubuntu/shuati-coach/server/coach.db')
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM questions")
print("Total questions:", c.fetchone()[0])
c.execute("SELECT cat, COUNT(*) FROM questions GROUP BY cat")
print("By category:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]}")
c.execute("SELECT * FROM questions LIMIT 1")
print("\nSample question columns:")
print([desc[0] for desc in c.description])
