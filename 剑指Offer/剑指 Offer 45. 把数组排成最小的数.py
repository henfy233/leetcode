# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 45. 把数组排成最小的数.py
@Time    :   2022/05/24 16:32:35
@Author  :   henfy
@Diffi   :   Middle
@Method  :   排序（简单）

题目：https://leetcode.cn/study-plan/lcof/?progress=tc1qtn5
'''


import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 快速排序
        def quick_sort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)

        # 内置函数
        # def sort_rule(x, y):
        #     a, b = x+y, y+x
        #     if a > b:
        #         return 1
        #     elif a < b:
        #         return -1
        #     else:
        #         return 0

        # strs = [str(num) for num in nums]
        # strs.sort(key=functools.cmp_to_key(sort_rule))
        # return ''.join(strs)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([10, 2], "102"),
        ([3, 30, 34, 5, 9], "3033459"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
