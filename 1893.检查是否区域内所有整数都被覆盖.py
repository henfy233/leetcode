#
# @lc app=leetcode.cn id=1893 lang=python
#
# [1893] 检查是否区域内所有整数都被覆盖
#

# @lc code=start
# https: // leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/solution/yi-ti-san-jie-bao-li-you-hua-chai-fen-by-w7xv/
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # print(ranges)
        # t = left
        # flag = 0
        # tmp = 0
        # for i, j in ranges:
        #     print('i', i)
        #     print('j', j)
        #     print('t', t)
        #     print('flag', flag)
        #     if flag == 1 and i - tmp > 1:
        #         print('tmp', tmp)
        #         return False

        #     if i < t and j < t:
        #         tmp = j
        #         continue
        #     if i <= t and j >= t:
        #         print('i >= t and j >= t')
        #         tmp = j
        #         t = right
        #         flag += 1
        #         if flag == 2:
        #             return True
        #         continue
        #     return False
        # return False

        # 暴力
        # flag = [0]*1000086
        # for l, r in ranges:
        #     for i in range(l, r+1):
        #         flag[i] = True
        # for i in range(left, right+1):
        #     if flag[i]:
        #         continue
        #     else:
        #         return False
        # return True

        # 基于排序 不知怎么对ranges数组排序
        # ranges.sort()
        # for l, r in ranges:
        #     if l <= left and left <= r:
        #         left = r + 1
        # return left > right

        # 优化 只标记[left, right] 取交集思想
        # flag = [False]*51
        # for i, j in ranges:
        #     L = max(i, left)
        #     R = min(j, right)
        #     for x in range(L, R+1):
        #         # print('x', x)
        #         flag[x] = True
        # for i in range(left, right+1):
        #     # print('i', i)
        #     if flag[i] == False:
        #         return False
        # return True

        # 差分数组 前缀和不仅能查询是否被覆盖，还能查询某一区间被覆盖几次
        flag = [0]*52
        for i, j in ranges:
            flag[i] += 1
            flag[j+1] -= 1

        for i in range(1, len(flag)):
            flag[i] += flag[i-1]

        for i in range(left, right+1):
            if flag[i] <= 0:
                return False
        return True
        # @lc code=end
