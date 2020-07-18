# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-07-18   08:41
# 文件名称    : homework01  PY
# 开发工具    : PyCharm

# 删除数组中的重复项
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
# 旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[:][::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums

# 合并链表
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        move = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return dummy.next

# 合并两个有序数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m == 0:
                nums1[n-1] = nums2[n-1]
                n -= 1
                continue
            elif nums1[m-1] < nums2[n-1]:
                nums1[m+n-1], nums2[n-1] = nums2[n-1], nums1[m+n-1]
                n -= 1
            else:
                nums1[m+n-1], nums1[m-1] = nums1[m-1], nums1[m+n-1]
                m -= 1
        return nums1

# 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(target - nums[i]) is not None:
                return [hashmap.get(target - nums[i]), i]
            hashmap[nums[i]] = i

# 移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != 0:
                i += 1
        return nums

# 加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newlst = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        else:
            digits[-1] += 1
            return digits + newlst

# 有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se = set(s)
        if se == set(t):
            for i in se:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False

# 设计双端队列
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.MaxSize = k
        self.deque = []
        self.CurSize = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.CurSize == self.MaxSize:
            return False
        self.deque = [value] + self.deque
        self.CurSize += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.CurSize == self.MaxSize:
            return False
        self.deque.append(value)
        self.CurSize += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.CurSize == 0:
            return False
        self.deque = self.deque[1:]
        self.CurSize -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.CurSize == 0:
            return False
        self.deque.pop()
        self.CurSize -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.CurSize == 0:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.CurSize == 0:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.CurSize == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.CurSize == self.MaxSize



# 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            key = tuple(sorted(i))
            dict[key] = dict.get(key, []) + [i]
        return list(dict.values())

# 接雨水
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        stack = []
        n = len(height)
        res = 0
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    continue
                res += (min(height[i], height[stack[-1]]) - height[top]) * (i - stack[-1] - 1)
            stack.append(i)
        return res

