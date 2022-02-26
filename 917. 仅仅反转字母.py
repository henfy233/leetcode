# -*- encoding: utf-8 -*-
'''
@File    :   917. 仅仅反转字母.py
@Time    :   2022/02/23 13:25:51
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/reverse-only-letters/
'''


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # 自己写，还行
        # sl = list(s)
        # left, right = 0, len(s)-1
        # # print(right)
        # # print(sl)
        # while left < right:
        #     while not sl[left].isalpha() and left < right:
        #         left += 1
        #     while not sl[right].isalpha() and left < right:
        #         right -= 1
        #     if left >= right:
        #         break
        #     sl[left], sl[right] = sl[right], sl[left]
        #     left += 1
        #     right -= 1
        # return ''.join(sl)

        # 双指针
        ans = list(s)
        left, right = 0, len(ans) - 1
        while True:
            while left < right and not ans[left].isalpha():  # 判断左边是否扫描到字母
                left += 1
            while right > left and not ans[right].isalpha():  # 判断右边是否扫描到字母
                right -= 1
            if left >= right:
                break
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
        ("7_28]", "7_28]")
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.reverseOnlyLetters(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
