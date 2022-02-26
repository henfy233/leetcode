# -*- encoding: utf-8 -*-
'''
@File    :   1984. 学生分数的最小差值.py
@Time    :   2022/02/11 18:56:16
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
'''


from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 题例误解
        # if len(nums) == 1:
        #     return 0
        # imax = nums[0]
        # length = len(nums)
        # for x in range(length-1):
        #     # print('x', nums[x])
        #     for y in range(x+1, length):
        #         # print('y', nums[y])
        #         diff = abs(nums[x] - nums[y])
        #         print('diff', diff)
        #         if diff < imax:
        #             imax = diff
        # return imax

        # 错漏百出
        # if len(nums) == 1:
        #     return 0
        # nums = sorted(nums)
        # length = len(nums)
        # print(nums[length-1])
        # print(nums[length - k])
        # return nums[length-1] - nums[length - k]

        # 参考答案
        nums = sorted(nums)
        length = len(nums)
        return min(nums[i+k-1]-nums[i] for i in range(length-k+1))


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([90], 1, 0),
        ([9, 4, 1, 7], 2, 2),
        ([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6, 74560)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minimumDifference(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
