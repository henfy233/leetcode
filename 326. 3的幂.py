# -*- encoding: utf-8 -*-
'''
@File    :   326. 3的幂.py
@Time    :   2021/08/03 23:55:00
@Author  :   henfy
@Diffi   :   Easy
@Version :   2.0

题目：https://leetcode-cn.com/problems/power-of-three/
'''
# 进阶：你能不使用循环或者递归来完成本题吗？

# 5/3在leetcode中为整数，在这里为浮点数，有问题


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 自己做 一直除以3
        # if n > 1:
        #     while n % 3 == 0:
        #         n /= 3
        # return n == 1
        # 执行用时：72 ms, 在所有 Python3 提交中击败了77.33 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.53 % 的用户

        # 1. 试除法
        # https://leetcode-cn.com/problems/power-of-three/solution/3de-mi-by-leetcode-solution-hnap/
        # while n and n % 3 == 0:
        #     n //= 3
        # return n == 1

        # 2. 递归解决
        # return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3)))
        # 执行用时：148 ms, 在所有 Python 提交中击败了97.53 % 的用户
        # 内存消耗：13.2 MB, 在所有 Python 提交中击败了14.25 % 的用户

        # 3. 循环
        # if n <= 0:
        #     return False
        # i = 1
        # while i <= n:
        #     if i == n:
        #         return True
        #     i *= 3
        #     # print('i', i)
        # return False

        # 4. 算术表达式计算
        # import math
        # if n <= 0:
        #     return False
        # return (math.log(n) / math.log(3)) % 1 == 0

        # 5. 判断是否为最大 33 的幂的约数
        # https://leetcode-cn.com/problems/power-of-three/solution/3de-mi-by-leetcode-solution-hnap/
        # 题中n的范围是-2 ^ 31 <= n <= 2 ^ 31 - 1，而在这个范围内3的最大幂是1162261467，
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
