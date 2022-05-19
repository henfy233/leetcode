# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 58 - I. 翻转单词顺序.py
@Time    :   2022/05/15 00:30:21
@Author  :   henfy
@Diffi   :   Easy
@Method  :   双指针

题目：https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        # 双指针
        # s = s.strip()  # 删除首尾空格
        # # print(s)
        # i = j = len(s)-1
        # res = []
        # while i >= 0:
        #     while i >= 0 and s[i] != ' ':
        #         i -= 1
        #     res.append(s[i+1: j+1])
        #     while s[i] == ' ':
        #         i -= 1
        #     j = i
        # return ' '.join(res)

        # 分割 + 倒序
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)  # 拼接为字符串并返回


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world!  ", "world! hello"),
        ("a good   example", "example good a")
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseWords(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
