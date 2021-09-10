# -*- encoding: utf-8 -*-
'''
@File    :   5849. 好子集的数目.py
@Time    :   2021/09/04 22:46:38
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-60/problems/the-number-of-good-subsets/
'''


from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4], 6),
        ([4, 2, 3, 15], 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfGoodSubsets(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
