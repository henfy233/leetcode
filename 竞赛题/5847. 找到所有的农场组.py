# -*- encoding: utf-8 -*-
'''
@File    :   5847. 找到所有的农场组.py
@Time    :   2021/09/04 22:40:34
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-60/problems/find-all-groups-of-farmland/
'''


from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # book = [[False] * len(land) for _ in range(len(land))]
        # print(book)
        # for i in range(len(land)):
        #     for j in range(len(land[i])):
        #         book[i][j] = True


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 0, 0], [0, 1, 1], [0, 1, 1]], [[0, 0, 0, 0], [1, 1, 2, 2]]),
        ([[1, 1], [1, 1]], [[0, 0, 1, 1]]),
        ([[0]], []),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findFarmland(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
