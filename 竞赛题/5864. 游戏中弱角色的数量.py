# -*- encoding: utf-8 -*-
'''
@File    :   5864. 游戏中弱角色的数量.py
@Time    :   2021/09/05 10:40:54
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-257/problems/the-number-of-weak-characters-in-the-game/
'''


from typing import List
import numpy as np


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        num = 0
        max = [[0, 0], [0, 0]]
        print(properties)
        properties = np.array(properties)
        properties.sort(reverse=True)
        print(properties)
        for i in range(len(properties)):
            if properties[i][0] > max[0] and properties[i][1] > max[1]:
                max = properties[i]
                # print(max)
            if properties[i][0] < max[0] and properties[i][1] < max[1]:
                num += 1
        return num


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[5, 5], [6, 3], [3, 6]], 0),
        ([[2, 2], [3, 3]], 1),
        ([[1, 5], [10, 4], [4, 3]], 1),
        ([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]], 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfWeakCharacters(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
