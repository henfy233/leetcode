# -*- encoding: utf-8 -*-
'''
@File    :   4. 玩具套圈.py
@Time    :   2021/09/11 15:32:24
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/contest/season/2021-fall/problems/vFjcfV/
'''


from typing import List


class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[3, 3, 1], [3, 2, 1]], [[4, 3]], 2, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.circleGame(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
