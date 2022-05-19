# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 48. 最长不含重复字符的子字符串.py
@Time    :   2022/05/12 18:39:33
@Author  :   henfy
@Diffi   :   Middle

题目：https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 不会
        # 动态规划 + 哈希表
        # dic = {}
        # res = tmp = 0
        # for j in range(len(s)):
        #     i = dic.get(s[j], -1)  # 获取索引 i
        #     dic[s[j]] = j  # 更新哈希表
        #     tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
        #     res = max(res, tmp)  # max(dp[j - 1], dp[j])
        # return res

        # 动态规划 + 线性遍历
        res = tmp = i = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]:
                i -= 1  # 线性查找 i
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res

        # 双指针 + 哈希表
        # dic, res, i = {}, 0, -1
        # for j in range(len(s)):
        #     if s[j] in dic:
        #         i = max(dic[s[j]], i)  # 更新左指针 i
        #     dic[s[j]] = j  # 哈希表记录
        #     res = max(res, j - i)  # 更新结果
        # return res


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.lengthOfLongestSubstring(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
