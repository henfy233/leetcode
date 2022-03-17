# -*- encoding: utf-8 -*-
'''
@File    :   521. 最长特殊序列 Ⅰ.py
@Time    :   2022/03/05 01:17:06
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/
'''


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # 好绕
        if a != b:
            return len(a) if len(a) > len(b) else len(b)
        else:
            return -1

        # 脑筋急转弯
        # return max(len(a), len(b)) if a != b else -1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("aba", "cdc", 3),
        ("aaa", "bbb", 3),
        ("aaa", "aaa", -1)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findLUSlength(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
