#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   457. 环形数组是否存在循环.py
@Time    :   2021/08/07 21:19:03
@Author  :   henfy
@Diffi   :   easy
@Version :   1.0
'''

# here put the import lib


# 这道题连题目都还没看懂，我傻了
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 自己写，所有 nums[seq[j]] 应当不是全正就是全负，这个问题难解
        # n = len(nums)
        # d = {}
        # for index in range(n):
        #     tar = index
        #     index = (index + nums[index]+n) % n
        #     while (index+1) % n != tar+1:
        #         d[index] = True
        #         index = (index + nums[index]+n) % n
        #         if (index+1) % n == tar+1:
        #             return True
        #         if index in d:
        #             return False
        # return False

        # 1. 快慢指针
        # 思路及算法：
        # 我们可以将环形数组理解为图中的 n 个点，nums[i] 表示 i 号点向(i+nums[i]) mod n 号点连有一条单向边。
        # 注意到这张图中的每个点有且仅有一条出边，这样我们从某一个点出发，沿着单向边不断移动，最终必然会进入一个环中。而依据题目要求，我们要检查图中是否存在一个所有单向边方向一致的环。
        # 我们可以使用在无向图中找环的一个经典算法：快慢指针来解决本题，参考题解「141. 环形链表」。

        # 为了降低时间复杂度，我们可以标记每一个点是否访问过，过程中如果我们的下一个节点为已经访问过的节点，则可以停止遍历。
        # 在实际代码中，我们无需新建一个数组记录每个点的访问情况，而只需要将原数组的对应元素置零即可（题目保证原数组中元素不为零）。遍历过程中，如果快慢指针相遇，或者移动方向改变，那么我们就停止遍历，并将快慢指针经过的点均置零即可。
        # 特别地，当 nums[i] 为 n 的整倍数时，i 的后继节点即为 i 本身，此时循环长度 k = 1，不符合题目要求，因此我们需要跳过这种情况。

        n = len(nums)
        # 保证返回值在 [0,n) 中

        def next(cur):
            return (cur + nums[cur]) % n
        # 具体地，我们检查每一个节点
        for i, num in enumerate(nums):
            if num == 0:
                continue
            # 令快慢指针从当前点出发
            slow, fast = i, next(i)
            # 判断非零且方向相同
            # 期间每移动一次，我们都需要检查当前单向边的方向是否与初始方向是否一致
            # 如果不一致，我们即可停止遍历，因为当前路径必然不满足条件
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                # 快指针每次移动两步，慢指针每次移动一步
                slow = next(slow)
                fast = next(next(fast))
            add = i
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0
        return False
        # 复杂度分析：
        # 时间复杂度：O(n)，其中 n 是环形数组的长度。我们至多遍历每个点四次，其中快指针两次，慢指针一次，置零标记一次。
        # 空间复杂度：O(1)。我们只需要常数的空间保存若干变量。
        # 执行用时：24 ms, 在所有 Python 提交中击败了52.17 % 的用户
        # 内存消耗：13 MB, 在所有 Python 提交中击败了82.61 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([2, -1, 1, -2, -2], False),
        ([2, -1, 1, 2, 2], True),
        ([-1, 2], False),
        ([-2, 1, -1, -2, -2], False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.circularArrayLoop(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
