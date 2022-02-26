# -*- encoding: utf-8 -*-
'''
@File    :   5869. 两个回文子序列长度的最大乘积.py
@Time    :   2021/09/12 11:14:07
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-258/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
'''


class Solution:
    def maxProduct(self, s: str) -> int:



if __name__ == '__main__':
   s = Solution()
   test_list = [
       (),
   ]

   for test_index, test_case in enumerate(test_list, start=1):
       *test, result = test_case
       test_result = s.maxProduct(*test)
       if test_result != result:
           raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (test_index, result, test_result))
       print("test_case %d succeed." % test_index)
