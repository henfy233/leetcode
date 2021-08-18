#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   552. 学生出勤记录 II.py
@Time    :   2021/08/18 01:10:55
@Author  :   henfy
@Diffi   :   diff
@Version :   1.0

可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
 - 'A'：Absent，缺勤
 - 'L'：Late，迟到
 - 'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
 - 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
 - 学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。

给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。
答案可能很大，所以返回对 109 + 7 取余 的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


# 这题需要用数学来解，有点烦，排列组合学得不好
class Solution:
    def checkRecord(self, n: int) -> int:
        # 1. 动态规划
        MOD = 10 ** 9+7
        # 长度，A 的数量，结尾连续 L 的数量
        dp = [[[0, 0, 0], [0, 0, 0]]for _ in range(n+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            # 以 P 结尾的数量
            for j in range(0, 2):
                for k in range(0, 3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

            # 以 A 结尾的数量
            for k in range(0, 3):
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

            # 以 L 结尾的数量
            for j in range(0, 2):
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD
        total = 0
        for j in range(0, 2):
            for k in range(0, 3):
                total += dp[n][j][k]

        return total % MOD
        # 注意到 dp[i][][] 只会从 dp[i−1][][] 转移得到。因此可以将 dp 中的总天数的维度省略，将空间复杂度优化到 O(1)。
        # MOD = 10**9 + 7
        # # A 的数量，结尾连续 L 的数量
        # dp = [[0, 0, 0], [0, 0, 0]]
        # dp[0][0] = 1

        # for i in range(1, n + 1):
        #     dpNew = [[0, 0, 0], [0, 0, 0]]

        #     # 以 P 结尾的数量
        #     for j in range(0, 2):
        #         for k in range(0, 3):
        #             dpNew[j][0] = (dpNew[j][0] + dp[j][k]) % MOD

        #     # 以 A 结尾的数量
        #     for k in range(0, 3):
        #         dpNew[1][0] = (dpNew[1][0] + dp[0][k]) % MOD

        #     # 以 L 结尾的数量
        #     for j in range(0, 2):
        #         for k in range(1, 3):
        #             dpNew[j][k] = (dpNew[j][k] + dp[j][k - 1]) % MOD
        #     dp = dpNew

        # total = 0
        # for j in range(0, 2):
        #     for k in range(0, 3):
        #         total += dp[j][k]
        # return total % MOD
        # 复杂度分析
        # 时间复杂度：O(n)。动态规划需要计算 n 天的状态，每天的状态有 2×3 = 6 个，每天的状态需要 O(1) 的时间计算。
        # 空间复杂度：O(1)。使用空间优化的实现，空间复杂度是 O(1)。

        # 2. 矩阵快速幂
        # MOD = 10**9 + 7
        # mat = [
        #     [1, 1, 0, 1, 0, 0],
        #     [1, 0, 1, 1, 0, 0],
        #     [1, 0, 0, 1, 0, 0],
        #     [0, 0, 0, 1, 1, 0],
        #     [0, 0, 0, 1, 0, 1],
        #     [0, 0, 0, 1, 0, 0],
        # ]

        # def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        #     rows, columns, temp = len(a), len(b[0]), len(b)
        #     c = [[0] * columns for _ in range(rows)]
        #     for i in range(rows):
        #         for j in range(columns):
        #             for k in range(temp):
        #                 c[i][j] += a[i][k] * b[k][j]
        #                 c[i][j] %= MOD
        #     return c

        # def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
        #     ret = [[1, 0, 0, 0, 0, 0]]
        #     while n > 0:
        #         if (n & 1) == 1:
        #             ret = multiply(ret, mat)
        #         n >>= 1
        #         mat = multiply(mat, mat)
        #     return ret

        # res = matrixPow(mat, n)
        # ans = sum(res[0])
        # return ans % MOD
        # 复杂度分析
        # 时间复杂度：O(logn)。
        # 空间复杂度：O(1)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 8),
        (1, 3),
        (10101, 183236316),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.checkRecord(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
