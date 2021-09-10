#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5852. 最小化目标值与所选元素的差.py
@Time    :   2021/08/22 11:15:17
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

https://leetcode-cn.com/contest/weekly-contest-255/problems/minimize-the-difference-between-target-and-chosen-elements/
'''

from typing import List


# 参加竞赛，这题偏难，没有做下去
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        return 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minimizeTheDifference(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
