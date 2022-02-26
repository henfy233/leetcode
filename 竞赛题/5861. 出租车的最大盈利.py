# -*- encoding: utf-8 -*-
'''
@File    :   5861. 出租车的最大盈利.py
@Time    :   2021/09/18 23:10:03
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-61/problems/maximum-earnings-from-taxi/
'''


from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (5, [[2, 5, 4], [1, 5, 1]], 7),
        (20, [[1, 6, 1], [3, 10, 2], [10, 12, 3], [
         11, 12, 2], [12, 15, 2], [13, 18, 1]], 20),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxTaxiEarnings(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
