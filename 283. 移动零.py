# -*- encoding: utf-8 -*-
'''
@File    :   283. 移动零.py
@Time    :   2021/09/01 01:11:14
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/move-zeroes/
'''


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 运行慢，省空间
        # n = len(nums)
        # num = 0
        # for i in range(n):
        #     while nums[i] == 0 and n-num > i:
        #         num += 1
        #         nums.pop(i)
        #         nums.append(0)
        # return nums

        # 把非0的往前挪
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != 0:
                # nums[index], nums[i] = nums[i], nums[index]
                nums[index] = nums[i]
                index += 1
        while index < n:
            nums[index] = 0
            index += 1
        return nums

        # 双指针
        # n = len(nums)
        # left = 0
        # right = n-1
        # while nums[left] == 0:
        #     left += 1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([1, 0, 0, 0, 3, 12, 0], [1, 3, 12, 0, 0, 0, 0]),
        ([1, 0, 0, 0, 3, 12], [1, 3, 12, 0, 0, 0]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.moveZeroes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
