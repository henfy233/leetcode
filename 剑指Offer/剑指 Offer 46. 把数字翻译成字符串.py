# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 46. 把数字翻译成字符串.py
@Time    :   2022/04/29 14:42:07
@Author  :   henfy
@Diffi   :   Middle

题目：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
'''


class Solution:
    def translateNum(self, num: int) -> int:
        # 不会
        # 字符串遍历
        # s = str(num)
        # a = b = 1
        # for i in range(2, len(s)+1):
        #     tmp = s[i-2:i]
        #     c = a + b if "10" <= tmp <= "25" else a
        #     b = a
        #     a = c
        # return a

        # 数字求余
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            tmp = 10 * x + y
            c = a + b if 10 <= tmp <= 25 else a
            a, b = c, a
            y = x
        return a


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (12258, 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.translateNum(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
