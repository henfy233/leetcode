#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   516. 最长回文子序列.py
@Time    :   2021/08/12 01:32:39
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

来源：力扣（LeetCode）
链接：https: // leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# here put the import lib


# 最近做题真是人傻了，都不会，这个我想到双指针，一头一尾，相同就下一个，可是怎么取舍
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1 动态规划
        # 对于一个子序列而言，如果它是回文子序列，并且长度大于 2，那么将它首尾的两个字符去除之后，它仍然是个回文子序列。因此可以用动态规划的方法计算给定字符串的最长回文子序列。
        n = len(s)
        # 用 dp[i][j] 表示字符串 ss 的下标范围[i, j] 内的最长回文子序列的长度。假设字符串 s 的长度为 n，则只有当 0≤i≤j < n 时，才会有 dp[i][j] > 0，否则 dp[i][j] = 0。
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            # 由于任何长度为 1 的子序列都是回文子序列，因此动态规划的边界情况是，对任意 0 ≤ i < n，都有 dp[i][i] = 1。
            dp[i][i] = 1
            # 由于状态转移方程都是从长度较短的子序列向长度较长的子序列转移，因此需要注意动态规划的循环顺序。
            for j in range(i + 1, n):
                # 当 i < j 时，计算 dp[i][j] 需要分别考虑 s[i] 和 s[j] 相等和不相等的情况：
                # - 如果 s[i] = s[j]，则首先得到 s 的下标范围[i+1, j−1] 内的最长回文子序列，然后在该子序列的首尾分别添加 s[i]和 s[j]，即可得到 s 的下标范围[i, j] 内的最长回文子序列，因此 dp[i][j] = dp[i+1][j−1]+2；
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # - 如果 s[i] ≠ s[j]，则 s[i] 和 s[j]不可能同时作为同一个回文子序列的首尾，因此 dp[i][j] = max(dp[i+1][j], dp[i][j−1])。
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 最终得到 dp[0][n−1] 即为字符串 s 的最长回文子序列的长度。
        return dp[0][n - 1]
        # 复杂度分析
        # 时间复杂度：O(n ^ 2)，其中 n 是字符串 s 的长度。动态规划需要计算的状态数是 O(n ^ 2)。
        # 空间复杂度：O(n ^ 2)，其中 n 是字符串 s 的长度。需要创建二维数组 dp，空间是 O(n ^ 2)。
        # 执行用时：888 ms, 在所有 Python 提交中击败了78.86 % 的用户
        # 内存消耗：27.7 MB, 在所有 Python 提交中击败了51.22 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("bbbab", 4),
        ("cbbd", 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.longestPalindromeSubseq(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
