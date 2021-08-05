#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   802. 找到最终的安全状态.py
@Time    :   2021/08/05 10:56:24
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


# 做了蛮久的，没有头绪，后续需要重复做
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # 自己做，用了哈希表，但解决不了样例三
        # n = len(graph)
        # dict = {}
        # list = []
        # for i in range(n):
        #     if graph[i] == []:
        #         dict[i] = i
        #         list.append(i)
        # for i in range(n):
        #     count = 0
        #     for j in range(len(graph[i])):
        #         if graph[i][j] in dict:
        #             count += 1
        #     if i not in dict and count == len(graph[i]):
        #         list.append(i)
        # list.sort()
        # return list

        # 1. 深度优先搜索 + 三色标记法
        # 根据题意，若起始节点位于一个环内，或者能到达一个环，则该节点不是安全的。否则，该节点是安全的。
        # 我们可以使用深度优先搜索来找环，并在深度优先搜索时，用三种颜色对节点进行标记，标记的规则如下：
        # - 白色（用 0 表示）：该节点尚未被访问；
        # - 灰色（用 1 表示）：该节点位于递归栈中，或者在某个环上；
        # - 黑色（用 2 表示）：该节点搜索完毕，是一个安全节点。
        # n = len(graph)
        # color = [0] * n
        # def safe(x):
        #     # 1. 如果在搜索过程中遇到了一个灰色节点，则说明找到了一个环，此时退出搜索，栈中的节点仍保持为灰色，
        #     # 这一做法可以将「找到了环」这一信息传递到栈中的所有节点上。
        #     # 2. 如果搜索过程中没有遇到灰色节点，则说明没有遇到环，那么递归返回前，我们将其标记由灰色改为黑色，
        #     # 表示它是一个安全的节点。
        #     if color[x] > 0:
        #         return color[x] == 2
        #     # 当我们首次访问一个节点时，将其标记为灰色
        #     color[x] = 1
        #     # 继续搜索与其相连的节点
        #     for y in graph[x]:
        #         if not safe(y):
        #             return False
        #     color[x] = 2
        #     return True
        # return [i for i in range(n) if safe(i)]
        # 复杂度分析:
        # - 时间复杂度：O(n+m)，其中 n 是图中的点数，m 是图中的边数。
        # - 空间复杂度：O(n)。存储节点颜色以及递归栈的开销均为 O(n)。
        # 执行用时：84 ms, 在所有 Python 提交中击败了96.67%的用户
        # 内存消耗：17.8 MB, 在所有 Python 提交中击败了100.00%的用户

        # 2. 拓扑排序
        # 根据题意，若一个节点没有出边，则该节点是安全的；若一个节点出边相连的点都是安全的，则该节点也是安全的。
        # 根据这一性质，我们可以将图中所有边反向，得到一个反图，然后在反图上运行拓扑排序。
        import collections
        # 首先得到反图 rg 及其入度数组 inDeg
        rg = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                rg[y].append(x)
        in_deg = [len(ys) for ys in graph]
        # 将所有入度为 0 的点加入队列
        q = collections.deque([i for i, d in enumerate(in_deg) if d == 0])
        # 循环直至队列为空
        while q:
            # 然后不断取出队首元素
            for x in rg[q.popleft()]:
                # 将其出边相连的点的入度减一
                in_deg[x] -= 1
                # 若该点入度减一后为 0，则将该点加入队列
                if in_deg[x] == 0:
                    q.append(x)
        # 循环结束后，所有入度为 0 的节点均为安全的
        # 我们遍历入度数组，并将入度为 0 的点加入答案列表
        return [i for i, d in enumerate(in_deg) if d == 0]
        # 复杂度分析
        # - 时间复杂度：O(n+m)，其中 n 是图中的点数，m 是图中的边数。
        # - 空间复杂度：O(n+m)。需要 O(n+m) 的空间记录反图。
        # 执行用时：120 ms, 在所有 Python 提交中击败了76.67 % 的用户
        # 内存消耗：18.4 MB, 在所有 Python 提交中击败了63.33 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
        ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]),
        ([[], [0, 2, 3, 4], [3], [4], []], [0, 1, 2, 3, 4])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.eventualSafeNodes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
