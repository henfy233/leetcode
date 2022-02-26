# -*- encoding: utf-8 -*-
'''
@File    :   1994. 好子集的数目.py
@Time    :   2022/02/22 13:39:39
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/the-number-of-good-subsets/
'''


from typing import Counter, List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # 完全不会

        # 状态压缩动态规划
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10**9 + 7

        freq = Counter(nums)
        f = [0] * (1 << len(primes))
        f[0] = pow(2, freq[1], mod)

        for i, occ in freq.items():
            if i == 1:
                continue

            # 检查 i 的每个质因数是否均不超过 1 个
            subset, x = 0, i
            check = True
            for j, prime in enumerate(primes):
                if x % (prime * prime) == 0:
                    check = False
                    break
                if x % prime == 0:
                    subset |= (1 << j)

            if not check:
                continue

            # 动态规划
            for mask in range((1 << len(primes)) - 1, 0, -1):
                if (mask & subset) == subset:
                    f[mask] = (f[mask] + f[mask ^ subset] * occ) % mod

        ans = sum(f[1:]) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 3, 4], 6),
        ([4, 2, 3, 15], 5),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.numberOfGoodSubsets(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
