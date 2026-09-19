p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. 在我的页面（或者首页）加 GitHub 绑定卡片
# 先在首页境界卡下面加一个 GitHub 绑定卡片
old_realm_end = '''      <div class="realm-desc" id="realm-desc">初入极客宗，Hello World 入门</div>
    </div>'''

new_realm_end = '''      <div class="realm-desc" id="realm-desc">初入极客宗，Hello World 入门</div>
    </div>

    <div class="realm-card" style="border-color: rgba(139,92,246,.2); background: rgba(139,92,246,.05)">
      <div class="realm-top">
        <div class="realm-badge" style="border-color:#8b5cf6; color:#8b5cf6; background:rgba(139,92,246,.1)">🔗 GitHub 同步</div>
        <div class="realm-exp" id="github-status">未绑定</div>
      </div>
      <div style="display:flex;gap:12px;align-items:center;margin-bottom:12px">
        <input type="text" id="github-username" placeholder="输入你的 GitHub 用户名" style="flex:1;padding:10px 14px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);font-size:14px;outline:none">
        <button class="btn btn-primary" style="flex:0;padding:10px 20px;font-size:13px" onclick="syncGithub()">同步</button>
      </div>
      <div class="realm-desc">绑定 GitHub 后，你的 PR 数将自动转换成 Commit 修为</div>
    </div>'''

c = c.replace(old_realm_end, new_realm_end)

# 2. 加 GitHub 同步 JS
github_js = '''
async function syncGithub() {
  const username = document.getElementById('github-username').value.trim();
  if (!username) {
    alert('请输入 GitHub 用户名！');
    return;
  }
  try {
    // 调用 GitHub API 获取用户公开 PR 数
    const res = await fetch(`https://api.github.com/search/issues?q=author:${username}+type:pr`);
    const data = await res.json();
    const prCount = data.total_count || 0;

    // 保存绑定信息
    localStorage.setItem('geek_github_user', username);
    localStorage.setItem('geek_github_pr_count', prCount);

    // 计算修为奖励：每个 PR 加 5 修为
    const oldPrCount = parseInt(localStorage.getItem('geek_github_pr_old') || '0');
    const newPrReward = (prCount - oldPrCount) * 5;
    if (newPrReward > 0) {
      exp += newPrReward;
      localStorage.setItem('geek_exp', exp);
      showToast(`同步成功！+${newPrReward} 修为（${prCount} 个 PR）`);
    } else {
      showToast(`同步成功！共 ${prCount} 个 PR`);
    }
    localStorage.setItem('geek_github_pr_old', prCount);

    document.getElementById('github-status').textContent = '@' + username;
    renderHome();
  } catch (e) {
    alert('GitHub 同步失败：' + e.message);
  }
}

function checkGithubBinding() {
  const username = localStorage.getItem('geek_github_user');
  if (username) {
    document.getElementById('github-status').textContent = '@' + username;
    document.getElementById('github-username').value = username;
  }
}
'''

# 插入到 checkDailyStatus 函数之后
c = c.replace('async function startDailyQuestion()', github_js + '\nasync function startDailyQuestion()')

# 3. 在初始化时调用 checkGithubBinding
old_init = 'renderHome();\nrenderCats();\ncheckDailyStatus();'
new_init = 'renderHome();\nrenderCats();\ncheckDailyStatus();\ncheckGithubBinding();'
c = c.replace(old_init, new_init)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added GitHub PR sync feature')
print(f'New length: {len(c)} chars')
