p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

old = """    const res = await fetch(API + '/api/questions?cat=' + cat);
    const data = await res.json();
    // 解析 opts 和 answer 的 JSON 字符串
    currentQuestions = data.map(q => ({
      ...q,
      opts: typeof q.opts === 'string' ? JSON.parse(q.opts) : q.opts,
      answer: typeof q.answer === 'string' ? JSON.parse(q.answer) : q.answer
    }));
    currentQIndex = 0;
    renderQuestion();"""

new = """    const res = await fetch(API + '/api/questions/sample?cat=' + cat + '&limit=30');
    const data = await res.json();
    // 解析 opts 和 answer 的 JSON 字符串
    currentQuestions = data.map(q => ({
      ...q,
      opts: typeof q.opts === 'string' ? JSON.parse(q.opts) : q.opts,
      answer: typeof q.answer === 'string' ? JSON.parse(q.answer) : q.answer
    }));
    currentQIndex = 0;
    renderQuestion();"""

if old in c:
    c = c.replace(old, new)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Frontend updated to use sample API')
else:
    print('Pattern not found')
