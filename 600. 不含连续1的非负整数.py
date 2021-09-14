# -*- encoding: utf-8 -*-
'''
@File    :   600. 不含连续1的非负整数.py
@Time    :   2021/09/11 08:48:57
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/
'''

from functools import reduce


class Solution:
    def findIntegers(self, n: int) -> int:
        # 自己做，超出时间限制
        # ans = 0
        # for i in range(n+1):
        #     # print(bin(i)[2:])
        #     s = bin(i)[2:]
        #     # print(s)
        #     flag = False
        #     for j in s:
        #         # print('j', j)
        #         if j == '1':
        #             if not flag:
        #                 flag = True
        #             else:
        #                 ans -= 1
        #                 break
        #         else:
        #             flag = False
        #     ans += 1
        # return ans

        # 1. 动态规划
        # https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/solution/bu-han-lian-xu-1de-fei-fu-zheng-shu-by-l-9l86/
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        pre = 0
        res = 0

        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1

        return res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        # (5, 5),
        (6, 9),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findIntegers(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
