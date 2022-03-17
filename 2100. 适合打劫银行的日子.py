# -*- encoding: utf-8 -*-
'''
@File    :   2100. 适合打劫银行的日子.py
@Time    :   2022/03/06 01:28:51
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank/
'''


from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # 自己做，超时了
        # n = len(security)
        # # flag = True
        # ans = []
        # for i in range(time, n-time):
        #     # print('i', i)
        #     flag = True
        #     for x in range(i-time, i):
        #         if security[x] < security[x+1]:
        #             flag = False
        #             break
        #         # print('x', x)
        #     if not flag:
        #         continue
        #     for y in range(i, i+time):
        #         if security[y] > security[y+1]:
        #             flag = False
        #             break
        #         # print('y', y)
        #     if not flag:
        #         continue
        #     ans.append(i)
        # return ans

        # 动态规划
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                right[n - i - 1] = right[n - i] + 1
        return [i for i in range(time, n - time) if left[i] >= time and right[i] >= time]


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([5, 3, 3, 3, 5, 6, 2], 2, [2, 3]),
        ([1, 1, 1, 1, 1], 0, [0, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6], 2, []),
        ([1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8], 2, [5, 10, 14])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.goodDaysToRobBank(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
