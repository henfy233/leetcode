#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   整数反转.py
@Time    :   2021/07/28 18:16:38
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 正负符号 不能超过32位 除10余数
        s = 0
        flag = True
        if x < 0:
            x = -x
            flag = False
        # while x % 10 or x//10:
        while x != 0:
            t = x % 10
            # print(x % 10)
            s = s * 10 + t
            if s > 2**31-1 or s < 0-2**31:
                return 0
            x //= 10
        return s if flag else -s


if __name__ == '__main__':
    s = Solution()
    test_list = [
        # (123, 321),
        (-123, -321),
        (0, 0),
        (120, 21),
        (1534236469, 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverse(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
