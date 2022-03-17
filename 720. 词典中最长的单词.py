# -*- encoding: utf-8 -*-
'''
@File    :   720. 词典中最长的单词.py
@Time    :   2022/03/17 12:20:16
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/longest-word-in-dictionary/
'''


from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None or not node.children[ch].isEnd:
                return False
            node = node.children[ch]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 哈希集合
        # words.sort(key=lambda x: (-len(x), x), reverse=True)
        # print('words', words)
        # longest = ""
        # candidates = {""}
        # for word in words:
        #     if word[:-1] in candidates:
        #         longest = word
        #         candidates.add(word)
        # return longest

        # 字典树
        t = Trie()
        for word in words:
            t.insert(word)
        longest = ""
        for word in words:
            if t.search(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                longest = word
        return longest


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.longestWord(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
