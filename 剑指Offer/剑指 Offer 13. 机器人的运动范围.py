# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 13. 机器人的运动范围.py
@Time    :   2022/05/20 00:56:47
@Author  :   henfy
@Diffi   :   Middle
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
'''


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度优先搜索（DFS）
        # def dfs(i, j, si, sj):
        #     if not 0 <= i < m or not 0 <= j < n or k < si+sj or (i, j) in visited:
        #         return 0
        #     visited.add((i, j))
        #     return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        # visited = set()
        # return dfs(0, 0, 0, 0)

        # 广度优先遍历 BFS
        queue, visited = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 3, 1, 3),
        (3, 1, 0, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.movingCount(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
