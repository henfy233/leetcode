# -*- encoding: utf-8 -*-
'''
@File    :   2055. 蜡烛之间的盘子.py
@Time    :   2022/03/08 15:28:00
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/plates-between-candles/
'''

from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # 前缀和 yyds, 看了答案抄着写的
        # 预处理 + 前缀和
        n = len(s)
        preSum, sum = [0]*n, 0
        left, l = [0]*n, 0
        for i, x in enumerate(s):
            # print(x, i)
            if x == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l
        # print('preSum', preSum)
        # print('left', left)

        right, r = [0]*n, -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            # print(x, y)
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y]-preSum[x]
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("**|**|***|", [[2, 5], [5, 9]], [2, 3]),
        ("***|**|*****|**||**|*", [[1, 17], [4, 5],
         [14, 17], [5, 11], [15, 16]], [9, 0, 0, 0, 0]),
        ("|*|*", [[3, 3]], [0])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.platesBetweenCandles(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
