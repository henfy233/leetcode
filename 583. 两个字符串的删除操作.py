# -*- encoding: utf-8 -*-
'''
@File    :   583. 两个字符串的删除操作.py
@Time    :   2021/09/25 15:39:27
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/delete-operation-for-two-strings/
'''

# 不会做，没头绪


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. 最长公共子序列
        # https://leetcode-cn.com/problems/delete-operation-for-two-strings/solution/liang-ge-zi-fu-chuan-de-shan-chu-cao-zuo-14uw/
        # m, n = len(word1), len(word2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # lcs = dp[m][n]
        # return m - lcs + n - lcs

        # 2. 动态规划
        # https://leetcode-cn.com/problems/delete-operation-for-two-strings/solution/liang-ge-zi-fu-chuan-de-shan-chu-cao-zuo-14uw/
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("sea", "eat", 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minDistance(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
