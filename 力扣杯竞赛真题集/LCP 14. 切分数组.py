# -*- encoding: utf-8 -*-
'''
@File    :   LCP 14. 切分数组.py
@Time    :   2021/09/06 22:39:07
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/qie-fen-shu-zu/
'''


from typing import List


# 遇到困难题，直接copy，后续学习，套积分
# class Solution:
#     def splitArray(self, nums: List[int]) -> int:

# 1.质数筛 + DP
# https://leetcode-cn.com/problems/qie-fen-shu-zu/solution/qie-fen-shu-zu-zhi-shu-shai-dp-by-leetcode-solutio/
max_num = 1000000
min_factor = [1] * (max_num + 1)
p = 2

# O(M loglog M)
while (p <= max_num):
    i = p
    while i * p <= max_num:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1

    p += 1
    while p <= max_num:
        if min_factor[p] == 1:
            break

        p += 1


class Solution:
    def splitArray(self, nums) -> int:
        f = {}
        n = len(nums)

        x = nums[0]
        INF = 100000000
        while True:
            if min_factor[x] == 1:
                f[x] = 1
                break

            f[min_factor[x]] = 1
            x //= min_factor[x]

        min_prev = 1
        for i in range(1, n):
            x = nums[i]

            min_cur = INF
            while True:
                if min_factor[x] == 1:
                    f[x] = min(f.get(x, INF), min_prev + 1)
                    min_cur = min(min_cur, f[x])
                    break

                f[min_factor[x]] = min(f.get(min_factor[x], INF), min_prev + 1)
                min_cur = min(min_cur, f[min_factor[x]])
                x //= min_factor[x]

            min_prev = min_cur

        return min_prev
        # 执行用时：820 ms, 在所有 Python3 提交中击败了78.43 % 的用户
        # 内存消耗：36 MB, 在所有 Python3 提交中击败了54.90 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, 3, 3, 2, 3, 3], 2),
        ([2, 3, 5, 7], 4),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.splitArray(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
