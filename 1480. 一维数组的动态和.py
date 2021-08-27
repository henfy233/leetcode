# -*- encoding: utf-8 -*-
'''
@File    :   1480. 一维数组的动态和.py
@Time    :   2021/08/28 00:37:43
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/running-sum-of-1d-array/
'''


from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 自己写，这题是真简单
        # 1. 原地修改
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
        # 复杂度分析
        # 时间复杂度：O(n)，其中 n 是给定数组长度。
        # 空间复杂度：O(1)。我们只需要常数的空间保存若干变量。
        # 执行用时：36 ms, 在所有 Python3 提交中击败了88.92 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.26 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.runningSum(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
