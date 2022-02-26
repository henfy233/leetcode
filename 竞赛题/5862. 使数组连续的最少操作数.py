# -*- encoding: utf-8 -*-
'''
@File    :   5862. 使数组连续的最少操作数.py
@Time    :   2021/09/18 23:18:45
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-61/problems/minimum-number-of-operations-to-make-array-continuous/
'''


from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([4, 2, 5, 3], 0),
        ([1, 2, 3, 5, 6], 1),
        ([1, 10, 100, 1000], 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minOperations(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
