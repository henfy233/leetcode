#
# @lc app=leetcode.cn id=1846 lang=python
#
# [1846] 减小和重新排列数组后的最大元素
#
# @lc code=start
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        sl = sorted(arr)
        sl[0] = 1
        for i in range(1,n):
            sl[i] = min(sl[i], sl[i-1] + 1)
        return max(sl)
# @lc code=end

