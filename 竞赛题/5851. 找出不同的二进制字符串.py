# -*- encoding: utf-8 -*-
'''
@File    :   5851. 找出不同的二进制字符串.py
@Time    :   2021/08/22 10:44:35
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

https://leetcode-cn.com/contest/weekly-contest-255/problems/find-unique-binary-string/
'''
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n = len(nums)
        # for i in range(2**n):
        #     # print('{:0'+str(n)+'b}')
        #     print("Binary value of ", i, " is: ",
        #           '{:0'+str(n)+'b}'.format(i))
        #     # if "{{:0"+str(n)+"b}}".format(i) not in nums:
        #     #     return "{{:0"+str(n)+"b}}".format(i)
        # return False
        # def dfs(depth: int) -> str:
        #     if depth==0:
        #         return
        #     return dfs(depth-1)
        # dfs(n)

        # 1. 转化为整数
        # 链接：https://leetcode-cn.com/problems/find-unique-binary-string/solution/zhao-chu-bu-tong-de-er-jin-zhi-zi-fu-chu-0t10/
        # n = len(nums)
        # vals = {int(num, 2) for num in nums}
        # val = 0
        # while val in vals:
        #     val += 1
        # res = "{:b}".format(val)
        # return '0'*(n-len(res))+res
        # 复杂度分析
        # 时间复杂度：O(n ^ 2)，其中 n 为 nums 的长度。预处理哈希集合的时间复杂度为 O(n ^ 2)，寻找第一个不在哈希表中的整数与生成答案字符串的时间复杂度为 O(n)。
        # 空间复杂度：O(n)，即为哈希集合的空间复杂度。

        # 2. 康托对角线
        # 解题思路
        # 只要和第i个串下标i的字符nums[i][i]不同，构造出来的串就和所有的串都不同。
        # 只限于串数不超过串长的情况。
        # 时间复杂度O(n)。
        # 链接：https://leetcode-cn.com/problems/find-unique-binary-string/solution/kang-tuo-dui-jiao-xian-by-seedjyh-wr2s/
        n = len(nums)
        ans = ''
        for i in range(n):
            if nums[i][i] == '0':
                ans += '1'
            else:
                ans += '0'
        return ans
        # 另一种一行代码解法
        # return ''.join(chr(ord(nums[i][i]) ^ 1) for i in range(len(nums)))
        # 执行用时：32 ms, 在所有 Python3 提交中击败了100.00 % 的用户
        # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了66.67 % 的用户


if __name__ == '__main__':
    s = Solution()
    # 答案不唯一
    test_list = [
        (["01", "10"], "11"),
        (["00", "01"], "11"),
        (["111", "011", "001"], "101"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findDifferentBinaryString(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
