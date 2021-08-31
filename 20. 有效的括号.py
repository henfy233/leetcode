# -*- encoding: utf-8 -*-
'''
@File    :   20. 有效的括号.py
@Time    :   2021/08/28 23:05:31
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/valid-parentheses/
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # 自己写，超出输出限制
        # arr = []
        # pairs = {'(': ')', '[': ']', '{': '}'}
        # tmp = ''
        # for i in s:
        #     # print(i)
        #     if tmp != i:
        #         arr.append(i)
        #         if i in pairs:
        #             tmp = pairs[i]
        #         else:
        #             return False
        #     else:
        #         arr.pop()
        #         tmp = pairs[arr[-1]] if len(arr) > 0 else ''
        #     print(arr)
        # # return True if len(arr) == 0 else False
        # return not arr

        # 1. 栈
        # https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
        # if len(s) % 2 == 1:
        #     return False
        # pairs = {
        #     ")": "(",
        #     "]": "[",
        #     "}": "{",
        # }
        # stack = list()
        # for ch in s:
        #     if ch in pairs:
        #         if not stack or stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(ch)
        # return not stack
        # 复杂度分析
        # 时间复杂度：O(n)，其中 n 是字符串 s 的长度。
        # 空间复杂度：O(n +∣Σ∣)，其中 Σ 表示字符集，本题中字符串只包含 6 种括号∣Σ∣= 6。栈中的字符数量为 O(n)，而哈希表使用的空间为 O(∣Σ∣)，相加即可得到总空间复杂度。

        # 另一种简单的方法
        # https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(){}}{", False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isValid(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
