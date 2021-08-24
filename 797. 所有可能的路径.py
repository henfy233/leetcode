# -*- encoding: utf-8 -*-
'''
@File    :   797. 所有可能的路径.py
@Time    :   2021/08/25 00:17:45
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/all-paths-from-source-to-target/
'''
from typing import List


# 需要记住这种全排列的模板
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 自己做，通过，最近竟然第一次 AC 深度优先搜索
        # ans = []
        # n = len(graph)

        # def dfs(s: int, queue: List[int]):
        #     nonlocal ans
        #     # 找出所有从节点 0 到节点 n-1 的路径并输出
        #     if s == n-1:
        #         # print('queue', queue)
        #         ans.append(queue[:])
        #         return
        #     # print('s', s)
        #     # 每个节点指定下一个点
        #     for i in graph[s]:
        #         queue.append(i)
        #         dfs(i, queue)
        #         queue.pop()
        # dfs(0, [0])
        # return ans
        # 执行用时：60 ms, 在所有 Python3 提交中击败了16.79 % 的用户'
        # 内存消耗：16 MB, 在所有 Python3 提交中击败了87.94 % 的用户

        # 1. 深度优先搜索
        # https://leetcode-cn.com/problems/all-paths-from-source-to-target/solution/suo-you-ke-neng-de-lu-jing-by-leetcode-s-iyoh/
        ans = list()
        stk = list()

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(stk[:])
                return

            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()
        stk.append(0)
        dfs(0)
        return ans
        # 复杂度分析
        # 时间复杂度：O(n × 2 ^ n)，其中 n 为图中点的数量。我们可以找到一种最坏情况，即每一个点都可以去往编号比它大的点。此时路径数为 O(2 ^ n)，且每条路径长度为 O(n)，因此总时间复杂度为 O(n × 2 ^ n)。
        # 空间复杂度：O(n)，其中 n 为点的数量。主要为栈空间的开销。注意返回值不计入空间复杂度。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        ([[4, 3, 1], [3, 2, 4], [3], [4], []], [
         [0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
        ([[1], []], [[0, 1]]),
        ([[1, 2, 3], [2], [3], []], [[0, 1, 2, 3], [0, 2, 3], [0, 3]]),
        ([[1, 3], [2], [3], []], [[0, 1, 2, 3], [0, 3]]),
        ([[4, 3, 1], [3, 2, 4], [], [4], []], [
         [0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 4]]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.allPathsSourceTarget(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
