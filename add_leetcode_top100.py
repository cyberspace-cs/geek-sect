p = r'D:\download\project\TX-budddy\hacker-edition\geek.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# 在 GitHub 项目修炼后面加力扣 Top100 算法题典
old_codex = '''    <div class="codex-card">
      <div class="codex-title">🔥 GitHub 热门 Agent 项目 Top 20</div>'''

new_codex = '''    <div class="codex-card">
      <div class="codex-title">📚 力扣 Top 100 算法题典（必刷经典）</div>
      <div style="font-size:12px;color:var(--ink-3);margin-bottom:16px">面试高频 · 每道题都有思路+复杂度分析 · 看完就能写代码</div>

      <!-- 二分查找 -->
      <div style="margin-bottom:20px">
        <div style="font-size:14px;font-weight:700;color:var(--brand);margin-bottom:10px">🔍 二分查找系列</div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#704 二分查找</div>
            <div style="font-size:11px;color:var(--brand);background:rgba(0,255,136,.1);padding:2px 8px;border-radius:10px">简单</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：有序数组找目标值，每次砍一半</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(log n) &nbsp;&nbsp; 💾 空间：O(1)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 模板：left=0, right=len-1, while left<=right</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#33 搜索旋转排序数组</div>
            <div style="font-size:11px;color:var(--warning);background:rgba(255,193,7,.1);padding:2px 8px;border-radius:10px">中等</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：二分 + 判断哪一半是有序的</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(log n) &nbsp;&nbsp; 💾 空间：O(1)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 关键：mid 和 left 比较，确定有序区间</div>
        </div>
      </div>

      <!-- 双指针 -->
      <div style="margin-bottom:20px">
        <div style="font-size:14px;font-weight:700;color:var(--accent);margin-bottom:10px">👯 双指针系列</div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#1 两数之和</div>
            <div style="font-size:11px;color:var(--brand);background:rgba(0,255,136,.1);padding:2px 8px;border-radius:10px">简单</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 解法1：哈希表 O(n) · 解法2：双指针 O(n log n)</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) &nbsp;&nbsp; 💾 空间：O(n)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 哈希表法：边遍历边查 target - x 是否在表里</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#15 三数之和</div>
            <div style="font-size:11px;color:var(--warning);background:rgba(255,193,7,.1);padding:2px 8px;border-radius:10px">中等</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：排序 + 固定一个数 + 双指针找另外两个</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n²) &nbsp;&nbsp; 💾 空间：O(1)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 去重：跳过相同的 nums[i], nums[left], nums[right]</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#206 反转链表</div>
            <div style="font-size:11px;color:var(--brand);background:rgba(0,255,136,.1);padding:2px 8px;border-radius:10px">简单</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：三个指针 prev, curr, next，逐个翻转</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) &nbsp;&nbsp; 💾 空间：O(1)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 递归法也能写，但迭代法面试更稳</div>
        </div>
      </div>

      <!-- 动态规划 -->
      <div style="margin-bottom:20px">
        <div style="font-size:14px;font-weight:700;color:var(--warning);margin-bottom:10px">🧮 动态规划系列</div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#70 爬楼梯</div>
            <div style="font-size:11px;color:var(--brand);background:rgba(0,255,136,.1);padding:2px 8px;border-radius:10px">简单</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：斐波那契数列 dp[i] = dp[i-1] + dp[i-2]</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) · 可优化到 O(log n) · 💾 空间：O(1)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 状态压缩：只用两个变量存前两个状态</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#121 买卖股票的最佳时机</div>
            <div style="font-size:11px;color:var(--brand);background:rgba(0,255,136,.1);padding:2px 8px;border-radius:10px">简单</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：遍历，维护历史最低价，每天算最大利润</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) &nbsp;&nbsp; 💾 空间：O(1)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 本质：dp[i] = max(dp[i-1], price[i] - min_price)</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#300 最长递增子序列</div>
            <div style="font-size:11px;color:var(--danger);background:rgba(255,107,107,.1);padding:2px 8px;border-radius:10px">困难</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 解法1：DP O(n²) · 解法2：二分+贪心 O(n log n)</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n log n) &nbsp;&nbsp; 💾 空间：O(n)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 二分法：维护一个 tails 数组，tails[i] 是长度 i+1 的最小尾元素</div>
        </div>
      </div>

      <!-- 二叉树 -->
      <div style="margin-bottom:20px">
        <div style="font-size:14px;font-weight:700;color:var(--danger);margin-bottom:10px">🌳 二叉树系列</div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#144 二叉树的前序遍历</div>
            <div style="font-size:11px;color:var(--brand);background:rgba(0,255,136,.1);padding:2px 8px;border-radius:10px">简单</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 解法1：递归 · 解法2：迭代（栈）</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) &nbsp;&nbsp; 💾 空间：O(n)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 模板：根 → 左 → 右，栈法压右再压左</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#102 二叉树的层序遍历</div>
            <div style="font-size:11px;color:var(--warning);background:rgba(255,193,7,.1);padding:2px 8px;border-radius:10px">中等</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：BFS 队列，每层记录当前层的 size</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) &nbsp;&nbsp; 💾 空间：O(n)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 模板：while queue: size = len(queue)，循环 size 次</div>
        </div>

        <div style="background:rgba(255,255,255,.03);border-radius:10px;padding:12px;margin-bottom:10px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <div style="font-size:13px;font-weight:700">#236 二叉树的最近公共祖先</div>
            <div style="font-size:11px;color:var(--warning);background:rgba(255,193,7,.1);padding:2px 8px;border-radius:10px">中等</div>
          </div>
          <div style="font-size:12px;color:var(--ink-2);margin:6px 0">💡 思路：后序遍历，左右分别找 p 和 q</div>
          <div style="font-size:12px;color:var(--ink-3)">
            ⏱ 时间：O(n) &nbsp;&nbsp; 💾 空间：O(h)
          </div>
          <div style="font-size:12px;color:var(--accent);margin-top:6px">💡 递归：if root == p or root == q: return root</div>
        </div>
      </div>

      <div style="text-align:center;font-size:12px;color:var(--ink-3);margin-top:16px">
        📖 更多题目去 leetcode.cn/problemset/ 刷吧
      </div>
    </div>

    <div class="codex-card">
      <div class="codex-title">🔥 GitHub 热门 Agent 项目 Top 20</div>'''

c = c.replace(old_codex, new_codex)

# 确保首页的修炼卡片显示正常
# 检查 home-cards 的样式
old_home_css = '''.home-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}'''

new_home_css = '''.home-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: 20px;
  visibility: visible;
  opacity: 1;
}'''

c = c.replace(old_home_css, new_home_css)

with open(p, 'w', encoding='utf-8') as f:
    f.write(c)

print('Added LeetCode Top 100 classic problems with detailed solutions')
print(f'New length: {len(c)} chars')
