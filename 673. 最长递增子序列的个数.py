# -*- encoding: utf-8 -*-
'''
@File    :   673. 最长递增子序列的个数.py
@Time    :   2021/09/20 12:15:08
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
'''


from typing import Callable, List


# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         # 不会做，以为用动规写，还是太难了
#         n = len(nums)
#         res = [[1]*n for _ in range(n+1)]
#         print('res', res)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i] < nums[j]:
#                     res[]

# 1. 动态规划
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/zui-chang-di-zeng-zi-xu-lie-de-ge-shu-by-w12f/
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n, max_len, ans = len(nums), 0, 0
        dp = [0] * n
        cnt = [0] * n
        for i, x in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                ans = cnt[i]  # 重置计数
            elif dp[i] == max_len:
                ans += cnt[i]
        return ans
# 时间复杂度：O(n ^ 2)，其中 n 是数组 nums 的长度。
# 空间复杂度：O(n)。

# 2. 贪心 + 前缀和 + 二分查找
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/zui-chang-di-zeng-zi-xu-lie-de-ge-shu-by-w12f/
# class Solution:
#     def findNumberOfLIS(self, nums: List[int]) -> int:
#         d, cnt = [], []
#         for v in nums:
#             i = bisect(len(d), lambda i: d[i][-1] >= v)
#             c = 1
#             if i > 0:
#                 k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
#                 c = cnt[i - 1][-1] - cnt[i - 1][k]
#             if i == len(d):
#                 d.append([v])
#                 cnt.append([0, c])
#             else:
#                 d[i].append(v)
#                 cnt[i].append(cnt[i][-1] + c)
#         return cnt[-1][-1]


# def bisect(n: int, f: Callable[[int], bool]) -> int:
#     l, r = 0, n
#     while l < r:
#         mid = (l + r) // 2
#         if f(mid):
#             r = mid
#         else:
#             l = mid + 1
#     return l
# 时间复杂度：O(nlogn)，其中 n 是数组 nums 的长度。对 nums 中的每个元素我们需要执行至多两次二分查找，每次耗时 O(logn)，因此时间复杂度为 O(nlogn)。
# 空间复杂度：O(n)。

if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 3, 5, 4, 7], 2),
        ([2, 2, 2, 2, 2], 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findNumberOfLIS(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
