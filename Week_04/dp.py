# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-09   20:10
# 文件名称    : dp  PY
# 开发工具    : PyCharm

# 最小路径和
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1]+grid[i][j], dp[i-1][j]+grid[i][j])
        return dp[-1][-1]

# 解码方法
class Solution:
    def numDecodings(self, s: str) -> int:
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
        return p

# 最大正方形
class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        res = 0  # 记录结果
        # 定义dp数组，每个元素代表当前位置可以达到的最大的正方形的边长
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return pow(res, 2)

# 回文字串
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        res = len(s)
        dp = [[i,i+1] for i in range(len(s))]
        for i in range(1, len(s)):
            for j in dp[i-1]:
                if j-1 >= 0 and s[j-1] == s[i]:
                    res += 1
                    dp[i].append(j-1)
        return res

# 最长有效括号
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=[]
        stack=[]
        for i in range(len(s)):
            if(stack and s[i]==")"):
                res.append(stack.pop())
                res.append(i)
            if(s[i]=="("):
                stack.append(i)
        #print(res)
        res.sort()
        max_len=0
        i=0
        while(i<len(res)-1):
            tmp=i
            while(i<len(res)-1 and res[i+1]-res[i]==1):
                i+=1
            max_len=max(max_len,i-tmp+1)
            i+=1
        return max_len

# 编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)
        return dp[-1][-1]

