#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   移动零.py
@Time    :   2021/07/24 23:23:33
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 自己做错
        # print(nums)
        # n = len(nums)
        # i = 0
        # while nums[i] == 0:
        #     i += 1
        # nums = nums[-(n-i):] + [0]*i
        # return nums

        # 双指针
        n = len(nums)
        left = 0
        right = n-1
        while nums[left] == 0:
            left += 1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.moveZeroes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
