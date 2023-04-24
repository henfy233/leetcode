# -*- encoding: utf-8 -*-
'''
@File    :   121.买卖股票的最佳时机.py
@Time    :   2021/08/29 16:14:33
@Author  :   henfy
@Diffi   :   Easy
@Method  :   暴力法、遍历
@Question:   https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
@Answer1 :   https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
@Answer2 :   https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
'''

from math import inf
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        # 1. 暴力法，两个for循环遍历最大利润
        # ans = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         ans = max(ans, prices[j] - prices[i])
        # return ans

        # 2. 一次遍历
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxProfit(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
