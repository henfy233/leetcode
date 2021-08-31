# -*- encoding: utf-8 -*-
'''
@File    :   344. 反转字符串.py
@Time    :   2021/07/28 19:05:45
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/reverse-string/submissions/
'''


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 自己写，简单
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        return s
        # 执行用时：40 ms, 在所有 Python3 提交中击败了75.86 % 的用户
        # 内存消耗：19.2 MB, 在所有 Python3 提交中击败了50.70 % 的用户

        # 1.双指针
        # https://leetcode-cn.com/problems/reverse-string/solution/fan-zhuan-zi-fu-chuan-by-leetcode-solution/
        # 和我的做法差不多，还是不改吧


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseString(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
