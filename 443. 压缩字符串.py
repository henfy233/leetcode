#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   443. 压缩字符串.py
@Time    :   2021/08/21 00:42:07
@Author  :   henfy
@Diffi   :   middle
@Version :   1.0

给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
 - 如果这一组长度为 1 ，则将字符追加到 s 中。
 - 否则，需要向 s 追加字符，后跟这一组的长度。

压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。
需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-compression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


# 12 整型从头取，一时想不清怎么取，淦
class Solution:
    def compress(self, chars: List[str]) -> int:
        # 有点复杂，不太好修改
        # count = 1
        # temp = chars[0]
        # ans = 0
        # for i in range(1, len(chars)):
        #     if chars[i] == temp:
        #         count += 1
        #     else:
        #         ans += 1
        #         if count == 1:
        #             temp = chars[i]
        #             continue
        #         while count != 0:
        #             ans += 1
        #             count //= 10
        #         count = 1
        #     temp = chars[i]
        # ans += 1
        # print(ans)
        # if count == 1:
        #     return ans
        # while count != 0:
        #     ans += 1
        #     reverse(chars,)
        #     count //= 10
        # # ans.append(list(count))
        # print(ans)
        # return ans

        # 1. 双指针
        # 思路和算法
        # 为了实现原地压缩，我们可以使用双指针分别标志我们在字符串中读和写的位置。每次当读指针 read 移动到某一段连续相同子串的最右侧，我们就在写指针 write 处依次写入该子串对应的字符和子串长度即可。
        # 在实际代码中，当读指针 read 位于字符串的末尾，或读指针 read 指向的字符不同于下一个字符时，我们就认为读指针 read 位于某一段连续相同子串的最右侧。该子串对应的字符即为读指针 read 指向的字符串。我们使用变量 left 记录该子串的最左侧的位置，这样子串长度即为 read−left+1。
        # 特别地，为了达到 O(1) 空间复杂度，我们需要自行实现将数字转化为字符串写入到原字符串的功能。这里我们采用短除法将子串长度倒序写入原字符串中，然后再将其反转即可。
        def reverse(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        n = len(chars)
        write = left = 0
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                num = read - left + 1
                if num > 1:
                    anchor = write
                    while num > 0:
                        chars[write] = str(num % 10)
                        write += 1
                        num //= 10
                    reverse(anchor, write - 1)
                left = read + 1
        return write
        # 复杂度分析
        # 时间复杂度：O(n)，其中 n 为字符串长度，我们只需要遍历该字符串一次。
        # 空间复杂度：O(1)。我们只需要常数的空间保存若干变量。
        # 执行用时：36 ms, 在所有 Python3 提交中击败了78.17 % 的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了68.11 % 的用户


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["a", "a", "b", "b", "c", "c", "c"], 6),
        (["a"], 1),
        (["a", "b", "b", "b", "b", "b", "b", "b", "b",
         "b", "b", "b", "b"], 4),
        (["a", "a", "b", "b", "c", "c", "c"], 6),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.compress(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
