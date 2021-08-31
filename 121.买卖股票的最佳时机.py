# -*- encoding: utf-8 -*-
'''
@File    :   121.买卖股票的最佳时机.py
@Time    :   2021/08/29 16:14:33
@Author  :   henfy
@Diffi   :   Easy
@Version :   2.0

题目：https: // leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''

from math import inf
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        # 自己想，对比最大利润 最近做又忘了
        minP = inf
        maxP = 0
        for price in prices:
            minP = min(minP, price)
            maxP = max(maxP, price - minP)
        return maxP

        # 1. 暴力法，两个for循环遍历最大利润
        # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
        # ans = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         ans = max(ans, prices[j] - prices[i])
        # return ans
        # 时间复杂度：O(n ^ 2)。循环运行 (n*(n−1))/2 次。
        # 空间复杂度：O(1)。只使用了常数个变量。

        # 2. 一次遍历
        # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
        # inf = int(1e9)
        # minprice = inf
        # maxprofit = 0
        # for price in prices:
        #     maxprofit = max(price - minprice, maxprofit)
        #     minprice = min(price, minprice)
        # return maxprofit
        # 时间复杂度：O(n)，只需要遍历一次。
        # 空间复杂度：O(1)。只使用了常数个变量。


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
