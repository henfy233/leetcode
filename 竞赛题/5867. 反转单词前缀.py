# -*- encoding: utf-8 -*-
'''
@File    :   5867. 反转单词前缀.py
@Time    :   2021/09/12 10:31:08
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-258/problems/reverse-prefix-of-word/
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 自己做，通过了
        index = 0
        for i, x in enumerate(word):
            # print('i', i, 'x', x)
            if x == ch:
                index = i
                break
        s = list(word[:index+1])
        # print('s', s)
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        ans = ''.join(s)+word[index+1:]
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("abcdefd", "d", "dcbaefd"),
        ("xyxzxe", "z", "zxyxxe"),
        ("abcd", "z", "abcd"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reversePrefix(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
