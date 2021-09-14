# -*- encoding: utf-8 -*-
'''
@File    :   447. 回旋镖的数量.py
@Time    :   2021/09/13 09:09:45
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/number-of-boomerangs/
'''


from typing import List
import collections


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # 自己做，超出超出时间限制
        # n = len(points)
        # # print('n', n)
        # ans = 0

        # def distance(arr1, arr2):
        #     x = arr1[0]-arr2[0]
        #     y = arr1[1]-arr2[1]
        #     # print('x', x, 'y', y)
        #     return x ** 2 + y ** 2
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         for k in range(n):
        #             if i == k or j == k:
        #                 continue
        #             if distance(points[i], points[j]) == distance(points[i], points[k]):
        #                 # print('points[i], points[j]', points[i], points[j])
        #                 # print('points[i], points[k]', points[i], points[k])
        #                 # print('i', i, 'j', j, 'k', k)
        #                 ans += 1
        # # print('ans', ans)
        # return ans

        # 1. 枚举 + 哈希表
        # https://leetcode-cn.com/problems/number-of-boomerangs/solution/hui-xuan-biao-de-shu-liang-by-leetcode-s-lft5/
        ans = 0
        for p in points:
            cnt = collections.defaultdict(int)
            for q in points:
                dis = (p[0] - q[0]) * (p[0] - q[0]) + \
                    (p[1] - q[1]) * (p[1] - q[1])
                cnt[dis] += 1
            # print('cnt', cnt)
            for m in cnt.values():
                # print('m', m)
                ans += m * (m - 1)
        # print('cnt', cnt)
        return ans
        # 时间复杂度：O(n ^ 2)，其中 n 是数组 points 的长度。
        # 空间复杂度：O(n)。
        # 执行用时：704 ms, 在所有 Python3 提交中击败了89.58 % 的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了54.17 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[0, 0], [1, 0], [2, 0]], 2),
        ([[1, 1], [2, 2], [3, 3]], 2),
        ([[1, 1]], 0),
        ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]], 24),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfBoomerangs(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
