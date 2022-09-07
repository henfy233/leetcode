# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 12. 矩阵中的路径.py
@Time    :   2022/05/15 00:42:53
@Author  :   henfy
@Diffi   :   Easy
@Method  :   搜索与回溯算法（中等）

题目：https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/
'''


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度优先搜索（DFS）+ 剪枝
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k +
                                              1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]], "ABCCED", True),
        ([["a", "b"], ["c", "d"]], "abcd", False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.exist(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
