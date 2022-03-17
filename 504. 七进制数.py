# -*- encoding: utf-8 -*-
'''
@File    :   504. 七进制数.py
@Time    :   2022/03/07 00:41:38
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/base-7/
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        # 自己写，通过，有点麻烦
        # if num < 0:
        #     symbol = ['-']
        #     num = -1*num
        # else:
        #     symbol = []
        # res = []
        # ans = ['0'] * 9
        # for i in range(9):
        #     res.append(7 ** i)
        #     # if 7**i > 10 ** 7:
        #     #     print(i)
        # # print('res', res)
        # for x in range(8, -1, -1):
        #     if num >= res[x]:
        #         ans[x] = str(num//res[x])
        #         num -= int(ans[x]) * res[x]
        #         print(x)
        # # print('ans', ans)
        # for i in range(8, -1, -1):
        #     if ans[i] != '0':
        #         break
        # # print('i', i)
        # # print('ans', ''.join(symbol+ans[i::-1]))
        # return ''.join(symbol+ans[i::-1])

        # 倒推 + 迭代
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append('-')
        return ''.join(reversed(digits))


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (100, "202"),
        (-7, "-10")
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.convertToBase7(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
