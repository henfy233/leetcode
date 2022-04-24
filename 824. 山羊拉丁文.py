# -*- encoding: utf-8 -*-
'''
@File    :   824. 山羊拉丁文.py
@Time    :   2022/04/21 15:07:05
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/goat-latin/
'''


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # ans, i, n = "", 0, len(sentence)
        # index = 0
        # ma = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # while i < n:
        #     left = i
        #     isHead, isAdd = True, False
        #     while i < n and isHead:
        #         isHead = False
        #         if sentence[i] in ma:
        #             isAdd = True

        #     while i < n and sentence[i] != ' ':
        #         i += 1

        #     index += 1

        #     if isAdd:
        #         ans += sentence[left:i]
        #         ans += 'ma'
        #         for _ in range(index):
        #             ans += 'a'
        #     else:
        #         # ans += sentence[left+1:i]+sentence[left]
        #         ans += sentence[left+1:i]
        #         ans += sentence[left]
        #         ans += 'ma'
        #         for _ in range(index):
        #             ans += 'a'
        #     if i < n:
        #         ans += ' '
        #     i += 1
        # # print('ans', ans)
        # return ans

        # 找到每一个单词 + 模拟
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        n = len(sentence)
        i, cnt = 0, 1
        words = list()

        while i < n:
            j = i
            while j < n and sentence[j] != " ":
                j += 1

            cnt += 1
            if sentence[i] in vowels:
                words.append(sentence[i:j] + "m" + "a" * cnt)
            else:
                words.append(sentence[i+1:j] + sentence[i] + "m" + "a" * cnt)

            i = j + 1

        return " ".join(words)


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
        ("The quick brown fox jumped over the lazy dog",
         "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.toGoatLatin(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
