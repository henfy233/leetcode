# -*- encoding: utf-8 -*-
'''
@File    :   5866. 数组的最大公因数排序.py
@Time    :   2021/09/05 11:15:42
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-257/problems/gcd-sort-of-an-array/
'''


from typing import List


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.gcdSort(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
