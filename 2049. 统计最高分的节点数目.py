# -*- encoding: utf-8 -*-
'''
@File    :   2049. 统计最高分的节点数目.py
@Time    :   2022/03/12 11:43:05
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/count-nodes-with-the-highest-score/
'''


from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # 有点难
        # 深度优先搜索
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size
        dfs(0)
        return cnt


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([-1, 2, 0, 2, 0], 3),
        ([-1, 2, 0], 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countHighestScoreNodes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
