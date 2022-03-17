# -*- encoding: utf-8 -*-
'''
@File    :   564. 寻找最近的回文数.py
@Time    :   2022/03/02 18:30:36
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/find-the-closest-palindrome/
'''


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # 困难题就躺平了
        # 模拟
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        selfPrefix = int(n[:(m + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                        abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("123", "121"),
        ("1", "0"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.nearestPalindromic(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
