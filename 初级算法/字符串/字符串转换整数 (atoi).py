#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   字符串转换整数 (atoi).py
@Time    :   2021/07/29 13:39:37
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib
import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = 0
        n = len(s)
        sign = True
        head = 0
        # 极端情况 "  " 和""
        if s == "":
            return 0
        # 先去除空格
        while head < n and s[head] == ' ':
            head += 1
        if head == n:
            return w
        # 判断符号
        if s[head] == '-':
            sign = False
            head += 1
        elif s[head] == '+':
            sign = True
            head += 1
        while head < n and s[head].isdigit():
            w = w*10 + int(s[head])
            head += 1
        # 判定是否溢值
        if sign:
            return min(w, 2**31-1)
        else:
            return max(-w, -2**31)

        # 正则运算
        # realNumber = 0
        # s = s.lstrip()
        # result1 = re.findall(r'^[-|+]?\d+', s)
        # if len(result1) != 0:
        #     tempS = int(''.join(map(str, result1)))
        #     if tempS >= (-2)**31 and tempS <= (2**31 - 1):
        #         realNumber = tempS
        #     elif tempS < (-2)**31:
        #         realNumber = (-2)**31
        #     else:
        #         realNumber = 2**31 - 1
        # return realNumber

        # return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("", 0),
        ("+1", 1),
        ("-+12", 0),
        (" ", 0)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.myAtoi(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
