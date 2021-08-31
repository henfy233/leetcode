# -*- encoding: utf-8 -*-
'''
@File    :   198. 打家劫舍.py
@Time    :   2021/08/30 23:39:55
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/house-robber/
'''


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 没头绪，但知道是用动规来做
        # n = len(nums)
        # arr = [0] * (n+1)
        # arr[1] = nums[0]
        # arr[2] = max(nums[0], nums[1])
        # for i in range(3, n+1):
        #     arr[n] =

        # 1. 动态规划
        # https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-by-leetcode-solution/
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        # dp = [0] * size
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, size):
        #     dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # return dp[size - 1]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        return second
        # 时间复杂度：O(n)，其中 n 是数组长度。只需要对数组遍历一次。
        # 空间复杂度：O(1)。使用滚动数组，可以只存储前两间房屋的最高总金额，而不需要存储整个数组的结果，因此空间复杂度是 O(1)。
        # 执行用时：32 ms, 在所有 Python3 提交中击败了74.06 % 的用户
        # 内存消耗：14.7 MB, 在所有 Python3 提交中击败了94.57 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.rob(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
