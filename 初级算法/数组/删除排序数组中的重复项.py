#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   删除排序数组中的重复项.py
@Time    :   2021/07/27 23:57:37
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 双指针
        # n = len(nums)
        # i = 0
        # for j in range(1, n):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        # return i+1

        # python逆序删除
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.removeDuplicates(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
