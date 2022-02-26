# -*- encoding: utf-8 -*-
'''
@File    :   LCP 07. 传递信息.py
@Time    :   2021/09/03 00:47:39
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/chuan-di-xin-xi/
'''


from typing import List
import collections


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # 这题有点难，这是简单题？
        # arr = [[]*n]
        # print(arr)
        # for i in range(len(relation)):
        #     arr[relation[i][0]][relation[i][1]] += 1
        # print(arr)
        # i = 1

        # def dfs(arr, depth):
        #     if depth == k:
        #         return 0

        # dfs(arr, 0)

        # 1. 深度优先搜索
        # https://leetcode-cn.com/problems/chuan-di-xin-xi/solution/chuan-di-xin-xi-by-leetcode-solution/
        #     self.ways, self.n, self.k = 0, n, k
        #     self.edges = collections.defaultdict(list)
        #     for src, dst in relation:
        #         self.edges[src].append(dst)
        #     self.dfs(0, 0)
        #     return self.ways
        # def dfs(self, index, steps):
        #     if steps == self.k:
        #         if index == self.n-1:
        #             self.ways += 1
        #         return
        #     for to in self.edges[index]:
        #         self.dfs(to, steps+1)
        # 时间复杂度：O(n ^ k)。最多需要遍历 k 层，每层遍历最多有 O(n) 个分支。
        # 空间复杂度：O(n+m+k)。其中 m 为 relation 数组的长度。空间复杂度主要取决于图的大小和递归调用栈的深度，保存有向图信息所需空间为 O(n+m)，递归调用栈的深度不会超过 k。
        # 执行用时：44 ms, 在所有 Python3 提交中击败了68.28 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了83.78 % 的用户

        # 2. 广度优先搜索
        # https://leetcode-cn.com/problems/chuan-di-xin-xi/solution/chuan-di-xin-xi-by-leetcode-solution/
        # edges = collections.defaultdict(list)
        # for edge in relation:
        #     src = edge[0]
        #     dst = edge[1]
        #     edges[src].append(dst)
        # steps = 0
        # queue = collections.deque([0])
        # while queue and steps < k:
        #     steps += 1
        #     size = len(queue)
        #     for i in range(size):
        #         index = queue.popleft()
        #         to = edges[index]
        #         for nextIndex in to:
        #             queue.append(nextIndex)
        # ways = 0
        # if steps == k:
        #     while queue:
        #         if queue.popleft() == n - 1:
        #             ways += 1
        # return ways
        # 时间复杂度：O(n ^ k)。最多需要遍历 kk 层，每层遍历最多有 O(n) 个分支。
        # 空间复杂度：O(n+m+n ^ k)。其中 m 为 relation 数组的长度。空间复杂度主要取决于图的大小和队列的大小，保存有向图信息所需空间为 O(n+m)，由于每层遍历最多有 O(n) 个分支，因此遍历到 k 层时，队列的大小为 O(n ^ k)。

        # 3.1 动态规划
        # https://leetcode-cn.com/problems/chuan-di-xin-xi/solution/chuan-di-xin-xi-by-leetcode-solution/
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(k):
            for edge in relation:
                src = edge[0]
                dst = edge[1]
                dp[i + 1][dst] += dp[i][src]
        print(dp)
        return dp[k][n - 1]

        # 3.2 动态规划
        # dp = [0 for _ in range(n + 1)]
        # dp[0] = 1
        # for i in range(k):
        #     next = [0 for _ in range(n + 1)]
        #     for edge in relation:
        #         src = edge[0]
        #         dst = edge[1]
        #         next[dst] += dp[src]
        #     dp = next
        # return dp[n - 1]
        # 时间复杂度：O(km)。其中 m 为 =relation 数组的长度。
        # 空间复杂度：O(n)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (5, [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], 3, 3),
        (3, [[0, 2], [2, 1]], 2, 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numWays(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
