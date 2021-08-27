# -*- encoding: utf-8 -*-
'''
@File    :   1838.最高频元素的频数.py
@Time    :   2021/07/19 00:45:20
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/
'''
from typing import List


class Solution(object):
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        l = 0
        sum = 1
        for r in range(1, n):
            total += (nums[r] - nums[r-1]) * (r-l)
            # print(total)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            sum = max(sum, r-l+1)
        return sum


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 4], 5, 3),
        ([1, 4, 8, 13], 5, 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxFrequency(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
