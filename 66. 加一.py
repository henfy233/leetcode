# -*- encoding: utf-8 -*-
'''
@File    :   66. 加一.py
@Time    :   2021/08/31 23:44:58
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/plus-one/
'''


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # python数组优点
        n = len(digits)
        digits[n-1] += 1
        while digits[n-1] == 10:
            if n-2 < 0:
                digits[n-1] = 0
                digits = [1]+digits[:]
                # digits.insert(0, 1)
            else:
                digits[n-2] += 1
                digits[n-1] = 0
            n -= 1
        return digits


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([0], [1]),
        ([9], [1, 0]),
        ([1, 9], [2, 0]),
        ([9, 9], [1, 0, 0]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.plusOne(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
