# -*- encoding: utf-8 -*-
'''
@File    :   1706. 球会落何处.py
@Time    :   2022/02/24 22:08:30
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/where-will-the-ball-fall/
'''


from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # 没时间做，还是算吧
        return []


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
         [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]], [1, -1, -1, -1, -1]),
        ([[-1]], [-1]),
        ([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1],
         [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]], [0, 1, 2, 3, 4, -1]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findBall(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
