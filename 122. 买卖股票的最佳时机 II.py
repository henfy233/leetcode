# -*- encoding: utf-8 -*-
'''
@File    :   122. 买卖股票的最佳时机 II.py
@Time    :   2021/08/31 23:48:22
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
'''


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法解决
        res = 0
        n = len(prices)
        for i in range(1, n):
            diff = prices[i]-prices[i-1]
            if diff > 0:
                res += diff
        return res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxProfit(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
