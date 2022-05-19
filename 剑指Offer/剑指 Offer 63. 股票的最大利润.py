# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 63. 股票的最大利润.py
@Time    :   2022/04/29 13:12:16
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
'''


from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 0:
        #     return 0
        # mi, fo, ans = prices[0], 0, 0
        # for i in range(1, len(prices)):
        #     mi = min(prices[i], mi)
        #     fo = prices[i] - mi
        #     if fo > 0:
        #         ans = max(ans, fo)
        # return ans
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxProfit(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
