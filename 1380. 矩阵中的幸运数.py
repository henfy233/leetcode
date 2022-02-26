# -*- encoding: utf-8 -*-
'''
@File    :   1380. 矩阵中的幸运数.py
@Time    :   2022/02/15 19:03:40
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/
'''

from typing import List


# 不会
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # length = len(matrix)
        # for x in range(length):
        #     index = min(matrix[x])
        #     print('index', index)
        #     for y in range(length):
        #         print('x', x, 'y', y)

        # 模拟
        # ans = []
        # for row in matrix:
        #     for j, x in enumerate(row):
        #         # print('j', j, 'x', x)
        #         # print(row)
        #         # print(max(r[j] for r in matrix))
        #         if max(r[j] for r in matrix) <= x <= min(row):
        #             ans.append(x)
        # return ans

        # 预处理
        minRow = [min(row) for row in matrix]
        maxCol = [max(col) for col in zip(*matrix)]
        print(minRow, maxCol)
        ans = []
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == minRow[i] == maxCol[j]:
                    ans.append(x)
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
        ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
        ([[7, 8], [1, 2]], [7]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.luckyNumbers(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
