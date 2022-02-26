# -*- encoding: utf-8 -*-
'''
@File    :   2. 心算挑战.py
@Time    :   2021/09/11 15:13:12
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/contest/season/2021-fall/problems/uOAnQW/
'''


from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        print(cards)
        n = len(cards)
        dp = [[0, 0] for _ in range(cnt+1)]
        print('dp', dp)
        list0 = {}
        list1 = {}
        for i in range(1, cnt+1):
            print('i', i)
            flag0, flag1 = True, True
            for j in range(n):
                print('cards[j]', cards[j])
                for k in range(2):
                    tmp = dp[i-1][k] + cards[j]
                    if tmp % 2 == 0 and tmp > dp[i][0] and j not in list0:
                        dp[i][0] = tmp
                        list0[j] = cards[j]
                    elif tmp % 2 == 1 and tmp > dp[i][1] and j not in list1:
                        dp[i][1] = tmp
                        list1[j] = cards[j]

                # if cards[j] % 2 == 0 and flag0 and j not in list0:
                #     dp[i][0] = dp[i-1][0] + cards[j]
                #     list0[j] = 1
                #     flag0 = False
                # elif cards[j] % 2 == 1 and flag1 and j not in list1:
                #     dp[i][1] = dp[i-1][1] + cards[j]
                #     list1[j] = 1
                #     flag1 = False
                # if not flag0 and not flag1:
                #     break
        print('dp', dp)
        return dp[cnt][0]

        # for x in range(n-cnt):
        #     for y in range(x+1, n-cnt):
        # ans = sum(cards[:cnt-1])
        # for i in range(cnt, n):
        #     ans += cards[i]
        #     # print('ans', ans)
        #     if ans % 2 == 0:
        #         return ans
        #     else:
        #         ans -= cards[i]
        # return 0


if __name__ == '__main__':
    s = Solution()
    test_list = [
        ([1, 2, 8, 9], 3, 18),
        ([3, 3, 1], 1, 0),
        ([8, 9, 2, 4], 3, 14),
    ]

    for test_index, test_case in enumerate(test_list, start=1):
        *test, result = test_case
        test_result = s.maxmiumScore(*test)
        if test_result != result:
            raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (
                test_index, result, test_result))
        print("test_case %d succeed." % test_index)
