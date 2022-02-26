# -*- encoding: utf-8 -*-
'''
@File    :   2016. 增量元素之间的最大差值.py
@Time    :   2022/02/26 12:55:02
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements/
'''


from tkinter import Y
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # 自己做，过了
        # large = -1
        # n = len(nums)
        # print(n)
        # # num = [[0 for _ in range(j)] for j in range(n-1, 0, -1)]
        # # print(num)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         print('i', i, 'j', j)
        #         diff = nums[j] - nums[i]
        #         if diff > large and diff != 0:
        #             # x, y = i, j
        #             large = diff
        # return large

        # 自己写，通过 2021/09/26 10:31:45 之前的竞赛题
        # n = len(nums)
        # ans = float("-inf")
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         tmp = nums[j] - nums[i]
        #         ans = max(ans, tmp)
        # return -1 if ans <= 0 else ans

        # 前缀最小值
        n = len(nums)
        ans, premin = -1, nums[0]

        for i in range(1, n):
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else:
                premin = nums[i]

        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([7, 1, 5, 4], 4),
        ([9, 4, 3, 2], -1),
        ([1, 5, 2, 10], 9),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maximumDifference(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
