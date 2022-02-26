# -*- encoding: utf-8 -*-
'''
@File    :   5882. 网格游戏.py
@Time    :   2021/09/26 10:41:36
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-260/problems/grid-game/
'''


from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # 自己写，不会做
        # path = []
        # ans = []
        # n = len(grid)
        # m = len(grid[0])
        # print('n,m', n, m)

        # def dfs(x, y, sum, path):
        #     if x == m-1 and y == n-1:
        #         if sum > ans:
        #             ans = sum
        #         else:
        #             return sum
        #     if x < 0 or x > m-1 or y < 0 or y > n-1:
        #         return 0
        #     print('n,m', n, m)
        #     print('x,y', x, y)
        #     path.append((x, y))
        #     sum += grid[y][x]
        #     return max(dfs(x+1, y, sum, path),
        #                dfs(x, y+1, sum, path))

        # dfs(0, 0, 0, path)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[2, 5, 4], [1, 5, 1]], 4),
        ([[3, 3, 1], [8, 5, 2]], 4),
        ([[1, 3, 1, 15], [1, 3, 3, 1]], 7),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.gridGame(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
