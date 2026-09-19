p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 加模考设置页、结果页、报告页的 HTML
exam_html = '''
  <!-- 模考设置页 -->
  <div id="page-exam-setup" style="display:none">
    <div class="section-title">宗门大比 · 选择试卷</div>
    <div class="exam-setup">
      <div class="exam-title">选择试炼类别</div>
      <div class="exam-options" id="exam-cats"></div>
    </div>
    <div class="quiz-footer">
      <button class="btn btn-primary" onclick="startExamNow()">开始试炼</button>
    </div>
  </div>

  <!-- 模考结果页 -->
  <div id="page-exam-result" style="display:none">
    <div class="section-title">试炼结果</div>
    <div class="exam-result-card">
      <div class="result-grade" id="result-grade">甲</div>
      <div class="result-score" id="result-score">85</div>
      <div class="result-label">分 · 正确率</div>
      <div class="result-stats">
        <div class="result-stat">
          <div class="result-stat-num" style="color:var(--brand)" id="result-correct">32</div>
          <div class="result-stat-label">答对</div>
        </div>
        <div class="result-stat">
          <div class="result-stat-num" style="color:var(--danger)" id="result-wrong">8</div>
          <div class="result-stat-label">答错</div>
        </div>
        <div class="result-stat">
          <div class="result-stat-num" style="color:var(--brand-2)" id="result-time">42</div>
          <div class="result-stat-label">用时(分钟)</div>
        </div>
      </div>
      <div style="font-size:14px;color:var(--ink-2)" id="result-comment">宗主点评：尚可，继续修炼！</div>
    </div>
    <div class="quiz-footer">
      <button class="btn btn-ghost" onclick="showPage('home', null)">返回首页</button>
      <button class="btn btn-primary" onclick="showPage('wrong', null)">查看错题</button>
    </div>
  </div>

  <!-- 学习报告页 -->
  <div id="page-report" style="display:none">
    <div class="section-title">修炼报告 · 码道人评点</div>
    <div class="report-card">
      <div class="report-title">📊 总览</div>
      <div class="stat-grid">
        <div class="stat-box">
          <div class="stat-box-num" id="report-total">0</div>
          <div class="stat-box-label">累计刷题</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-num" id="report-acc">0%</div>
          <div class="stat-box-label">正确率</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-num" id="report-streak">0</div>
          <div class="stat-box-label">连续天数</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-num" id="report-realm">筑基</div>
          <div class="stat-box-label">当前境界</div>
        </div>
      </div>
    </div>
    <div class="report-card">
      <div class="report-title">🎯 分类掌握度</div>
      <div id="report-cats"></div>
    </div>
    <div class="report-card">
      <div class="report-title">🐛 Bug分布</div>
      <div id="report-wrong-topics"></div>
    </div>
    <div class="report-card">
      <div class="report-title">💪 本周Commit趋势</div>
      <div id="report-weekly"></div>
    </div>
  </div>

'''

# 找排行榜页的位置，插入到它前面
rank_page_start = c.find('<!-- 排行榜页 -->')
if rank_page_start > 0:
    c = c[:rank_page_start] + exam_html + c[rank_page_start:]
    print('Inserted before rank page')
else:
    # 没找到注释，找 page-rank 的位置
    rank_start = c.find('<div id="page-rank"')
    if rank_start > 0:
        c = c[:rank_start] + exam_html + c[rank_start:]
        print('Inserted before page-rank div')
    else:
        print('ERROR: Could not find rank page!')

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')
print(f'New length: {len(c)} chars')
