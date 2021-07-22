#
# @lc app=leetcode.cn id=1877 lang=python
#
# [1877] 数组中最大数对和的最小值
#

# @lc code=start
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 循环一半数组
        # nums.sort()
        # n = len(nums)
        # # li = []
        # res = 0
        # for i in range(n//2):
        #     # print(nums[i]+nums[n-i-1])
        #     # li.append(nums[i]+nums[n-i-1])
        #     res = max(res, nums[i]+nums[n-i-1])
        # return res

        # 双指针解题
        nums.sort()
        left, right, res = 0, len(nums)-1, 0
        while left < right:
            res = max(res, nums[left] + nums[right])
            left += 1
            right -= 1
        return res

# @lc code=end
