#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1583. 统计不开心的朋友.py
@Time    :   2021/08/14 00:32:20
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。

对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。

所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。

但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x 就会不开心：

x 与 u 的亲近程度胜过 x 与 y，且
u 与 x 的亲近程度胜过 u 与 v
返回 不开心的朋友的数目 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-unhappy-friends
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


# 最近半夜做题没头绪，盖亚，看答案吧
class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        # 自己写，没头绪
        # sum = 0
        # for i in range(len(pairs)):
        #     x = pairs[i][0]
        #     y = pairs[i][1]
        #     for j in range(i+1, len(pairs)):
        #         u = pairs[j][0]
        #         v = pairs[j][1]
        #         if

        # 1. 模拟
        # 这道题看似复杂，其实只要进行模拟，即可得到答案。
        # 共有 n 位朋友，每位朋友都对应一个其余 n−1 位朋友的亲近程度从高到低排列的朋友列表，列表中的下标越小的朋友亲近程度越高。
        # 题目已经给出了二维数组 preferences 表示每位朋友对应的按亲近程度从高到低排列的朋友列表，但是并没有直接给出其余 n−1 位朋友对应的亲近程度下标，因此需要进行预处理，存储每位朋友的其余 n−1 位朋友对应的亲近程度下标。

        # 具体而言，创建 n 行 n 列的二维数组 order，其中 order[i][j] 表示朋友 j 在 i 的朋友列表中的亲近程度下标。
        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                # 遍历 preferences 即可填入 order 中的全部元素的值。
                order[i][preferences[i][j]] = j
        # 所有的朋友被分成 n/2 对，为了快速知道每位朋友的配对的朋友，对于配对情况也需要进行预处理。创建长度为 n 的数组 match，如果 x 和 y 配对，则有 match[x] = y 以及 match[y] = x。
        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x
        # 进行预处理之后，即可统计不开心的朋友的数目。
        unhappyCount = 0
        # 遍历从 0 到 n−1 的每位朋友 x，进行如下操作。
        for x in range(n):
            # 找到与朋友 x 配对的朋友 y。
            y = match[x]
            # 找到朋友 y 在朋友 x 的朋友列表中的亲近程度下标，记为 index。
            index = order[x][y]
            # 朋友 x 的朋友列表中的下标从 0 到 index−1 的朋友都是可能的 u。遍历每个可能的 u，找到与朋友 u 配对的朋友 v。
            for i in range(index):
                u = preferences[x][i]
                v = match[u]
                # 如果 order[u][x] < order[u][v]，则 x 是不开心的朋友。
                if order[u][x] < order[u][v]:
                    unhappyCount += 1
                    break
                # 需要注意的是，对于每个朋友 x，只要能找到一个满足条件的四元组(x, y, u, v)，则 x 就是不开心的朋友。
        return unhappyCount
        # 复杂度分析
        # 时间复杂度：O(n ^ 2)。
        # 预处理需要填入二维数组 order 和数组 match 中的值，时间复杂度分别是 O(n ^ 2) 和 O(n)。
        # 统计不开心的朋友的数目时，需要遍历每个 x，找到满足要求的四元组(x, y, u, v)，其中遍历 u 的时间复杂度是 O(n)，在已知 x 和 u 的情况下，可以在 O(1) 时间内得到 y 和 v，因此时间复杂度是 O(n ^ 2)。
        # 故总时间复杂度是 O(n ^ 2)。
        # 空间复杂度：O(n ^ 2)。空间复杂度取决于预处理时创建的二维数组 order 和数组 match，其大小分别为 n×n 和 n，因此空间复杂度是 O(n ^ 2)。
        # 执行用时：52 ms, 在所有 Python 提交中击败了100.00 % 的用户
        # 内存消耗：23.3 MB, 在所有 Python 提交中击败了33.33 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]], 2),
        (2, [[1], [0]], [[1, 0]], 0),
        (4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]], 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.unhappyFriends(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
