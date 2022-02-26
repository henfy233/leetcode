# -*- encoding: utf-8 -*-
'''
@File    :   5870. 每棵子树内缺失的最小基因值.py
@Time    :   2021/09/12 11:14:56
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-258/problems/smallest-missing-genetic-value-in-each-subtree/
'''


from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.smallestMissingValueSubtree(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
