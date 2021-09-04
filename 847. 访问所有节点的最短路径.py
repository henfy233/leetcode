#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   847. 访问所有节点的最短路径.py
@Time    :   2021/08/06 00:12:37
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes/
'''


from typing import List

# 没做过这种题，直接一脸懵逼，对图论不是很了解，昨天的深搜也不行，后续复习
# 果然和我想的广搜一样，但是没写过，算吧算吧


class Solution(object):
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # 1. 状态压缩 + 广度优先搜索
        # 思路与算法
        # 由于题目需要我们求出「访问所有节点的最短路径的长度」，并且图中每一条边的长度均为 1，考虑使用广度优先搜索的方法求出最短路径。
        # 在常规的广度优先搜索中，我们会在队列中存储节点的编号。对于本题而言，最短路径的前提是「访问了所有节点」，因此除了记录节点的编号以外，我们还需要记录每一个节点的经过情况。因此，我们使用三元组(u, mask, dist) 表示队列中的每一个元素，其中：
        # - u 表示当前位于的节点编号；
        # - mask 是一个长度为 n的二进制数，表示每一个节点是否经过。如果 mask的第 i位是 1，则表示节点 i已经过，否则表示节点 i未经过；
        # - dist 表示到当前节点为止经过的路径长度。
        # 这样一来，我们使用该三元组进行广度优先搜索，即可解决本题。
        import collections
        n = len(graph)
        # 初始时，我们将所有的(i, 2 ^ i, 0)放入队列，表示可以从任一节点开始
        q = collections.deque((i, 1 << i, 0) for i in range(n))
        # 细节
        # 为了保证广度优先搜索时间复杂度的正确性，即同一个节点 u 以及节点的经过情况 mask 只被搜索到一次，我们可以使用数组或者哈希表记录(u, mask) 是否已经被搜索过，防止无效的重复搜索。
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0
        while q:
            u, mask, dist = q.popleft()
            # 在搜索的过程中，如果当前三元组中的 mask包含 n个 1（即 mask = 2 ^ n - 1），那么就可以返回 dist作为答案。
            if mask == (1 << n) - 1:
                ans = dist
                break
            # 搜索相邻的节点
            for v in graph[u]:
                # 将 mask 的第 v 位置为 1
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))
        return ans
        # 复杂度分析
        # - 时间复杂度：O(n ^ 2 * 2 ^ n)。常规的广度优先搜索的时间复杂度为 O(n + m)，其中 n 和 m 分别表示图的节点数和边数。本题中引入了 mask 这一维度，其取值范围为[0, 2 ^ n)，因此可以看成是进行了 2 ^ n次常规的广度优先搜索。由于 m 的范围没有显式给出，在最坏情况下为完全图，有 m = O(n ^ 2)，因此总时间复杂度为 O(n ^ 2 * 2 ^ n)。
        # - 空间复杂度：O(n * 2 ^ n)，即为队列需要使用的空间。
        # 执行用时：92 ms, 在所有 Python 提交中击败了100.00 % 的用户
        # 内存消耗：18.3 MB, 在所有 Python 提交中击败了55.07 % 的用户

        # 2. 预处理点对间最短路 + 状态压缩动态规划
        # 思路与算法
        # 由于题目中给定的图是连通图，那么我们可以计算出任意两个节点之间 u,v 间的最短距离，记为 d(u, v)。这样一来，我们就可以使用动态规划的方法计算出最短路径。
        # n = len(graph)
        # d = [[n + 1] * n for _ in range(n)]
        # for i in range(n):
        #     for j in graph[i]:
        #         d[i][j] = 1
        # # 使用 floyd 算法预处理出所有点对之间的最短路径长度
        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        # f = [[float("inf")] * (1 << n) for _ in range(n)]
        # for mask in range(1, 1 << n):
        #     # 如果 mask 只包含一个 1，即 mask 是 2 的幂
        #     if (mask & (mask - 1)) == 0:
        #         u = bin(mask).count("0") - 1
        #         f[u][mask] = 0
        #     else:
        #         for u in range(n):
        #             if mask & (1 << u):
        #                 for v in range(n):
        #                     if (mask & (1 << v)) and u != v:
        #                         f[u][mask] = min(
        #                             f[u][mask], f[v][mask ^ (1 << u)] + d[v][u])

        # ans = min(f[u][(1 << n) - 1] for u in range(n))
        # return ans
        # 复杂度分析
        # - 时间复杂度：O(n ^ 2 * 2 ^ n)。状态的总数为 O(n * 2 ^ n)，对于每一个状态，我们需要 O(n) 的时间枚举 v 进行状态转移，因此总时间复杂度 O(n ^ 2 * 2 ^ n)。
        # 预处理所有 d(u, v)的时间复杂度为 O(n ^ 3)，但其在渐近意义下小于 O(n ^ 2 * 2 ^ n)，因此可以忽略。
        # - 空间复杂度：O(n * 2 ^ n)，即为存储所有状态需要使用的空间。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2, 3], [0], [0], [0]], 4),
        ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.shortestPathLength(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
