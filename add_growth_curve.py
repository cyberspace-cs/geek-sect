p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 在修炼报告页加成长曲线卡片
old_report_weekly = '''    <div class="report-card">
      <div class="report-title">💪 本周Commit趋势</div>
      <div id="report-weekly"></div>
    </div>
  </div>'''

new_report_weekly = '''    <div class="report-card">
      <div class="report-title">💪 本周Commit趋势</div>
      <div id="report-weekly"></div>
    </div>
    <div class="report-card">
      <div class="report-title">📈 修为成长曲线</div>
      <div id="growth-chart" style="height:150px;display:flex;align-items:flex-end;gap:4px"></div>
      <div style="display:flex;justify-content:space-between;font-size:11px;color:var(--ink-3);margin-top:8px">
        <span>30天前</span>
        <span>现在</span>
      </div>
    </div>
  </div>'''

c = c.replace(old_report_weekly, new_report_weekly)

# 2. 在 loadReport 函数里加成长曲线
old_load_end = '''  document.getElementById('report-weekly').innerHTML = `
    <div style="display:flex;gap:8px;align-items:flex-end;height:100px">${barsHtml}</div>
  `;
}'''

new_load_end = '''  document.getElementById('report-weekly').innerHTML = `
    <div style="display:flex;gap:8px;align-items:flex-end;height:100px">${barsHtml}</div>
  `;

  // 修为成长曲线（模拟30天数据）
  let growthHtml = '';
  let baseExp = Math.max(0, exp - 300);
  for (let i = 29; i >= 0; i--) {
    const d = new Date();
    d.setDate(d.getDate() - i);
    const key = 'geek_done_' + d.toISOString().slice(0,10);
    const todayExp = parseInt(localStorage.getItem(key) || '0') * 10;
    baseExp += todayExp;
    const h = Math.min(100, baseExp / 10);
    const isToday = i === 0;
    growthHtml += `
      <div style="flex:1;height:${Math.max(4, h)}px;background:linear-gradient(180deg, var(--brand), var(--brand-2));border-radius:2px 2px 0 0;${isToday ? 'box-shadow:0 0 8px var(--brand)' : ''}"></div>
    `;
  }
  document.getElementById('growth-chart').innerHTML = growthHtml;
}'''

c = c.replace(old_load_end, new_load_end)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added growth curve feature')
print(f'New length: {len(c)} chars')
