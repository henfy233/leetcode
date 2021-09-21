# -*- encoding: utf-8 -*-
'''
@File    :   58. 最后一个单词的长度.py
@Time    :   2021/09/21 12:09:27
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/length-of-last-word/
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 自己写，运用了python特性，取数组最后一个
        # flag = False
        # ans = 0
        # for i in s[::-1]:
        #     if not flag:
        #         if i != " ":
        #             flag = True
        #             ans += 1
        #     else:
        #         if i == " ":
        #             flag = False
        #             break
        #         else:
        #             ans += 1
        # return ans
        # 执行用时：24 ms, 在所有 Python3 提交中击败了97.17 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.46 % 的用户

        # 自己写，运用反转特性，但效果差很多
        # s = ''.join(reversed(s))
        # # print(s)
        # flag = False
        # ans = 0
        # for i in s:
        #     if flag:
        #         if i == ' ':
        #             flag = False
        #             break
        #         else:
        #             ans += 1
        #     else:
        #         if i != ' ':
        #             flag = True
        #             ans += 1
        # return ans
        # 执行用时：36 ms, 在所有 Python3 提交中击败了44.39 % 的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.35 % 的用户

        # 1. 反向遍历
        # https://leetcode-cn.com/problems/length-of-last-word/solution/zui-hou-yi-ge-dan-ci-de-chang-du-by-leet-51ih/
        index = len(s) - 1
        while s[index] == ' ':
            index -= 1
        wordLength = 0
        while index >= 0 and s[index] != ' ':
            wordLength += 1
            index -= 1
        return wordLength
        # 时间复杂度：O(n)，其中 n 是字符串的长度。最多需要反向遍历字符串一次。
        # 空间复杂度：O(1)。
        # 执行用时：32 ms, 在所有 Python3 提交中击败了70.74 % 的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了14.08 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("sds ", 3),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.lengthOfLastWord(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
