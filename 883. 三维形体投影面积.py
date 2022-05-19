# -*- encoding: utf-8 -*-
'''
@File    :   883. 三维形体投影面积.py
@Time    :   2022/04/26 22:53:05
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/projection-area-of-3d-shapes/
'''


from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # 转置数组有点麻烦，自己写
        # n = len(grid)
        # ans = 0
        # xx = list(zip(*grid))
        # for i in range(n):
        #     ans += max(grid[i])
        #     ans += max(xx[i])
        #     for j in range(n):
        #         if grid[i][j] != 0:
        #             ans += 1
        # return ans

        # 数学
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        zxArea = sum(map(max, grid))
        return xyArea + yzArea + zxArea


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 2], [3, 4]], 17),
        ([[2]], 5),
        ([[1, 0], [0, 2]], 8),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.projectionArea(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
