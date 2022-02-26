# -*- encoding: utf-8 -*-
'''
@File    :   537. 复数乘法.py
@Time    :   2022/02/25 21:26:53
@Author  :   henfy
@Diffi   :   Midddle
@Version :   1.0

题目：https://leetcode-cn.com/problems/complex-number-multiplication/
'''


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # 自己做，不难
        # s = num1.split('+', 1)
        # a, b = int(s[0]), int(s[1][:-1])
        # s = num2.split('+', 1)
        # c, d = int(s[0]), int(s[1][:-1])
        # # print(a, b, c, d)
        # x = a*c-b*d
        # y = c*b+a*d
        # # print(x, y)
        # return str(x)+"+"+str(y)+"i"

        # 模拟
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i'


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("1+1i", "1+1i", "0+2i"),
        ("1+-1i", "1+-1i", "0+-2i"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.complexNumberMultiply(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
