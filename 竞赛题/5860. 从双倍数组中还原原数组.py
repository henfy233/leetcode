# -*- encoding: utf-8 -*-
'''
@File    :   5860. 从双倍数组中还原原数组.py
@Time    :   2021/09/18 22:41:58
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/biweekly-contest-61/problems/find-original-array-from-doubled-array/
'''


from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        # changed.sort()
        # ans = []
        # res = []
        # for x in changed:
        #     if x in res:
        #         res.remove(x)
        #         continue
        #     # print('x', x)
        #     tmp = x * 2
        #     if tmp in changed:
        #         res.append(tmp)
        #         ans.append(x)
        # # print('ans', ans)
        # # print('res', res)
        # # print('changed', changed)
        # if len(res) > 0:
        #     return []
        # return ans

        # 超出时间限制
        changed.sort()
        ans = []
        for x in changed:
            print('x', x)
            tmp = x * 2
            if tmp in changed:
                print('x', x)
                changed.remove(tmp)
                ans.append(x)
        print('ans', ans)
        print('changed', changed)
        if ans == changed:
            return ans
        else:
            return []


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 4, 8, 4, 8, 16], [2, 4, 8]),
        ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
        ([6, 3, 0, 1], []),
        ([1], []),
        ([0, 3, 2, 4, 6, 0], [0, 2, 3])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findOriginalArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
