# -*- encoding: utf-8 -*-
'''
@File    :   1601. 最多可达成的换楼请求数目.py
@Time    :   2022/02/28 10:44:33
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/
'''


from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        return n


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]], 5),
        (3, [[0, 0], [1, 2], [2, 1]], 3),
        (4, [[0, 3], [3, 1], [1, 2], [2, 0]], 4)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maximumRequests(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
