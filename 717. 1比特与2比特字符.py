# -*- encoding: utf-8 -*-
'''
@File    :   717. 1比特与2比特字符.py
@Time    :   2022/02/20 11:59:34
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/
'''


from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 错误的做法，没有想到好的做法
        # for i, x in enumerate(bits):
        #     if x != 0:
        #         break
        # length = len(bits) - i
        # print(length)
        # if length % 2 == 0:
        #     return False
        # else:
        #     return True

        # 正序遍历
        i, n = 0, len(bits)
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1

        # 倒序遍历
        # n = len(bits)
        # i = n - 2
        # while i >= 0 and bits[i]:
        #     i -= 1
        # return (n - i) % 2 == 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 0, 0], True),
        ([1, 1, 1, 0], False),
        ([0, 0], True),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isOneBitCharacter(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
