#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   541. 反转字符串 II.PY
@Time    :   2021/08/20 01:43:26
@Author  :   henfy
@Diffi   :   easy
@Version :   1.0

给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

 - 如果剩余字符少于 k 个，则将剩余字符全部反转。
 - 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 自己写，这题还是简单的
        # s = list(s)
        # n = len(s)

        # def reverse(s: list, l: int, r: int) -> list:
        #     while l < r:
        #         s[l], s[r] = s[r], s[l]
        #         l += 1
        #         r -= 1
        #     return s

        # head = 0
        # while head < n:
        #     if n - head >= k:
        #         s = reverse(s, head, head+k-1)
        #         head += 2*k
        #     else:
        #         s = reverse(s, head, n-1)
        #         head += n - head
        # return ''.join(s)
        # 执行用时：36 ms, 在所有 Python3 提交中击败了72.21 % 的用户
        # 内存消耗：15.2 MB, 在所有 Python3 提交中击败了25.38 % 的用户

        # 1. 模拟
        # 我们直接按题意进行模拟：反转每个下标从 2k 的倍数开始的，长度为 k 的子串。若该子串长度不足 k，则反转整个子串。
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)
        # 复杂度分析
        # 时间复杂度：O(n)，其中 n 是字符串 s 长度。
        # 空间复杂度：O(1) 或 O(n)，取决于使用的语言中字符串类型的性质。如果字符串是可修改的，那么我们可以直接在原字符串上修改，空间复杂度为 O(1)，否则需要使用 O(n) 的空间将字符串临时转换为可以修改的数据结构（例如数组），空间复杂度为 O(n)。
        # 执行用时：24 ms, 在所有 Python3 提交中击败了99.06 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了78.22 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("abcdefg", 2, "bacdfeg"),
        ("abcd", 2, "bacd"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseStr(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
