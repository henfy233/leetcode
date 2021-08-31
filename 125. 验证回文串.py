# -*- encoding: utf-8 -*-
'''
@File    :   125. 验证回文串.py
@Time    :   2021/08/31 23:20:58
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/valid-palindrome/
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # n = len(s)
        # left = 0
        # right = n-1
        # # print(ord('0'), ord('9'))
        # # print(ord('a'), ord('z'))
        # # print(ord('A'), ord('Z'))
        # while left < right:
        #     s1 = ord(s[left])
        #     s2 = ord(s[right])
        #     while (s1 < 48 or 57 < s1) and (s1 < 65 or 90 < s1) and (s1 < 97 or 122 < s1) and left != right:
        #         left += 1
        #         s1 = ord(s[left])
        #     while (s2 < 48 or 57 < s2) and (s2 < 65 or 90 < s2) and (s2 < 97 or 122 < s2) and left != right:
        #         right -= 1
        #         s2 = ord(s[right])
        #     if s1 == s2 or (abs(s1 - s2) == 32 and s1 > 64 and s2 > 64):
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        # return True

        # 1. python 调用api
        new = s.lower()
        res = ''.join([x for x in new if x.isalpha() or x.isdigit()])
        leng = len(res)
        for i in range(leng//2):
            if res[i] != res[leng - 1 - i]:
                return False
        return True

        # 2. python 调用api
        # tmp = ""
        # # 把字母和数字按顺序取出来
        # for i in s:
        #     if i.isdigit():
        #         tmp += i
        #         continue
        #     # 字母全部转小写
        #     if i.isalpha():
        #         tmp += i.lower()
        # # 反转判断是否一致
        # if tmp == tmp[::-1]:
        #     return True
        # return False


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("aa", True),
        ("0P", False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isPalindrome(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
