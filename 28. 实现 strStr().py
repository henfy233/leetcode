# -*- encoding: utf-8 -*-
'''
@File    :   28. 实现 strStr().py
@Time    :   2021/07/29 20:08:24
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/implement-strstr/
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 自己写，第四个样例过不去
        # left = 0
        # startAt = 0
        # if needle == "":
        #     return 0
        # m = len(haystack)
        # n = len(needle)
        # while left < m:
        #     startAt = left
        #     right = 0
        #     while left < m and right < n and haystack[left] == needle[right]:
        #         left += 1
        #         right += 1
        #     if right == n:
        #         return startAt
        #     left = startAt
        #     left += 1
        # return -1

        # 1. 滑动窗口
        n = len(haystack)
        left = 0
        right = len(needle)
        if right == 0:
            return 0
        while right <= n:
            if haystack[left: right] == needle:
                return left
            left += 1
            right += 1
        return -1

        # 2. 官方API
        # return haystack.find(needle)

        # 3. KMP算法
        # def getNext(p, next):
        #     np = len(p)
        #     i = 0
        #     j = -1
        #     next[0] = -1
        #     # 这个默认的，匹配的时候是当前字符的前一个和前面的匹配，所以最后一个是不参与匹配的，可以看strStr方法的注释，
        #     while i < np - 1:
        #         if j == -1 or p[i] == p[j]:
        #             # 如果j不等于-1，指定的字符相等，那么i和j要往后移一位，这点很好理解，如果j为-1的时候，i往后移移位，j置为0
        #             # 重新开始匹配。next[i]是匹配成功的数量
        #             i += 1
        #             j += 1
        #             next[i] = j
        #         else:
        #             # 关键是这里不好理解，为什么匹配失败要让next[j]等于j，要记住这里的next[j]是指匹配成功的数量，有可能为0，也有可能是其他数.比如
        #             # 字符串ABCABXYABCABATDM, 对应的next数组为{-1	0	0	0	1	2	0	0	1	2	3	4	5	1	0	0	}
        #             j = next[j]
        # n = len(needle)
        # if n == 0:
        #     return 0
        # i = 0
        # j = 0
        # # 数组next表示pattern指定的下标前具有相同的字符串数量，语言组织能力不好，可能不是太好理解，我举个例子吧
        # # ，比如ABCABA，数组next[0]是-1，这个是固定的，因为第一个A前面是没有字符的，next[1]是0，因为B的前面就一个A，没有
        # # 重复的，所以是0, 同理next[2]也是, next[3]也是0, 而next[4]是1，因为next[4]所指向的是第二个B，第二个B前面有一个A和
        # # 第一个A相同，所以是1, next[5]是2，因为next[5]所指向的是最后一个Ａ，因为前面的Ａ对比成功，并且Ｂ也对比成功，所以是２，
        # # 也就是ＡＢ两个字符串匹配成功, 再举个例子，比如WABCABA，数组除了第一个为-1，其他的都是为0，因为只有第一个匹配成功之后
        # # 才能匹配后面的，虽然后面的AB和前面的AB匹配成功，但是后面AB的前面是C和前面AB的前面一个W不匹配，所以后面的匹配都是0.
        # # 要记住只有指定字符前面的字符和第一个字符匹配成功的时候才能往后匹配，否则后面的永远都是先和第一个匹配。
        # next = [0]*n
        # getNext(needle, next)
        # while i < len(haystack) and j < n:
        #     # 这里j等于-1的时候也只有在下面next数组赋值的时候才会出现，并且只有在数组next[0]的时候才会等于-1，
        #     # 其他时候是没有的，这一点要谨记，待会下面求next数组的时候就会用到。这里可以这样来理解，如果j不等于-1，
        #     # 并且下标i和j所指向的字符相等，那么i和j分别往后移一位继续比较，这个很好理解，那么如果j == -1的时候，就表示
        #     # 就表示前面没有匹配成功的，同时i往后移一位，j置为0（j == -1的时候，j++为0），再从0开始比较。
        #     if j == -1 or haystack[i] == needle[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         # i = i - j + 1
        #         # j = 0
        #         # 返回到指定的位置，不是返回到匹配失败的下一个位置，这里都好理解，重点是求数组next。
        #         # 这里只要j等于0，在next[j]赋值的之后，j就会等于-1；因为next[0]等于-1
        #         j = next[j]
        #         # j回到指定位置
        #     if j == n:
        #         return i - j
        # return -1


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("mississippi", "issip", 4)
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.strStr(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
