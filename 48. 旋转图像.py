# -*- encoding: utf-8 -*-
'''
@File    :   48. 旋转图像.py
@Time    :   2021/09/01 01:09:37
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/rotate-image/
'''
import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. 先上下交换，在对角线交换
        # n = len(matrix)
        # for i in range(n//2):
        #     for j in range(n):
        #         matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        # for i in range(n-1, -1, -1):
        #     for j in range(i):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # return matrix

        # 2. 直接交换 一圈一圈的旋转
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                x = n - j - 1
                y = n - i - 1
                matrix[i][j] = matrix[x][i]
                matrix[x][i] = matrix[y][x]
                matrix[y][x] = matrix[j][y]
                matrix[j][y] = tmp
        return matrix

        # python 深拷贝
        # n = len(matrix)
        # tmp = copy.deepcopy(matrix)
        # for i in range(n-1, -1, -1):
        #     for j in range(n):
        #         # print('matrix[j][i]', matrix[j][i])
        #         matrix[j][i] = tmp[n-1-i][j]
        # return matrix


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.rotate(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
