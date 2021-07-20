#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1.暴力破解
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 1.5 暴力破解
        # n = len(nums)
        # for i in range(n):
        #     if target - nums[i] in nums:
        #         j = nums.index(target - nums[i])
        #         if(j != i):
        #             break
        # if(j > i):
        #     return [i, j]
        # else:
        #     return [j, i]

        # 2.哈希表
        hashmap = dict()

        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i

# @lc code=end
