#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   789. 逃脱阻碍者.py
@Time    :   2021/08/22 00:36:06
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

你在进行一个简化版的吃豆人游戏。你从 [0, 0] 点开始出发，你的目的地是 target = [xtarget, ytarget] 。
地图上有一些阻碍者，以数组 ghosts 给出，第 i 个阻碍者从 ghosts[i] = [xi, yi] 出发。所有输入均为 整数坐标 。

每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 1 个单位 的新位置。当然，也可以选择 不动 。所有动作 同时 发生。

如果你可以在任何阻碍者抓住你 之前 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。
如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。

只有在你有可能成功逃脱时，输出 true ；否则，输出 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/escape-the-ghosts
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


# 说实话，从来没做过这种大题，真难受
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # 1. 曼哈顿距离
        # 为了逃脱阻碍者，玩家应按照最短路径向目的地移动。阻碍者为了抓住玩家，也会按照最短路径向目的地移动。
        # 由于每次移动为向四个方向之一移动一个单位，因此对于玩家和阻碍者而言，到达目的地的最短路径的距离为当前所在位置和目的地的曼哈顿距离。
        source = [0, 0]
        distance = manhattanDistance(source, target)
        for ghost in ghosts:
            if manhattanDistance(ghost, target) <= distance:
                return False
        return True
        # return all(manhattanDistance(ghost, target) > distance for ghost in ghosts)


def manhattanDistance(point1: List[int], point2: List[int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
# 复杂度分析
# 时间复杂度：O(n)，其中 n 是数组 ghosts 的长度。需要计算玩家和目的地的距离，以及遍历数组 ghosts 计算每个阻碍者和目的地的距离。
# 空间复杂度：O(1)。
# 执行用时：40 ms, 在所有 Python3 提交中击败了47.95 % 的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了16.44 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[1, 0], [0, 3]], [0, 1], True),
        ([[1, 0]], [2, 0], False),
        ([[2, 0]], [1, 0], False),
        ([[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]], [7, 7], False),
        ([[-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0]], [0, 0], True),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.escapeGhosts(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
