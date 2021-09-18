# -*- encoding: utf-8 -*-
'''
@File    :   36. 有效的数独.py
@Time    :   2021/09/01 01:12:30
@Author  :   henfy
@Diffi   :   Medium
@Version :   2.0

题目：https://leetcode-cn.com/problems/valid-sudoku/
'''


from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 自己参考答案来写，逐渐有思路
        # n = len(board)
        # row = [[]*9 for _ in range(9)]
        # # print(row)
        # col = [[]*9 for _ in range(9)]
        # nine = [[]*9 for _ in range(9)]
        # for i in range(n):
        #     for j in range(n):
        #         tmp = board[i][j]
        #         if tmp != '.':
        #             if tmp in row[i]:
        #                 return False
        #             if tmp in col[j]:
        #                 return False
        #             if tmp in nine[i//3*3+j//3]:
        #                 return False
        #             row[i].append(tmp)
        #             col[j].append(tmp)
        #             nine[i//3*3+j//3].append(tmp)
        # return True
        # 执行用时：44 ms, 在所有 Python3 提交中击败了60.16 % 的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了26.70 % 的用户

        # https://leetcode-cn.com/problems/valid-sudoku/solution/chi-xiao-dou-nojie-ti-python-jian-ji-min-33yd/
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):

                curr = board[i][j]
                if curr == '.':
                    continue
                box_index = i//3 * 3 + j//3
                if curr in row[i] or curr in col[j] or curr in box[box_index]:
                    return False

                row[i].add(curr)
                col[j].add(curr)
                box[box_index].add(curr)
        return True

        # https://leetcode-cn.com/problems/valid-sudoku/solution/gong-shui-san-xie-yi-ti-san-jie-ha-xi-bi-ssxp/
        # 位运算解决


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True),
        ([["5", "3", "5", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False),
        ([["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isValidSudoku(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
