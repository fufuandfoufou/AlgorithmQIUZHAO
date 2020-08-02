学习笔记
### 二分查找一个半有序数组中间无序的地方
**思路：** 类似查找半有序数组中的最小值，返回其下标。
```python
class Solution:
        def search(self, nums: List[int], target: int) -> int:
                l, r = 0, len(nums) - 1
                while l < r:
                        mid = (l + r) // 2
                        if nums[mid] < nums[r]:
                                l = mid + 1
                        else:
                                r = mid
                return nums[l]
```
