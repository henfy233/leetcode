#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   两数之和.py
@Time    :   2021/07/27 20:23:45
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # print(nums)
        d = dict()
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.twoSum(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
