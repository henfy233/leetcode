# -*- encoding: utf-8 -*-
'''
@File    :   326. 3的幂.py
@Time    :   2021/08/03 23:55:00
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/power-of-three/
'''
# 进阶：你能不使用循环或者递归来完成本题吗？

# 5/3在leetcode中为整数，在这里为浮点数，有问题


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1. 一直除以3 我用的是这种方法，但有点问题
        # if n > 1:
        #     while n % 3 == 0:
        #         n /= 3
        # return n == 1
        # 执行用时：168 ms, 在所有 Python 提交中击败了86.58 % 的用户
        # 内存消耗：13.3 MB, 在所有 Python 提交中击败了5.75 % 的用户

        # 2. 递归解决
        # return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3)))
        # 执行用时：148 ms, 在所有 Python 提交中击败了97.53 % 的用户
        # 内存消耗：13.2 MB, 在所有 Python 提交中击败了14.25 % 的用户

        # 3. 算术表达式计算 有问题，跑不出结果
        # import math
        # return (math.log(n, 10) / math.log(3, 10)) % 1 == 0

        # 4. 题中n的范围是-2 ^ 31 <= n <= 2 ^ 31 - 1，而在这个范围内3的最大幂是1162261467，
        # 在比他大就超过int表示的范围了，我们直接用它对n求余即可，过求余的结果是0，说明n是3的幂次方
        return n > 0 and 1162261467 % n == 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (27, True),
        (0, False),
        (9, True),
        (45, False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isPowerOfThree(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
