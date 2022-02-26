# -*- encoding: utf-8 -*-
'''
@File    :   5868. 可互换矩形的组数.py
@Time    :   2021/09/12 10:39:16
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/contest/weekly-contest-258/problems/number-of-pairs-of-interchangeable-rectangles/
'''


from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # 自己做，超出时间限制
        # n = len(rectangles)
        # ans = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if rectangles[i][0] * rectangles[j][1] == rectangles[i][1] * rectangles[j][0]:
        #             ans += 1
        # return ans

        n = len(rectangles)
        ans = 0
        diff = [[0] * i for i in range(1, n)]
        print('diff', diff)
        for i in range(n-1):
            l = []
            for j in range(i+1, n):
                if rectangles[i][0] * rectangles[j][1] == rectangles[i][1] * rectangles[j][0]:
                    diff[j-1][i] = 1
                    l.append(j-1)
                    ans += 1
            print('l', l)
        print('diff', diff)
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        # ([[4, 8], [3, 6], [10, 20], [15, 30]], 6),
        # ([[4, 5], [7, 8]], 0),
        ([[4, 8], [6, 10], [9, 15], [8, 16], [12, 20]], 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.interchangeableRectangles(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
