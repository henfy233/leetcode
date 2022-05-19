# -*- encoding: utf-8 -*-
'''
@File    :   剑指 Offer 50. 第一个只出现一次的字符.py
@Time    :   2022/04/25 18:04:05
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
'''


from collections import defaultdict
import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 自己写 哈希表
        # res = defaultdict(dict)
        # for i in s:
        #     # print(i)
        #     if i not in res:
        #         res[i] = 1
        #     else:
        #         res[i] += 1
        # for i in res:
        #     if res[i] == 1:
        #         return i
        #     # print(i, res[i])
        # return ' '
        '''
        作者：jyd
        链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        '''
        # 哈希表
        # dic = {}
        # for c in s:
        #     dic[c] = not c in dic
        # for c in s:
        #     if dic[c]:
        #         return c
        # return ' '

        # 有序哈希表
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v:
                return k
        return ' '


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ("abaccdeff", 'b'),
        ("", ' '),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.firstUniqChar(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
