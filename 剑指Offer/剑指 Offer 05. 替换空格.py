# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 05. 替换空格.py
@Time    :   2022/04/25 00:47:22
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
'''


class Solution:
    def replaceSpace(self, s: str) -> str:
        # ans = []
        # for i in s:
        #     if i == ' ':
        #         ans.append('%20')
        #     else:
        #         ans.append(i)
        # return ''.join(ans)

        # 简单作弊法
        return s.replace(' ', '%20')


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("We are happy.", "We%20are%20happy."),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.replaceSpace(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
