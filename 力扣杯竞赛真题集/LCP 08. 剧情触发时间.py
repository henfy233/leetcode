# -*- encoding: utf-8 -*-
'''
@File    :   LCP 08. 剧情触发时间.py
@Time    :   2021/09/06 15:59:52
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/ju-qing-hong-fa-shi-jian/
'''


from typing import List
import bisect


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        # 自己写，超出输出限制，尽力了
        # increase = [[0, 0, 0]] + increase
        # print(increase)
        # ans = [-1]*len(requirements)
        # print(ans)
        # sum = [0]*3
        # for i in range(len(increase)):
        #     print('i', i)
        #     for j in range(3):
        #         sum[j] += increase[i][j]
        #     print('sum', sum)
        #     for k in range(len(requirements)):
        #         print('requirements[k]', requirements[k])
        #         flag = True
        #         for j in range(3):
        #             if flag and requirements[k][j] > sum[j]:
        #                 flag = False
        #         if flag and ans[k] == -1:
        #             ans[k] = i
        #         # sum[j] += increase[i][j]
        # print('ans', ans)
        # return ans

        # 1. 简化问题
        # https://leetcode-cn.com/problems/ju-qing-hong-fa-shi-jian/solution/ju-qing-hong-fa-shi-jian-by-leetcode-solution/
        # a = [0 for i in range(3)]
        # # 将剧情的下标记录在story中，方便映射结果
        # requirements = [x + [i] for i, x in enumerate(requirements)]
        # # 将requirements按三种维度分别排序，得到 s
        # s = [sorted(requirements, key=lambda x: x[i]) for i in range(3)]
        # index = [0 for i in range(3)]

        # n = len(requirements)
        # trigger = [0 for i in range(n)]
        # ans = [-1 for i in range(n)]
        # # 枚举每一天
        # for d, (na, nb, nc) in enumerate(increase):
        #     # 计算当天的属性
        #     a[0] += na
        #     a[1] += nb
        #     a[2] += nc
        #     # 遍历三种属性的排序序列，计算当前可以被触发的剧情
        #     for i in range(3):
        #         while index[i] < n and a[i] >= s[i][index[i]][i]:
        #             trigger[s[i][index[i]][-1]] += 1
        #             # 如果某个剧情触发次数等于3次(三种属性均触发，剧情被实际触发)
        #             if trigger[s[i][index[i]][-1]] == 3:
        #                 ans[s[i][index[i]][-1]] = d + 1
        #             index[i] += 1
        # # 第0天单独考虑
        # for i, (na, nb, nc, _) in enumerate(requirements):
        #     if na == 0 and nb == 0 and nc == 0:
        #         ans[_] = 0
        # return ans
        # 时间复杂度：O(n∗log(n))。对属性的排序为整体的时间复杂度瓶颈。
        # 空间复杂度：O(n)。
        # 执行用时：596 ms, 在所有 Python3 提交中击败了40.68 % 的用户
        # 内存消耗：62.9 MB, 在所有 Python3 提交中击败了15.25 % 的用户

        # 2. 木桶原理 前缀和 简单粗暴
        # https://leetcode-cn.com/problems/ju-qing-hong-fa-shi-jian/solution/c-python3-qian-zhui-he-er-fen-cha-zhao-m-uhto/
        n = len(increase)
        a = [0]  # 前缀和  虚指 题目的天数也是虚指（从1开始）
        b = [0]
        c = [0]
        for x, y, z in increase:
            a.append(a[-1] + x)
            b.append(b[-1] + y)
            c.append(c[-1] + z)
        res = []
        for x, y, z in requirements:
            loc_a = bisect.bisect_left(a, x)  # 寻找符合条件的最左
            loc_b = bisect.bisect_left(b, y)
            loc_c = bisect.bisect_left(c, z)
            loc = max(loc_a, loc_b, loc_c)  # 3个条件都符合，才触发
            if loc <= n:
                res.append(loc)
            else:
                res.append(-1)
        return res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([[2, 8, 4], [2, 5, 0], [10, 9, 8]], [[2, 11, 3], [
         15, 10, 7], [9, 17, 12], [8, 1, 14]], [2, -1, 3, -1]),
        ([[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]], [[12, 11, 16], [
         20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]], [-1, 4, 3, 3, 3]),
        ([[1, 1, 1]], [[0, 0, 0]], [0]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.getTriggerTime(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
