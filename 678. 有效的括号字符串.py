# -*- encoding: utf-8 -*-
'''
@File    :   678. 有效的括号字符串.py
@Time    :   2021/09/12 11:17:55
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/valid-parenthesis-string/
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        # 自己做，最后一个样例过不了
        # sum = 0
        # num = 0
        # for i in s:
        #     print('i', i)
        #     if i == '(':
        #         sum += 1
        #     elif i == ')':
        #         sum -= 1
        #     elif i == '*':
        #         num += 1
        #     if sum < 0:
        #         if num > 0:
        #             num -= 1
        #         else:
        #             return False
        # if sum > 0:
        #     print('sum', sum, 'num', num)
        #     if num >= sum:
        #         return True
        #     else:
        #         return False
        # return True

        # 1. 动态规划
        # https://leetcode-cn.com/problems/valid-parenthesis-string/solution/you-xiao-de-gua-hao-zi-fu-chuan-by-leetc-osi3/
        n = len(s)
        if n == 0:
            return True
        dp = [[False]*n for _ in range(n)]
        for i, x in enumerate(s):
            if x == '*':
                dp[i][i] = True
        for i in range(1, n):
            c1 = s[i-1]
            c2 = s[i]
            dp[i - 1][i] = (c1 == '(' or c1 ==
                            '*') and (c2 == ')' or c2 == '*')
        for i in range(n-3, -1, -1):
            c1 = s[i]
            for j in range(i+2, n):
                c2 = s[j]
                if (c1 == '(' or c1 == '*') and (c2 == ')' or c2 == '*'):
                    dp[i][j] = dp[i + 1][j - 1]
                for k in range(i, j):
                    if not dp[i][j]:
                        dp[i][j] = dp[i][k] and dp[k + 1][j]
        return dp[0][n - 1]
        # 时间复杂度：O(n ^ 3)，其中 n 是字符串 s 的长度。动态规划的状态数是 O(n ^ 2)，每个状态的计算时间最多为 O(n)。
        # 空间复杂度：O(n ^ 2)，其中 n 是字符串 s 的长度。创建了 n 行 n 列的二维数组 dp。
        # 执行用时：416 ms, 在所有 Python3 提交中击败了6.02 % 的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.98 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        # ("()", True),
        ("(*)", True),
        ("(*))", True),
        ("(", False),
        ("", True),
        ("(((((*)))**", True),
        ("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())", False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.checkValidString(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
