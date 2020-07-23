# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-07-23   19:39
# 文件名称    : homwork02  PY
# 开发工具    : PyCharm

# N叉树的后序遍历
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            top = stack.pop()
            res.append(top.val)
            for i in top.children:
                stack.append(i)
        return res[::-1]

# N叉树的前序遍历
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        if not root:
            return []
        while stack:
            top = stack.pop()
            res.append(top.val)
            for i in top.children[::-1]:
                stack.append(i)
        return res

# 二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            res.append(top.val)
            cur = top.right
        return res

# 二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            cur = top.right
        return res

# N叉树的层序遍历
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            child = []
            node = []
            for i in stack:
                if i.children: node += i.children
                child.append(i.val)
            res.append(child)
            stack = node
        return res

# 丑数
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1, n):
            n1, n2, n3 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1: a += 1
            if dp[i] == n2: b += 1
            if dp[i] == n3: c += 1
        return dp[-1]

# 前K个高频元素
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        heap = []
        ans = []
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for i in dict:
            heapq.heappush(heap, (-dict[i], i))
        for i in range(k):
            top = heapq.heappop(heap)
            ans.append(top[1])
        return ans

# 二叉树的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
# 从前序与中序遍历序列构造二叉树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root
# 组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def com(depth, nums, k, res, path, start):
            if depth == k:
                res.append(path.copy())
                return
            for i in range(start, n + 1):
                path.append(i)
                com(depth + 1, n, k, res, path, i + 1)
                path.pop()

        res = []
        com(0, n, k, res, [], 1)
        return res
# 全排列
lass Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def pre(depth, size, path, res, used, nums):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    pre(depth+1, size, path, res, used, nums)
                    used[i] = False
                    path.pop()
        res = []
        size = len(nums)
        used = [False for i in range(size)]
        pre(0, size, [], res, used, nums)
        return res

# 全排列二
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def pre(depth, size, path, res, used, nums):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    pre(depth+1, size, path, res, used, nums)
                    used[i] = False
                    path.pop()
        res = []
        size = len(nums)
        used = [False for i in range(size)]
        nums.sort()
        pre(0, size, [], res, used, nums)
        return res