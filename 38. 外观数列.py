# -*- encoding: utf-8 -*-
'''
@File    :   38. 外观数列.py
@Time    :   2021/07/29 23:21:41
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/count-and-say/
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        # 不会做，觉得很麻烦
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        ans = ''
        start, end = 0, 0
        while end < len(s):
            while end < len(s) and s[start] == s[end]:
                end += 1
            ans += str(end - start) + s[start]
            start = end
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (1, "1"),
        (4, "1211"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countAndSay(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
