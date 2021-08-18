#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   345. 反转字符串中的元音字母.py
@Time    :   2021/08/19 00:55:47
@Author  :   henfy
@Diffi   :   easy
@Version :   1.0

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


class Solution:
    def reverseVowels(self, s: str) -> str:
        # 自己写，这题简单，列表转字符串难
        # head, tail = 0, len(s)-1
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # x = list(s)
        # while head < tail:
        #     while head < tail and x[head] not in vowels:
        #         head += 1
        #     while head < tail and x[tail] not in vowels:
        #         tail -= 1
        #     if head < tail and x[head] in vowels and x[tail] in vowels:
        #         x[head], x[tail] = x[tail], x[head]
        #         head += 1
        #         tail -= 1
        # return ''.join(x)
        # 执行用时：48 ms, 在所有 Python3 提交中击败了90.19 % 的用户
        # 内存消耗：15.6 MB, 在所有 Python3 提交中击败了47.60 % 的用户

        # 1. 双指针
        # 思路与算法
        # 我们可以使用两个指针 i 和 j 对字符串相向地进行遍历。
        # 具体地，指针 i 初始时指向字符串 s 的首位，指针 j 初始时指向字符串 s 的末位。在遍历的过程中，我们不停地将 i 向右移动，直到 i 指向一个元音字母（或者超出字符串的边界范围）；同时，我们不停地将 j 向左移动，直到 j 指向一个元音字母。此时，如果 i < j，那么我们交换 i 和 j 指向的元音字母，否则说明所有的元音字母均已遍历过，就可以退出遍历的过程。
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"

        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not isVowel(s[i]):
                i += 1
            while j > 0 and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
        # 复杂度分析
        # 时间复杂度：O(n)，其中 n 是字符串 s 的长度。在最坏的情况下，两个指针各遍历整个字符串一次。
        # 空间复杂度：O(1) 或 O(n)，取决于使用的语言中字符串类型的性质。如果字符串是可修改的，那么我们可以直接在字符串上使用双指针进行交换，空间复杂度为 O(1)，否则需要使用 O(n) 的空间将字符串临时转换为可以修改的数据结构（例如数组），空间复杂度为 O(n)。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseVowels(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
