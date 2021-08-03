#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5831. 你可以工作的最大周数.py
@Time    :   2021/08/02 00:01:49
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


# 错题,没有思路
class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        # 如果 longest > rest+1，那么无法完成所有的工作
        # 1. 贪心
        longest = max(milestones)
        rest = sum(milestones) - longest
        if longest > rest + 1:
            return rest*2+1
        else:
            return longest + rest


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3], 6),
        ([5, 2, 1], 7),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfWeeks(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
