# -*- encoding: utf-8 -*-
'''
@File    :   5. 十字路口的交通.py
@Time    :   2021/09/11 15:33:26
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/contest/season/2021-fall/problems/Y1VbOX/
'''


from typing import List


class Solution:
    def trafficCommand(self, directions: List[str]) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.trafficCommand(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
