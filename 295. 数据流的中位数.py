# -*- encoding: utf-8 -*-
'''
@File    :   295. 数据流的中位数.py
@Time    :   2021/08/27 09:52:51
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/find-median-from-data-stream/

进阶:
- 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
- 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
'''
from sortedcontainers import SortedList
# import SortedList
import heapq


# 可先做 1046 简单题
# 自己写，超出时间限制
class MedianFinder0:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)
        print('n', n)
        print('arr', self.arr)
        if n % 2 == 0:
            ans = (self.arr[n//2] + self.arr[n//2-1])/2
        else:
            ans = self.arr[n//2]
        return ans


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 1. 优先队列
# https://leetcode-cn.com/problems/find-median-from-data-stream/solution/shu-ju-liu-de-zhong-wei-shu-by-leetcode-ktkst/
class MedianFinder1:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2

# 复杂度分析
# 时间复杂度：
#   addNum: O(logn)，其中 n 为累计添加的数的数量。
#   findMedian: O(1)。
# 空间复杂度：O(n)，主要为优先队列的开销。
# 执行用时：384 ms, 在所有 Python3 提交中击败了60.03 %的用户
# 内存消耗：34.8 MB, 在所有 Python3 提交中击败了29.97%的用户


# 2. 有序集合 + 双指针
# https://leetcode-cn.com/problems/find-median-from-data-stream/solution/shu-ju-liu-de-zhong-wei-shu-by-leetcode-ktkst/
class MedianFinder2:

    def __init__(self):
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num: int) -> None:
        nums_ = self.nums

        n = len(nums_)
        nums_.add(num)

        if n == 0:
            self.left = self.right = 0
        else:
            # 模拟双指针，当 num 小于 self.left 或 self.right 指向的元素时，num 的加入会导致对应指针向右移动一个位置
            if num < self.left_value:
                self.left += 1
            if num < self.right_value:
                self.right += 1

            if n & 1:
                if num < self.left_value:
                    self.left -= 1
                else:
                    self.right += 1
            else:
                if self.left_value < num < self.right_value:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_value:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right

        self.left_value = nums_[self.left]
        self.right_value = nums_[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value) / 2
# 复杂度分析
# 时间复杂度：
#   addNum: O(logn)，其中 n 为累计添加的数的数量。
#   findMedian: O(1)。
# 空间复杂度：O(n)，主要为有序数组的开销。


# 进阶 1
# 如果数据流中所有整数都在 0 到 100 范围内，那么我们可以利用计数排序统计每一类数的数量，并使用双指针维护中位数。

# 进阶 2
# 如果数据流中 99 % 的整数都在 0 到 100 范围内，那么我们依然利用计数排序统计每一类数的数量，并使用双指针维护中位数。对于超出范围的数，我们可以单独进行处理，建立两个数组，分别记录小于 0 的部分的数的数量和大于 100 的部分的数的数量即可。当小部分时间，中位数不落在区间[0, 100] 中时，我们在对应的数组中暴力检查即可。
