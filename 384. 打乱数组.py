# -*- encoding: utf-8 -*-
'''
@File    :   384. 打乱数组.py
@Time    :   2021/08/04 15:52:49
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/shuffle-an-array/
'''

import random
from typing import List


# 没做过这种类型的题目，还是直接看答案吧
class Solution(object):
    # 使用整数数组 nums 初始化对象
    def __init__(self, nums: List[int]):
        self.nums = nums

    # 重设数组到它的初始状态并返回
    def reset(self) -> List[int]:
        return self.nums

    # 返回数组随机打乱后的结果
    def shuffle(self) -> List[int]:
        # 调用API
        copy = self.nums[:]
        random.shuffle(copy)
        return copy
    # 执行用时：304 ms, 在所有 Python 提交中击败了94.74 % 的用户
    # 内存消耗：18.7 MB, 在所有 Python 提交中击败了58.48 % 的用户


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
