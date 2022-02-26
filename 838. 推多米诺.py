# -*- encoding: utf-8 -*-
'''
@File    :   838. 推多米诺.py
@Time    :   2022/02/21 12:13:01
@Author  :   henfy
@Diffi   :   Middle
@Version :   1.0

题目：https://leetcode-cn.com/problems/push-dominoes/
'''


from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 不会
        # l = []
        # left, right = 0, 0
        # n = len(dominoes)-1
        # while left < n:
        #     print(right, dominoes[right])
        #     if dominoes[right] == 'L':
        #         for i in range(left, right):
        #             print('i', i)
        #             # dominoes[i] = 'L'
        #             l.append('L')
        #     elif dominoes[right] == 'R':
        #         left = right
        #     right += 1
        # print(l)
        # return dominoes

        # 广度优先搜索
        # n = len(dominoes)
        # q = deque()
        # time = [-1] * n
        # force = [[] for _ in range(n)]
        # for i, f in enumerate(dominoes):
        #     if f != '.':
        #         q.append(i)
        #         time[i] = 0
        #         force[i].append(f)

        # res = ['.'] * n
        # while q:
        #     i = q.popleft()
        #     if len(force[i]) == 1:
        #         res[i] = f = force[i][0]
        #         ni = i - 1 if f == 'L' else i + 1
        #         if 0 <= ni < n:
        #             t = time[i]
        #             if time[ni] == -1:
        #                 q.append(ni)
        #                 time[ni] = t + 1
        #                 force[ni].append(f)
        #             elif time[ni] == t + 1:
        #                 force[ni].append(f)
        # return ''.join(res)

        # 模拟
        s = list(dominoes)
        n, i, left = len(s), 0, 'L'
        while i < n:
            j = i
            while j < n and s[j] == '.':  # 找到一段连续的没有被推动的骨牌
                j += 1
            right = s[j] if j < n else 'R'
            if left == right:  # 方向相同，那么这些竖立骨牌也会倒向同一方向
                while i < j:
                    s[i] = right
                    i += 1
            elif left == 'R' and right == 'L':  # 方向相对，那么就从两侧向中间倒
                k = j - 1
                while i < k:
                    s[i] = 'R'
                    s[k] = 'L'
                    i += 1
                    k -= 1
            left = right
            i = j + 1
        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("RR.L", "RR.L"),
        (".L.R...LR..L..", "LL.RR.LLRRLL..")
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.pushDominoes(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
