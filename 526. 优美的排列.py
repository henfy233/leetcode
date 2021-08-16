#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   526. 优美的排列.py
@Time    :   2021/08/16 08:44:39
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，
使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。
条件：
1. 第 i 位的数字能被 i 整除
2. i 能被第 i 位上的数字整除

现在给定一个整数 N，请问可以构造多少个优美的排列？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-arrangement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
import collections


# 要用到全排列，还不会写
class Solution(object):
    def countArrangement(self, n: int) -> int:
        # 1. 回溯
        # 思路和算法
        # 我们可以使用回溯法解决本题，从左向右依次向目标排列中放入数即可。
        # 特别地，为了优化回溯效率，我们可以预处理每个位置的符合条件的数有哪些，用二维数组 match 保存。当我们尝试向位置 index 放入数时，我们只需要遍历 match[index] 即可。
        # match = collections.defaultdict(list)
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         if i % j == 0 or j % i == 0:
        #             match[i].append(j)
        # num = 0
        # vis = set()
        # 具体地，我们定义函数 backtrack(index, n)，表示尝试向位置 index 放入数。其中 n 表示排列的长度。在当前函数中，我们首先找到一个符合条件的未被使用过的数，然后递归地执行 backtrack(index+1, n)，当该函数执行完毕，回溯到当前层，我们再尝试下一个符合条件的未被使用过的数即可。
        # def backtrack(index: int) -> None:
        #     if index == n+1:
        #         nonlocal num
        #         num += 1
        #         return
        #     for x in match[index]:
        #         # 回溯过程中，我们可以用 vis 数组标记哪些数被使用过，每次我们选中一个数 x，我们就将 vis[x] 标记为 true，回溯完成后，我们再将其置为 false。
        #         if x not in vis:
        #             vis.add(x)
        #             backtrack(index+1)
        #             vis.discard(x)
        # backtrack(1)
        # return num
        # 复杂度分析
        # 时间复杂度：O(n!)，其中 n 为排列的长度。预处理 match 数组的时间复杂度为 O(n ^ 2)，回溯的时间复杂度为 O(n!)，因此总时间复杂度为 O(n ^ 2 + n!) = O(n!)。
        # 空间复杂度：O(n ^ 2)，我们需要 O(n ^ 2) 的空间保存 match 数组，递归的栈空间大小为 O(n)，因此总空间复杂度为 O(n ^ 2 + n) = O(n ^ 2)。
        # 执行用时：452 ms, 在所有 Python3 提交中击败了80.66 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了39.92 % 的用户

        # 2. 状态压缩 + 动态规划
        # 思路和算法
        # 由于题目保证了排列的长度 n 至多为 15，因此我们可以用一个位数为 n 的二进制数 mask 表示排列中的数被选取的情况。若 mask 中的第 i 位为 1（从 0 开始编号），则数 i+1 已经被选取，否则就还未被选取。我们可以利用这样的二进制数表示选取数的过程的状态，以 n = 4, mask = (0110)_2为例，这代表数 2, 3 都已经被选取，并以任意顺序放置在排列中前两个位置。
        # 令f[mask] 表示状态为 mask 时的可行方案总数，这样答案即为 f[2 ^ n - 1]。
        # 其中 num(mask) 表示二进制数 mask 中 1 的个数，x∣y 表示 x 可以整除 y。

        # 状态转移方程的含义为，当我们想要计算 f[mask] 时，我们只需要在前 num(mask)−1 位都已经放置了数的情况下，考虑第 num(mask) 位要放置的数即可，我们枚举当前位的符合条件的数，并将方案数累加到 f[mask] 中即可。

        # 作者：LeetCode-Solution
        # 链接：https://leetcode-cn.com/problems/beautiful-arrangement/solution/you-mei-de-pai-lie-by-leetcode-solution-vea2/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]
        return f[(1 << n) - 1]
        # 复杂度分析
        # 时间复杂度：O(n × 2 ^ n)，其中 nn 为排列的长度。我们需要 O(2 ^ n) 的时间枚举所有状态，每个状态需要 O(n) 的时间检查所有符合条件的数。因此总时间复杂度为 O(n × 2 ^ n)。
        # 空间复杂度：O(2 ^ n)，其中 n 为排列的长度。我们需要 O(2 ^ n) 的空间保存状态。


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (6, 36),
        (2, 2),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.countArrangement(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
