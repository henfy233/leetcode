#
# @lc app=leetcode.cn id=1838 lang=python
#
# [1838] 最高频元素的频数
#

# @lc code=start
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        total = 0
        l = 0
        sum = 1
        for r in range(1, n):
            total += (nums[r] - nums[r-1]) * (r-l)
            print(total)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            sum = max(sum, r-l+1)
        return sum
# @lc code=end
