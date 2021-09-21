# -*- encoding: utf-8 -*-
'''
@File    :   650. 只有两个键的键盘.py
@Time    :   2021/09/19 12:36:35
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/2-keys-keyboard/
'''


# 不会做，比想象中复杂,数学题
class Solution:
    def minSteps(self, n: int) -> int:
        # 1. 动态规划
        # https://leetcode-cn.com/problems/2-keys-keyboard/solution/zhi-you-liang-ge-jian-de-jian-pan-by-lee-ussa/
        # f = [0] * (n + 1)
        # for i in range(2, n + 1):
        #     f[i] = float("inf")
        #     j = 1
        #     while j * j <= i:
        #         if i % j == 0:
        #             f[i] = min(f[i], f[j] + i // j)
        #             f[i] = min(f[i], f[i // j] + j)
        #         j += 1
        # return f[n]

        # 2. 分解质因数
        # https://leetcode-cn.com/problems/2-keys-keyboard/solution/zhi-you-liang-ge-jian-de-jian-pan-by-lee-ussa/
        ans = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
                ans += i
            i += 1
        if n > 1:
            ans += n
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (2, 2),
        (3, 3),
        (1, 0),
        (5, 5),
        (8, 6),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.minSteps(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
