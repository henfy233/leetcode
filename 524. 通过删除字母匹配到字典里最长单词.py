# -*- encoding: utf-8 -*-
'''
@File    :   524. 通过删除字母匹配到字典里最长单词.py
@Time    :   2021/09/14 00:01:26
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/
'''


from typing import List
import collections


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 自己做，做错了，参考了双指针来写
        # n = len(dictionary)
        # res = ""
        # for i in range(n):
        #     left, right = 0, 0
        #     while left < len(s) and right < len(dictionary[i]):
        #         if s[left] == dictionary[i][right]:
        #             right += 1
        #         left += 1
        #     if right == len(dictionary[i]):
        #         if right > len(res) or (right == len(res) and dictionary[i] < res):
        #             print('dictionary[i]', dictionary[i])
        #             print('res', res)
        #             print('dictionary[i] < res', dictionary[i] < res)
        #             res = dictionary[i]
        # return res

        # 1. 双指针
        # https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/
        # res = ""
        # for t in dictionary:
        #     i = j = 0
        #     while i < len(t) and j < len(s):
        #         if t[i] == s[j]:
        #             i += 1
        #         j += 1
        #     if i == len(t):
        #         if len(t) > len(res) or (len(t) == len(res) and t < res):
        #             res = t
        # return res
        # 时间复杂度：O(d×(m+n))，其中 d 表示 dictionary 的长度，m 表示 s 的长度，n 表示 dictionary 中字符串的平均长度。我们需要遍历 dictionary 中的 d 个字符串，每个字符串需要 O(n+m) 的时间复杂度来判断该字符串是否为 s 的子序列。
        # 空间复杂度：O(1)。

        # 2. 排序
        # https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/
        # # print('dictionary', dictionary)
        # dictionary.sort(key=lambda x: (-len(x), x))
        # # print('dictionary', dictionary)
        # for t in dictionary:
        #     i = j = 0
        #     while i < len(t) and j < len(s):
        #         if t[i] == s[j]:
        #             i += 1
        #         j += 1
        #     if i == len(t):
        #         return t
        # return ""

        # 2. 动态规划
        # https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/
        m = len(s)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                if ord(s[i]) == j + 97:
                    f[i][j] = i
                else:
                    f[i][j] = f[i + 1][j]

        res = ""
        for t in dictionary:
            match = True
            j = 0
            for i in range(len(t)):
                if f[j][ord(t[i]) - 97] == m:
                    match = False
                    break
                j = f[j][ord(t[i]) - 97] + 1
            if match:
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("abpcplea", ["ale", "apple", "monkey", "plea"], "apple"),
        ("abpcplea", ["a", "b", "c"], "a"),
        ("abce", ["abe", "abc"], "abc"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findLongestWord(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
