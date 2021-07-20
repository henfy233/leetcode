#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 暴力破解 自己想的，但超时了
        # flag = nums[0]
        # i = 0
        # for num in nums:
        #     sum = 0
        #     sum += num
        #     if sum > flag:
        #         flag = sum
        #     for num in nums[i+1:]:
        #         print(num)
        #         sum += num
        #         if sum > flag:
        #             flag = sum
        #     i = i+1
        # return flag

        # 2. 当前值 之前和    当前和 最大和 自己写
        #     num  beforeAll nowAll sum
        # beforeAll = 0
        # nowAll = 0
        # flag = None
        # for num in nums:
        #     nowAll = max(num, beforeAll+num)
        #     if not flag:
        #         sum = max(num, nowAll)
        #     else:
        #         sum = max(num, nowAll, beforeAll)
        #     # print("sum=%d", sum)
        #     if sum > flag:
        #         flag = sum
        #     beforeAll = nowAll
        # return flag

        # 2. 动态规划 滚动数组
        # pre = 0
        # maxAns = nums[0]
        # for num in nums:
        #     pre = max(num, pre+num)
        #     maxAns = max(maxAns, pre)
        # return maxAns
        n = len(nums)
        for i in range(1, n):
            # nums[i] = max(nums[i-1]+nums[i], nums[i])
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
# @lc code=end
