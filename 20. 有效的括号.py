# -*- encoding: utf-8 -*-
'''
@File    :   20. 有效的括号.py
@Time    :   2021/08/28 23:05:31
@Author  :   henfy
@Diffi   :   Easy
@Method  :   栈
@Question:   https://leetcode-cn.com/problems/valid-parentheses/
@Answer1 :  https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
@Answer2 :   https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
'''

# NOTE 继续练习
class Solution:
    def isValid(self, s: str) -> bool:
        # 1. 栈
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

        # 2.栈
        # dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        # # 解决边界问题：栈 stack 为空, 此时 stack.pop() 操作会报错, 给 stack 赋初值 ?
        # stack = ['?']
        # for c in s:
        #     if c in dic:
        #         stack.append(c)
        #     elif dic[stack.pop()] != c:
        #         return False
        # return len(stack) == 1


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
