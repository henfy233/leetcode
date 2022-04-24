# -*- encoding: utf-8 -*-
'''
@File    :   398. 随机数索引.py
@Time    :   2022/04/25 00:37:47
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/random-pick-index/
'''
# 不会

from collections import defaultdict
from random import choice, randrange
from typing import List


# 哈希表
class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.pos[target])


# 水塘抽样
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if randrange(cnt) == 0:
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
