#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   字符串中的第一个唯一字符.py
@Time    :   2021/07/28 23:02:33
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        minAns = float("inf")
        for i, x in enumerate(s):
            if x in d:
                d[x] = -1
            else:
                d[x] = i
        for i in d:
            if d[i] >= 0:
                minAns = min(d[i], minAns)
        if minAns == float("inf"):
            return -1
        return minAns
        # print(s)
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # print(d)
        # for i in d:
        #     if d[i] == 1:
        #         break
        # for j, x in enumerate(s):
        #     # print(j, x)
        #     if i == x:
        #         return j


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.firstUniqChar(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
