# -*- encoding: utf-8 -*-
'''
@File    :   2039. 网络空闲的时刻.py
@Time    :   2022/03/20 23:59:20
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/the-time-when-the-network-becomes-idle/
'''


from collections import deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # 最近没时间做
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n
        vis[0] = True
        q = deque([0])
        ans, dist = 0, 1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if vis[v]:
                        continue
                    vis[v] = True
                    q.append(v)
                    ans = max(ans, (dist * 2 - 1) //
                              patience[v] * patience[v] + dist * 2 + 1)
            dist += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[0, 1], [1, 2]], [0, 2, 1], 8),
        ([[0, 1], [0, 2], [1, 2]], [0, 10, 10], 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.networkBecomesIdle(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
