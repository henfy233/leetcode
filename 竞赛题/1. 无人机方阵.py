# -*- encoding: utf-8 -*-
'''
@File    :   1. 无人机方阵.py
@Time    :   2021/09/11 15:01:37
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/season/2021-fall/problems/0jQkd0/
'''

import collections
from typing import List


class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        # 自己做，通过了
        N = len(target)
        M = len(target[0])
        d = collections.defaultdict()
        for i in range(N):
            for j in range(M):
                if target[i][j] not in d:
                    d[target[i][j]] = 1
                else:
                    d[target[i][j]] += 1
                # if target[i][j] != source[i][j]:
        print(d)
        sum = 0
        for i in range(N):
            for j in range(M):
                if source[i][j] in d:
                    d[source[i][j]] -= 1
                    if d[source[i][j]] < 0:
                        sum += 1
                    # print('d[source[i][j]]', d[source[i][j]])
                    # x = d[source[i][j]][0]
                    # y = d[source[i][j]][1]
                    # source[i][j], source[x][y] = source[x][y], source[i][j]
                else:
                    sum += 1
        print('source', source)
        return sum


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 3], [5, 4]], [[3, 1], [6, 5]], 1),
        ([[1, 2, 3], [3, 4, 5]], [[1, 3, 5], [2, 3, 4]], 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minimumSwitchingTimes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
