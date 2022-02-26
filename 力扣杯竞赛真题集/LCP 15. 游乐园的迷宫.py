# -*- encoding: utf-8 -*-
'''
@File    :   LCP 15. 游乐园的迷宫.py
@Time    :   2021/09/06 22:50:28
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/you-le-yuan-de-mi-gong/
'''


from typing import List

# 遇到困难题，直接copy，后续学习，套积分
# class Solution:
#     def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:


# 1. 贪心思路
# https://leetcode-cn.com/problems/you-le-yuan-de-mi-gong/solution/you-le-yuan-de-mi-gong-tan-xin-si-lu-by-leetcode-s/
class Solution:
    def sub(self, a, b):  # 求点 a 到点 b 的向量
        return [a[0]-b[0], a[1]-b[1]]

    def cross(self, a, b):  # 求向量 a 到向量 b 的向量叉积
        return a[0] * b[1] - a[1] * b[0]

    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        n = len(points)
        used = [False] * n  # 记录点的遍历情况， False未遍历 / True已遍历
        order = []  # 记录返回结果

        # 查找最左的点作为 起始点
        start = 0
        for i in range(0, n):
            if points[i][0] < points[start][0]:
                start = i
        used[start] = True
        order.append(start)

        for i in direction:
            nxt = -1
            if i == 'L':
                # 转向方向为 L，选择相对方向最右的点
                for j in range(0, n):
                    if not used[j]:
                        if nxt == -1 or self.cross(self.sub(points[nxt], points[start]), self.sub(points[j], points[start])) < 0:
                            nxt = j
            else:
                # 转向方向为 R，选择相对方向最左的点
                for j in range(0, n):
                    if not used[j]:
                        if nxt == -1 or self.cross(self.sub(points[nxt], points[start]), self.sub(points[j], points[start])) > 0:
                            nxt = j
            # 返回结果加入选择的点，更新下一次转向的起点
            used[nxt] = True
            order.append(nxt)
            start = nxt

        # 添加最后一个剩余点
        for i in range(0, n):
            if not used[i]:
                order.append(i)
        return order
        # 执行用时：1508 ms, 在所有 Python3 提交中击败了26.67 % 的用户
        # 内存消耗：15.3 MB, 在所有 Python3 提交中击败了93.33 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 1], [1, 4], [3, 2], [2, 1]], "LL", [0, 2, 1, 3]),
        ([[1, 3], [2, 4], [3, 3], [2, 1]], "LR", [0, 3, 1, 2]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.visitOrder(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
