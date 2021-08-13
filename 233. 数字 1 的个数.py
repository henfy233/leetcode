#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   233. 数字 1 的个数.py
@Time    :   2021/08/13 08:54:04
@Author  :   henfy
@Diffi   :   hard
@Version :   1.0

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-digit-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib


# 回看了字符串的整数反转，运用了while条件,但是超出时间了
# 看完发现原来用数学解题目，牛的
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 自己写，超出时间限制，没时间，还是看答案吧
        # sum = 0
        # for s in range(0, n+1, 10):
        #     # print('s', s)
        #     while s != 0:
        #         tail = s % 10
        #         s //= 10
        #         if tail == 1:
        #             sum += 1
        # return sum

        # 1. 枚举每一数位上 1 的个数
        '''
        思路:
        根据题目要求，我们需要统计[0, n] 范围内所有整数中，数字 1 出现的个数。由于 n 的范围最大为 2 × 10 ^ 9，它是一个 10 位整数，因此我们可以考虑枚举每一个数位，分别统计该数位上数字 1 出现的次数，最后将所有数位统计出的次数进行累加即可得到答案。
        为了直观地叙述我们的算法，下面我们以「百位」进行举例，对于几个不同的 n 手动计算出答案，随后扩展到任意数位。
        以 n = 1234567 为例，我们需要统计「百位」上数字 1 出现的次数。我们知道，对于从 0 开始每 1000 个数，「百位」上的数字 1 都会出现 100 次，即数的最后三位每 100 个数都呈现[000, 999] 的循环，其中的[100, 199] 在「百位」上的数字为 1，共有 100 个。
        n 拥有 1234 个这样的循环，每个循环「百位」上都出现了 100 次 1，这样就一共出现了 1234 × 100 次 1。如果使用公式表示，那么这部分出现的 1 的次数为：⌊ n / 1000 ⌋ × 100
        其中 x 表示将 x 向下取整，那么 ⌊ n / 1000 ⌋ 就表示 n 拥有的完整的[000, 999] 循环的数量。
        对于剩余不在完整的循环中的部分，最后三位为[000, 567]，其中 567 可以用 n mod 1000 表示，其中 mod 表示取模运算。记 n' = n mod 1000，这一部分在「百位」上出现 1 的次数可以通过分类讨论得出：
        - 当 n' < 100 时，「百位」上不会出现 1；
        - 当 100≤ n′ <200 时，「百位」上出现 1 的范围为[100, n']，所以出现了 n' - 100 + 1次 1；
        - 当 n' ≥200 时，「百位」上出现了全部 100 次 1。

        作者：LeetCode-Solution
        链接：https: // leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode-solution-zopq/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        算法:
        我们可以从小到大枚举 k。如果 n ≥ 10 ^ k ，说明 n 包含 10 ^ k对应的数位，我们通过(1) 式计算这一数位 1 的个数并累加，否则退出枚举。
        '''

        # mulk 表示 10^k
        # 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        # 但为了让代码看起来更加直观，这里保留了 k
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + \
                min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans
        # 复杂度分析
        # 时间复杂度：O(logn)。n 包含的数位个数与 n 呈对数关系。
        # 空间复杂度：O(1)。
        # 执行用时：16 ms, 在所有 Python 提交中击败了67.16 % 的用户
        # 内存消耗：12.9 MB, 在所有 Python 提交中击败了61.19 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (13, 6),
        (0, 0),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countDigitOne(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
