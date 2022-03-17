# -*- encoding: utf-8 -*-
'''
@File    :   2104. 子数组范围和.py
@Time    :   2022/03/04 02:06:55
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/sum-of-subarray-ranges/
'''


from math import inf
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # 有问题
        # nums.sort()
        # print(nums)
        # sum = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i, n):
        #         # if j-i > 3:
        #         #     sum += (nums[j]-nums[i]) * (j-i-1)
        #         #     print('diff', nums[j]-nums[i] * (j-i-1))
        #         # else:
        #         sum += nums[j]-nums[i]
        #         print('diff', nums[j]-nums[i])
        # print('sum', sum)
        # return sum

        # 遍历子数组
        # nums.sort()
        ans, n = 0, len(nums)
        for i in range(n):
            minVal, maxVal = inf, -inf
            for j in range(i, n):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                ans += maxVal - minVal
                # ans += nums[j] - nums[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3], 4),
        ([1, 3, 3], 4),
        ([4, -2, -3, 4, 1], 59)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.subArrayRanges(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
