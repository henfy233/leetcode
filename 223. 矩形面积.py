# -*- encoding: utf-8 -*-
'''
@File    :   223. 矩形面积.py
@Time    :   2021/09/30 23:14:56
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/rectangle-area/
'''


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 自己写，写得一般
        # s1 = (ax2 - ax1) * (ay2 - ay1)
        # print('s1', s1)
        # s2 = (bx2 - bx1) * (by2 - by1)
        # print('s2', s2)
        # ans = s1+s2
        # if ax2 >= bx1 and ay1 <= by2 and ay2 >= by1 and bx2 >= ax1:
        #     print('in it')
        #     x1 = max(ax1, bx1)
        #     y1 = max(ay1, by1)
        #     x2 = min(ax2, bx2)
        #     y2 = min(ay2, by2)
        #     print(x1, y1, x2, y2)
        #     s = (x2-x1)*(y2-y1)
        #     ans -= s
        # return ans
        # 执行用时：56 ms, 在所有 Python3 提交中击败了24.19 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了65.66 % 的用户

        # 1. 计算重叠面积
        # https://leetcode-cn.com/problems/rectangle-area/solution/ju-xing-mian-ji-by-leetcode-solution-xzbl/
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (-3, 0, 3, 4, 0, -1, 9, 2, 45),
        (-2, -2, 2, 2, -2, -2, 2, 2, 16),
        (-3, 5, 3, 7, 0, -1, 9, 4, 57),
        (-2, - 2, 2, 2, - 4, 3, -3, 4, 17),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.computeArea(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
