# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 57. 和为s的两个数字.py
@Time    :   2022/05/15 00:22:38
@Author  :   henfy
@Diffi   :   Easy
@Method  :   双指针

题目：https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 双指针
        i, j = 0, len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 7, 11, 15], 9, [2, 7]),
        ([10, 26, 30, 31, 47, 60], 40, [10, 30]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.twoSum(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
