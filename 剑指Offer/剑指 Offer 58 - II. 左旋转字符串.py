# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 58 - II. 左旋转字符串.py
@Time    :   2022/04/25 00:59:01
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
'''


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 字符串切片
        # return s[n:] + s[:n]

        # 列表遍历拼接
        # ans = []
        # for i in range(n, len(s)):
        #     ans.append(s[i])
        # for i in range(n):
        #     ans.append(s[i])
        # return ''.join(ans)

        # 利用求余运算，可以简化代码
        # res = []
        # for i in range(n, n + len(s)):
        #     res.append(s[i % len(s)])
        # return ''.join(res)

        # 字符串遍历拼接
        res = ""
        for i in range(n, n + len(s)):
            res += s[i % len(s)]
        return res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("abcdefg", 2, "cdefgab"),
        ("lrloseumgh", 6, "umghlrlose"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseLeftWords(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
