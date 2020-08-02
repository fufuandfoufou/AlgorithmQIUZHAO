# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-08-02   14:46
# 文件名称    : work3  PY
# 开发工具    : PyCharm

# Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            return self.myPow(x*x, n//2) if n % 2 == 0 else x * self.myPow(x*x, n//2)

# 子集
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(level, tmp):
            if level == len(nums):
                res.append(tmp.copy())
                return
            helper(level+1, tmp+[nums[level]])
            helper(level+1, tmp)
        helper(0, [])
        return res
# 电话号码的字母组合
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"],
                    "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        res = []
        if not digits:
            return []
        def helper(level, digit, tmp):
            if level == len(digits):
                res.append(tmp)
                return
            for i in digit:
                for j in hashmap[i]:
                    helper(level+1, digit[1:], tmp+j)
                break
        helper(0, digits, "")
        return res
# 岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    cur_pos = collections.deque()
                    cur_pos.append([i, j])
                    while cur_pos:
                        x, y = cur_pos.popleft()
                        for new_x, new_y in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                            if 0<= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                cur_pos.append([new_x, new_y])
        return count

# N皇后
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        s = "." * n

        def helper(level, tmp, col, z, f):
            if level == n:
                res.append(tmp)
                return
            for i in range(n):
                if i not in col and i + level not in z and i - level not in f:
                    helper(level + 1, tmp + [s[:i] + "Q" + s[i + 1:]], col | {i}, z | {i + level}, f | {i - level})

        helper(0, [], set(), set(), set())
        return res

# 跳跃游戏二
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        step = 0
        max_bound = 0
        for i in range(len(nums)-1):
            max_bound = max(max_bound, i+nums[i])
            if i >= end and max_bound >= end:
                step += 1
                end = max_bound
        return step