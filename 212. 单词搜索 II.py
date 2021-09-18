# -*- encoding: utf-8 -*-
'''
@File    :   212. 单词搜索 II.py
@Time    :   2021/09/16 17:26:59
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/word-search-ii/
'''

from collections import defaultdict
from typing import List


# 不会做

# 1. 回溯 + 字典树
# https://leetcode-cn.com/problems/word-search-ii/solution/dan-ci-sou-suo-ii-by-leetcode-solution-7494/


# class Trie:
#     def __init__(self):
#         self.children = defaultdict(Trie)
#         self.word = ""

#     def insert(self, word):
#         cur = self
#         for c in word:
#             cur = cur.children[c]
#         cur.is_word = True
#         cur.word = word


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         for word in words:
#             trie.insert(word)

#         def dfs(now, i1, j1):
#             if board[i1][j1] not in now.children:
#                 return

#             ch = board[i1][j1]

#             now = now.children[ch]
#             if now.word != "":
#                 ans.add(now.word)

#             board[i1][j1] = "#"
#             for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
#                 if 0 <= i2 < m and 0 <= j2 < n:
#                     dfs(now, i2, j2)
#             board[i1][j1] = ch

#         ans = set()
#         m, n = len(board), len(board[0])

#         for i in range(m):
#             for j in range(n):
#                 dfs(trie, i, j)

#         return list(ans)


# 2. 删除被匹配的单词
# https://leetcode-cn.com/problems/word-search-ii/solution/dan-ci-sou-suo-ii-by-leetcode-solution-7494/


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            nxt = now.children[ch]
            if nxt.word != "":
                ans.append(nxt.word)
                nxt.word = ""

            if nxt.children:
                board[i1][j1] = "#"
                for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                    if 0 <= i2 < m and 0 <= j2 < n:
                        dfs(nxt, i2, j2)
                board[i1][j1] = ch

            if not nxt.children:
                now.children.pop(ch)

        ans = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], [
         "i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.findWords(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
