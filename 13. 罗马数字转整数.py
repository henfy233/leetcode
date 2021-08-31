# -*- encoding: utf-8 -*-
'''
@File    :   13. 罗马数字转整数.py
@Time    :   2021/08/04 14:54:58
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/roman-to-integer/
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        # 自己想，多重判断
        # sum = 0
        # n = len(s)
        # i = 0
        # while i < n:
        #     # print(s[i])
        #     if s[i] == "I":
        #         i += 1
        #         if i != n and s[i] == "V":
        #             sum += 4
        #         elif i != n and s[i] == "X":
        #             sum += 9
        #         else:
        #             i -= 1
        #             sum += 1
        #     elif s[i] == "V":
        #         sum += 5
        #     elif s[i] == "X":
        #         i += 1
        #         if i != n and s[i] == "L":
        #             sum += 40
        #         elif i != n and s[i] == "C":
        #             sum += 90
        #         else:
        #             i -= 1
        #             sum += 10
        #     elif s[i] == "L":
        #         sum += 50
        #     elif s[i] == "C":
        #         i += 1
        #         if i != n and s[i] == "D":
        #             sum += 400
        #         elif i != n and s[i] == "M":
        #             sum += 900
        #         else:
        #             i -= 1
        #             sum += 100
        #     elif s[i] == "D":
        #         sum += 500
        #     elif s[i] == "M":
        #         sum += 1000
        #     i += 1
        # return sum
        # 执行用时：64 ms, 在所有 Python 提交中击败了57.89%的用户
        # 内存消耗：13 MB, 在所有 Python 提交中击败了63.81%的用户

        # 逆序,特殊技巧
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ret = 0
        for i in range(len(s)-1, -1, -1):
            if ret > 4*dic[s[i]]:
                ret -= dic[s[i]]
            else:
                ret += dic[s[i]]
        return ret
        # 执行用时：32 ms, 在所有 Python 提交中击败了99.93 % 的用户
        # 内存消耗：13 MB, 在所有 Python 提交中击败了59.45 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.romanToInt(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
