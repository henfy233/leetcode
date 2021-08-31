# -*- encoding: utf-8 -*-
'''
@File    :   528. 按权重随机选择.py
@Time    :   2021/08/30 00:07:11
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/random-pick-with-weight/
'''


from typing import List
from itertools import accumulate
import random
import bisect


class Solution:

    # def __init__(self, w: List[int]):
    #     self.w = w
    #     print(self.w)
    #     self.sumI = sum(self.w)

    # # 不知道概率怎么输出，还是直接看答案吧
    # def pickIndex(self) -> int:
    #     # sumI = sum(self.w)
    #     print('sumI', self.sumI)
    #     return

    # 1.前缀和 + 二分查找
    # https://leetcode-cn.com/problems/random-pick-with-weight/solution/an-quan-zhong-sui-ji-xuan-ze-by-leetcode-h13t/
    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect.bisect_left(self.pre, x)
    # 时间复杂度：初始化的时间复杂度为 O(n)，每次选择的时间复杂度为 O(logn)，其中 n 是数组 w 的长度。
    # 空间复杂度：O(n)，即为前缀和数组 pre 需要使用的空间。

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
