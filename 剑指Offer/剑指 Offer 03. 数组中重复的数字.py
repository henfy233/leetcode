# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 03. 数组中重复的数字.py
@Time    :   2022/04/25 01:30:34
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
'''


from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 3, 1, 0, 2, 5, 3], 2 or 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findRepeatNumber(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
