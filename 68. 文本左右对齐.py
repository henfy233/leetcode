# -*- encoding: utf-8 -*-
'''
@File    :   68. 文本左右对齐.py
@Time    :   2021/09/09 00:22:55
@Author  :   henfy
@Diffi   :   Hard
@Version :   1.0

题目：https://leetcode-cn.com/problems/text-justification/
'''


from typing import List


# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
# 总感觉自己做的方法有问题，算了，还是不做了
# num = 1
# sum = 0
# space = list()
# ans = list()
# for i in range(len(words)):
#     sum += len(words[i])+1
#     space.append(1)
#     if sum > maxWidth+1:
#         num += 1
#         sum -= len(words[i])+1
#         spaceNum = len(space)-2
#         print("diff", maxWidth + 1 - sum)
#         print('spaceNum', spaceNum)

#         ans.append
#         sum = 0
#         space = list()
#         sum += len(words[i])+1
#         space.append(1)
#         # for j in range(spaceNum):

#     # print('num', num)
#     # print('sum', sum)

# 1. 模拟
# https://leetcode-cn.com/problems/text-justification/solution/wen-ben-zuo-you-dui-qi-by-leetcode-solut-dyeg/
# blank 返回长度为 n 的由空格组成的字符串
def blank(n: int) -> str:
    return ' ' * n


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        right, n = 0, len(words)
        while True:
            left = right  # 当前行的第一个单词在 words 的位置
            sumLen = 0  # 统计这一行单词长度之和
            # 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1

            # 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen

            # 当前行只有一个单词：该单词左对齐，在行末填充空格
            if numWords == 1:
                ans.append(words[left] + blank(numSpaces))
                continue

            # 当前行不只一个单词
            avgSpaces = numSpaces // (numWords - 1)
            extraSpaces = numSpaces % (numWords - 1)
            # 拼接额外加一个空格的单词
            s1 = blank(avgSpaces + 1).join(words[left:left + extraSpaces + 1])
            s2 = blank(avgSpaces).join(
                words[left + extraSpaces + 1:right])  # 拼接其余单词
            ans.append(s1 + blank(avgSpaces) + s2)

        return ans
        # 时间复杂度：O(m)，其中 m 是数组 words 中所有字符串的长度之和。
        # 空间复杂度：O(m)。

        # 2. 平均分布额外空格
        # https://leetcode-cn.com/problems/text-justification/solution/text-justification-by-ikaruga/

        # 3. 硬模拟
        # https://leetcode-cn.com/problems/text-justification/solution/pythonjava-ying-mo-ni-by-himymben-jl5l/


if __name__ == '__main__':
    s = Solution()
    test_list = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16, [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]),
        (["What", "must", "be", "acknowledgment", "shall", "be"], 16, [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]),
        (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20, [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ])
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.fullJustify(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
