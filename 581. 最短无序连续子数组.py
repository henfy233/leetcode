#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   581. 最短无序连续子数组.py
@Time    :   2021/08/03 01:49:23
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


# 错题,没有思路
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 排序 原数组与排序后数组对比
        # n = len(nums)

        # def isSorted():
        #     for i in range(1, n):
        #         if nums[i-1] > nums[i]:
        #             return False
        #     return True
        # if isSorted():
        #     return 0
        # numsSorted = sorted(nums)
        # left = 0
        # while nums[left] == numsSorted[left]:
        #     left += 1
        # right = n-1
        # while nums[right] == numsSorted[right]:
        #     right -= 1
        # return right - left + 1
        # 执行用时：32 ms, 在所有 Python 提交中击败了99.20 % 的用户
        # 内存消耗：13.9 MB, 在所有 Python 提交中击败了46.59 % 的用户

        # 2. 一次遍历
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        return 0 if right == -1 else right - left + 1
        # 执行用时：36 ms, 在所有 Python 提交中击败了94.78%的用户
        # 内存消耗：13.9 MB, 在所有 Python 提交中击败了52.61%的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 6, 4, 8, 10, 9, 15], 5),
        ([1, 2, 3, 4], 0),
        ([1], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findUnsortedSubarray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
