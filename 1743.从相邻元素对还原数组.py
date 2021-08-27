# -*- encoding: utf-8 -*-
'''
@File    :   1743.从相邻元素对还原数组.py
@Time    :   2021/07/25 02:24:32
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/
'''
from typing import List


class Solution(object):
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 1. 哈希表
        # https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/solution/cong-xiang-lin-yuan-su-dui-huan-yuan-shu-v55t/
        res = {}
        for a, b in adjacentPairs:
            if res.get(a):
                if res.get(b):
                    m, n = res[a][-1], res[b][-1]
                    res[m] = res[a][::-1]+res[b]
                    res[n] = res[m][::-1]
                    del res[a], res[b]
                else:
                    res[res[a][-1]].append(b)
                    res[a].insert(0, b)
                    res[b] = res[a]
                    del res[a]
            else:
                if res.get(b):
                    res[res[b][-1]].append(a)
                    res[b].insert(0, a)
                    res[a] = res[b]
                    del res[b]
                else:
                    res[a] = [a, b]
                    res[b] = [b, a]
        return res[list(res.keys())[0]]
        # 复杂度分析
        # 时间复杂度：O(n)，其中 n 是原数组的长度。我们只需要遍历每一个元素一次。
        # 空间复杂度：O(n)，其中 n 是原数组的长度。主要为哈希表的开销。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[2, 1], [3, 4], [3, 2]], [1, 2, 3, 4]),
        ([[4, -2], [1, 4], [-3, 1]], [-2, 4, 1, -3]),
        ([[100000, -100000]], [100000, -100000]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.restoreArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
