# -*- encoding: utf-8 -*-
'''
@File    :   1719. 重构一棵树的方案数.py
@Time    :   2022/02/16 18:04:14
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/
'''


from collections import defaultdict
from sys import maxsize
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # 太难了

        # 直接模拟
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        # 检测是否存在根节点
        root = next((node for node, neighbours in adj.items()
                    if len(neighbours) == len(adj) - 1), -1)
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue

            currDegree = len(neighbours)
            parent = -1
            parentDegree = maxsize
            # 根据 degree 的大小找到 node 的父节点 parent
            for neighbour in neighbours:
                if currDegree <= len(adj[neighbour]) < parentDegree:
                    parent = neighbour
                    parentDegree = len(adj[neighbour])
            # 检测 neighbours 是否为 adj[parent] 的子集
            if parent == -1 or any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours):
                return 0

            if parentDegree == currDegree:
                ans = 2
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2], [2, 3]], 1),
        ([[1, 2], [2, 3], [1, 3]], 2),
        ([[1, 2], [2, 3], [2, 4], [1, 5]], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.checkWays(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
