# -*- encoding: utf-8 -*-
'''
@File    :   470. 用 Rand7() 实现 Rand10().py
@Time    :   2021/09/05 00:03:50
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/implement-rand10-using-rand7/
'''
# The rand7() API is already defined for you.


def rand7():
    return 7
# @return a random integer in the range 1 to 7


# 没做过，看到就懵了
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # 1. 拒绝采样
        # https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/yong-rand7-shi-xian-rand10-by-leetcode-s-qbmd/
        # while True:
        #     row = rand7()
        #     col = rand7()
        #     idx = col + (row - 1) * 7
        #     if idx <= 40:
        #         break
        # return 1 + (idx - 1) % 10
        # 时间复杂度：期望时间复杂度为 O(1)，但最坏情况下会达到 O(∞)（一直被拒绝）。
        # 空间复杂度：O(1)。

        # 2. 进阶问题
        while True:
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b
            if idx <= 40:
                return 1 + (idx - 1) % 10
            a = idx - 40
            b = rand7()
            # get uniform dist from 1 - 63
            idx = (a - 1) * 7 + b
            if idx <= 60:
                return 1 + (idx - 1) % 10
            a = idx - 60
            b = rand7()
            # get uniform dist from 1 - 21
            idx = (a - 1) * 7 + b
            if idx <= 20:
                return 1 + (idx - 1) % 10
