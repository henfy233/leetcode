#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   最长公共前缀.py
@Time    :   2021/07/29 23:52:33
@Author  :   henfy
@Version :   1.0
'''

# here put the import lib


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # ns = len(strs)
        # # s = ""
        # for s in strs:
        #     for i in s

        # 没去想，这是用别人的想法的
        if len(strs) == 0:
            return ""
        pre = strs[0]
        strs = strs[1:]
        for i in range(len(strs)):
            count = 0
            length = min(len(pre), len(strs[i]))
            for j in range(length):
                if strs[i][j] == pre[j]:
                    count += 1
                else:
                    break
            pre = pre[:count]
        return pre


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.longestCommonPrefix(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
