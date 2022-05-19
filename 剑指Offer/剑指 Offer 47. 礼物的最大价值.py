# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 47. 礼物的最大价值.py
@Time    :   2022/04/29 14:23:20
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
'''


from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 自己写，和参考代码一致
        # m = len(grid)
        # n = len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             grid[i][j] = grid[i][j]
        #         elif i == 0:
        #             grid[i][j] += grid[i][j-1]
        #         elif j == 0:
        #             grid[i][j] += grid[i-1][j]
        #         else:
        #             grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        # print(grid)
        # return grid[-1][-1]
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
        # 优化
        # m, n = len(grid), len(grid[0])
        # for j in range(1, n):  # 初始化第一行
        #     grid[0][j] += grid[0][j - 1]
        # for i in range(1, m):  # 初始化第一列
        #     grid[i][0] += grid[i - 1][0]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        # return grid[-1][-1]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ], 12),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxValue(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
