# -*- encoding: utf-8 -*-
'''
@File    :   面试题 10.02. 变位词组.py
@Time    :   2021/07/18 00:45:11
@Author  :   henfy
@Diffi   :   Medium
@Version :   1.0

题目：https://leetcode-cn.com/problems/group-anagrams-lcci/
'''


from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        flag = []
        book = []
        li = []
        for index, word in enumerate(strs):
            print(index, word)
            tmp = []
            if word == "":
                li = [26]
            for id, ch in enumerate(word):
                tmp.append(ord(ch)-97)
                li = sorted(tmp)
                # print('li', li)
            if li not in book:
                book.append(li)
                flag.append([word])
            else:
                id = book.index(li)
                # print(id)
                flag[id].append(word)
        # print(book)
        return flag


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.groupAnagrams(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
