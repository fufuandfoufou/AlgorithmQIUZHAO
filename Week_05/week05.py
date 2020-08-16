#!/usr/bin/env python

# 爬楼梯
class Solution:
def climbStairs(self, n: int) -> int:
    if n == 1: return 1
    if n == 2: return 2
    dp = [1] * (n+1)
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
    
    
# 位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count
            
# 2的幂
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

# 实现Trie（前缀树）
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True


# 朋友圈
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        p = [i for i in range(len(M))]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    a = find(i)
                    b = find(j)
                    p[a] = b
        print(p)
        for i in range(len(M)):
            find(i)
        return len(set(p))

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
