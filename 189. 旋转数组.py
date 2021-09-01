# -*- encoding: utf-8 -*-
'''
@File    :   189. 旋转数组.py
@Time    :   2021/09/01 01:07:20
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/rotate-array/
'''


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # for i in range(1, n+1):
        #     # print(i)
        #     if (k + i) % n == 0:
        #         break
        # for i in range(i):
        #     tmp = nums[0]
        #     nums.pop(0)
        #     nums.append(tmp)
        # # print(nums)
        # return nums

        # 使用临时数组
        # n = len(nums)
        # tmp = [0]*n
        # for i in range(n):
        #     tmp[i] = nums[i]
        # for i in range(n):
        #     nums[(i + k) % n] = tmp[i]
        # return nums

        # 多次反转
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)
        return nums

        # python数组优点
        # k %= len(nums)
        # nums[:] = nums[-k:]+nums[:-k]
        # return nums


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.rotate(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
