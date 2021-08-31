# -*- encoding: utf-8 -*-
'''
@File    :   242. 有效的字母异位词.py
@Time    :   2021/07/28 23:59:05
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/valid-anagram/
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        # 遍历s全部存进哈希表，相同的加一
        for i in s:
            if i in ds:
                ds[i] += 1
            else:
                ds[i] = 1
        for i in t:
            if i in ds and ds[i] != 0:
                ds[i] -= 1
            else:
                return False
        # 遍历哈希表，不为0则不同
        for i in ds:
            if ds[i] != 0:
                return False
        return True

        # 也可以计数法 通过字母的ASCII码相减可作为索引存进数组

        # 1. python 使用 collections.Counter 将字符串转换为 hashmap 格式
        # return collections.Counter(s) == collections.Counter(t)

        # 2. python 将字符串排序，然后比对字符串是否相等
        # return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("ab", "a", False),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.isAnagram(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
