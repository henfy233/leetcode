#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   反转字符串.py
@Time    :   2021/07/28 17:55:48
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
        return s


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseString(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
