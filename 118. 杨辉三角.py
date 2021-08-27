# -*- encoding: utf-8 -*-
'''
@File    :   118. 杨辉三角.py
@Time    :   2021/08/28 00:43:32
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/pascals-triangle/
'''


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.generate(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
