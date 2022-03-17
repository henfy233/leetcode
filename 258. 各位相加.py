# -*- encoding: utf-8 -*-
'''
@File    :   258. 各位相加.py
@Time    :   2022/03/03 10:26:53
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/add-digits/
'''


class Solution:
    def addDigits(self, num: int) -> int:
        # 自己做
        # while num/10 >= 1:
        #     temp = num
        #     sum = 0
        #     while temp > 0:
        #         sum += temp % 10
        #         # print('sum', sum)
        #         temp //= 10
        #         # print('temp', temp)
        #     num = sum
        # return num

        # 模拟
        while num >= 10:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum
        return num

        # 数学
        # return (num - 1) % 9 + 1 if num else 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (38, 2),
        (0, 0),
        (10, 1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.addDigits(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
