#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5850. 找出数组的最大公约数.py
@Time    :   2021/08/22 10:32:47
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

给你一个整数数组 nums ，返回数组中最大数和最小数的 最大公约数 。

两个数的 最大公约数 是能够被两个数整除的最大正整数。

https://leetcode-cn.com/contest/weekly-contest-255/problems/find-greatest-common-divisor-of-array/

解析：https://www.jianshu.com/p/61b25e503811
'''

# here put the import lib
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # 1. 辗转相除法
        # 辗转相除法， 又名欧几里德算法（Euclidean algorithm），是求最大公约数的一种方法。
        # 它的具体做法是：用较小数除较大数，再用出现的余数（第一余数）去除除数，再用出现的余数（第二余数）去除第一余数，如此反复，直到最后余数是0为止。如果是求两个数的最大公约数，那么最后的除数就是这两个数的最大公约数。
        minNum = min(nums)
        maxNum = max(nums)
        # tmp = minNum
        while minNum != 0:
            tmp = minNum
            minNum = maxNum % minNum
            maxNum = tmp
        return maxNum


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 5, 6, 9, 10], 2),
        ([7, 5, 6, 8, 3], 1),
        ([3, 3], 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findGCD(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
