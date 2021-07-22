class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        n = len(prices)
        for i in range(1, n):
            diff = prices[i]-prices[i-1]
            if diff > 0:
                res += diff
        return res
