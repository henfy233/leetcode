#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 自己想，对比最大利润 有点复杂
        # inf = int(1e9)
        # minprice = inf
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            print(minprice)
            if price < minprice:
                minprice = price
                continue
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit
        # 暴力法，两个for循环遍历最大利润
        # ans = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         ans = max(ans, prices[j] - prices[i])
        # return ans

        # 一次遍历
        # inf = int(1e9)
        # minprice = inf
        # maxprofit = 0
        # for price in prices:
        #     maxprofit = max(price - minprice, maxprofit)
        #     minprice = min(price, minprice)
        # return maxprofit

# @lc code=end
