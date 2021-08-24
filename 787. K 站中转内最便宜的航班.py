# -*- encoding: utf-8 -*-
'''
@File    :   787. K 站中转内最便宜的航班.py
@Time    :   2021/08/24 01:45:44
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

本题和「1928. 规定时间内到达终点的最小花费」是类似的题。读者在解决本题后，可以尝试解决该题。

https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
'''
from typing import List


# 图论，永远的疼
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra 算法 自己做，还是错的
        # g = [[float('inf')]*n for _ in range(n)]
        # for x, y, val in flights:
        #     g[x][y] = val
        # # 新建邻接表
        # dist = [[float('inf'), -1] for _ in range(n)]
        # dist[src] = [0, -1]
        # used = [False]*n
        # for _ in range(n):
        #     x = -1
        # # 寻找未访问点 在 dist数组最小的索引
        #     for y, u in enumerate(used):
        #         if not u and (x == -1 or dist[y][0] < dist[x][0]):
        #             x = y
        #     # print('x', x)
        #     used[x] = True
        #     # 寻找当前点到目标点的最短路径
        #     for y, val in enumerate(g[x]):
        #         # print('y', y, 'val', val)
        #         tmp = min(dist[y][0], dist[x][0]+val)
        #         if dist[y][0] > tmp and dist[y][1] < k:
        #             dist[y][1] += 1
        #             dist[y][0] = tmp
        # print(dist[dst])
        # return dist[dst][0] if dist[dst][0] < float('inf') else -1

        # 1. 动态规划
        # 链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/solution/k-zhan-zhong-zhuan-nei-zui-bian-yi-de-ha-abzi/
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)
        ans = min(f[t][dst] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans
        # 下面的代码使用两个一维数组进行状态转移。
        # f = [float("inf")] * n
        # f[src] = 0
        # ans = float("inf")
        # for t in range(1, k + 2):
        #     g = [float("inf")] * n
        #     for j, i, cost in flights:
        #         g[i] = min(g[i], f[j] + cost)
        #     f = g
        #     ans = min(ans, f[dst])
        # return -1 if ans == float("inf") else ans
        # 复杂度分析
        # 时间复杂度：O((m+n)k)，其中 m 是数组 flights 的长度。状态的数量为 O(nk)，对于固定的 t，我们需要 O(m) 的时间计算出所有 f[t][..] 的值，因此总时间复杂度为 O((m+n)k)。
        # 空间复杂度：O(nk) 或 O(n)，即为存储状态需要的空间。
        # 执行用时：200 ms, 在所有 Python3 提交中击败了52.53 % 的用户
        # 内存消耗：15.5 MB, 在所有 Python3 提交中击败了58.93 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
        (5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [
         0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1, -1),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1, 6),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findCheapestPrice(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
