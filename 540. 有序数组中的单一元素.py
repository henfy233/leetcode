# -*- encoding: utf-8 -*-
'''
@File    :   540. 有序数组中的单一元素.py
@Time    :   2022/02/14 01:23:27
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/single-element-in-a-sorted-array/
'''


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 时间复杂度超了
        # total = 0
        # for i, x in enumerate(nums):
        #     # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         total += x
        #     else:
        #         total -= x
        # return total

        # 全数组的二分查找
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            # print('mid', mid)
            # print('mid ^ 1', mid ^ 1)
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.singleNonDuplicate(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
