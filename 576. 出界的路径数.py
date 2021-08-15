#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   576. 出界的路径数.py
@Time    :   2021/08/15 09:14:22
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。
你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。
你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。
因为答案可能非常大，返回对 109 + 7 取余 后的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/out-of-boundary-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


# 大学做过这种题，现在不会了，又一次看答案
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        # 自己写，还没通过
        # area = [[0]*n]*m
        # ball = [startRow][startColumn]
        # next = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # count = 0
        # for i in range(1, maxMove+1):
        #     queue = [startRow, startColumn]
        #     while i != 0:
        #         x, y = queue.pop(0)
        #         for j in range(4):
        #             tx = x + next[j][0]
        #             ty = y + next[j][1]
        #             if i == maxMove and (tx == -1 or ty == -1):
        #                 count += 1
        # return count

        # 1. 动态规划
        # 可以使用动态规划计算出界的路径数。
        # 根据上述思路，可以得到时间复杂度和空间复杂度都是 O(maxMove×m×n) 的实现。
        MOD = 10**9 + 7
        outCounts = 0
        # 动态规划的状态由移动次数、行和列决定，定义 dp[i][j][k] 表示球移动 i 次之后位于坐标(j, k) 的路径数量。
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        # 当 i = 0 时，球一定位于起始坐标(startRow, startColumn)，因此动态规划的边界情况是：dp[0][startRow][startColumn] = 1，当(j, k) ≠ (startRow, startColumn) 时有 dp[0][j][k] = 0。
        dp[0][startRow][startColumn] = 1
        # 如果球移动了 i 次之后位于坐标(j, k)，且 i < maxMove，0 ≤ j < m，0 ≤ k < n，则移动第 i+1 次之后，球一定位于和坐标(j, k) 相邻的一个坐标，记为(j', k')。
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            # 当 0 ≤ j′< m 且 0 ≤ k′< n 时，球在移动 i+1 次之后没有出界，将 dp[i][j][k] 的值加到 dp[i+1][j′][k′]；
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1]
                                                     [j1][k1] + dp[i][j][k]) % MOD
                            # 否则，球在第 i+1 次移动之后出界，将 dp[i][j][k] 的值加到出界的路径数。
                            else:
                                outCounts = (outCounts + dp[i][j][k]) % MOD
        # 由于最多可以移动的次数是 maxMove，因此遍历 0 ≤ i < maxMove，根据 dp[i][][] 计算 dp[i+1][][] 的值以及出界的路径数，即可得到最多移动 maxMove 次的情况下的出界的路径数。
        return outCounts
        # 复杂度分析
        # 时间复杂度：O(maxMove×m×n)。动态规划需要遍历的状态数是 O(maxMove×m×n)，对于每个状态，计算后续状态以及出界的路径数的时间都是 O(1)。
        # 空间复杂度：O(m×n)。使用空间优化的实现，空间复杂度是 O(m×n)。
        # 执行用时：72 ms, 在所有 Python 提交中击败了100.00 % 的用户
        # 内存消耗：14.7 MB, 在所有 Python 提交中击败了79.17 % 的用户

        # 注意到 dp[i][][] 只在计算 dp[i+1][][] 时会用到，因此可以将 dp 中的移动次数的维度省略，将空间复杂度优化到 O(m×n)。
        # MOD = 10**9 + 7
        # outCounts = 0
        # dp = [[0] * n for _ in range(m)]
        # dp[startRow][startColumn] = 1
        # for i in range(maxMove):
        #     dpNew = [[0] * n for _ in range(m)]
        #     for j in range(m):
        #         for k in range(n):
        #             if dp[j][k] > 0:
        #                 for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
        #                     if 0 <= j1 < m and 0 <= k1 < n:
        #                         dpNew[j1][k1] = (
        #                             dpNew[j1][k1] + dp[j][k]) % MOD
        #                     else:
        #                         outCounts = (outCounts + dp[j][k]) % MOD
        #     dp = dpNew
        # return outCounts


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 2, 2, 0, 0, 6),
        (1, 3, 3, 0, 1, 12),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findPaths(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
