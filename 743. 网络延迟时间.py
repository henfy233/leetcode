#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   743. 网络延迟时间.py
@Time    :   2021/08/02 00:11:21
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib
import heapq


# 错题,没有思路
# 五种最短路径 两种存图方式
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 1. Dijkstra 算法 贪心 枚举 单源最短路
        g = [[float('inf')]*n for _ in range(n)]
        for x, y, time in times:
            g[x-1][y-1] = time
        # 新建邻接表
        dist = [float('inf')]*n
        # 当前点为 0
        dist[k-1] = 0
        # 设置访问数组
        used = [False]*n
        for _ in range(n):
            x = -1
            # 寻找未访问点 在 dist数组最小的索引
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            # print('x', x)
            used[x] = True
            # 寻找当前点到目标点的最短路径
            for y, time in enumerate(g[x]):
                # print('y', y, 'time', time)
                dist[y] = min(dist[y], dist[x]+time)
            # print('dist', dist)
            # print('used', used)
        ans = max(dist)
        return ans if ans < float('inf') else -1
        # 执行用时：44 ms, 在所有 Python 提交中击败了100.00 % 的用户
        # 内存消耗：14.6 MB, 在所有 Python 提交中击败了41.24 % 的用户

        # 2. Dijkstra 算法 使用一个小根堆来寻找「未确定节点」中与起点距离最近的点
        # 数据数组
        # g = [[] for _ in range(n)]
        # for x, y, time in times:
        #     g[x - 1].append((y - 1, time))
        # # 新建邻接表
        # dist = [float('inf')] * n
        # dist[k - 1] = 0
        # q = [(0, k - 1)]
        # while q:
        #     time, x = heapq.heappop(q)
        #     if dist[x] < time:
        #         continue
        #     for y, time in g[x]:
        #         dist[y] = min(dist[y], dist[x] + time)
        #         heapq.heappush(q, (dist[y], y))
        # ans = max(dist)
        # return ans if ans < float('inf') else -1
        # 执行用时：52 ms, 在所有 Python 提交中击败了99.44 % 的用户
        # 内存消耗：14.6 MB, 在所有 Python 提交中击败了41.81 % 的用户

        # Floyd（邻接矩阵）
    #     N, M = 9, 6010
    #     w = [[]*N for _ in range(N)]
    #     INF = float('inf')
    #     for i in range(1, n+1):
    #         for j in range(1, n+1):
    #             w[i][j] = w[j][i] = 0 if i == j else INF
    #     for x, y, time in times:
    #         w[x][y] = time
    #     self.floyd(w, n)
    #     ans = 0
    #     for i in range(1, n+1):
    #         ans = max(ans, w[k][i])
    #     return -1 if ans >= INF / 2 else ans

    # def floyd(w, n):
    #     for x in range(1, n+1):
    #         for x in range(1, n+1):
    #             for z in range(1, n+1):
    #                 w[x][z] = min(w[x][z], w[x][x] + w[x][z])

        # 朴素 Dijkstra（邻接矩阵）

        # 堆优化 Dijkstra（邻接表）

        # Bellman Ford（邻接表）

        # SPFA（邻接表）


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1]], 2, 1, 1),
        ([[1, 2, 1]], 2, 2, -1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.networkDelayTime(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
