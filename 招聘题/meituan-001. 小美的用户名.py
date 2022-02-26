# -*- encoding: utf-8 -*-
'''
@File    :   meituan-001. 小美的用户名.py
@Time    :   2021/09/11 16:38:38
@Author  :   henfy
@Diffi   :   Easy
@Version :   1.0

题目：https://leetcode-cn.com/problems/BaR9fy/
'''

# 找别人的题解，不会做
# https://leetcode-cn.com/problems/BaR9fy/solution/cpython3java-mo-ni-shu-ru-you-hua-jia-su-299c/
T = int(input())
for _ in range(T):
    s = input()
    ok = True
    if not(s[0].isalpha()):
        ok = False

    cnt1 = 0
    cnt2 = 0
    if ok == True:
        for c in s:
            if c.isdigit():
                cnt1 += 1
            elif c.isalpha():
                cnt2 += 1
            else:
                ok = False
                break

    if ok == True and cnt1 > 0 and cnt2 > 0:
        print("Accept")
    else:
        print("Wrong")

# https://leetcode-cn.com/problems/BaR9fy/solution/meituan-001-xiao-mei-de-yong-hu-ming-pyt-m1n7/
# nums = int(input())
# for _ in range(nums):
#     ret, li = True, [False, False]
#     strs = input()
#     if not (strs[0].islower() or strs[0].isupper()):
#         ret = False

#     for i in strs:
#         if i.islower() or i.isupper():
#             li[0] = True
#         elif i.isdigit():
#             li[1] = True
#         else:
#             ret = False
#             break
#     if not all(li):
#         ret = False
#     print("Accept" if ret else "Wrong")
