#
# @lc app=leetcode.cn id=1818 lang=python
#
# [1818] 绝对差值和
#
import bisect
# @lc code=start
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
# [20000008,7,5]\n[2,3,5]
# [2,3,5]\n[2,3,5]
        n = len(nums1)
        total = 0
        ans = float("inf")
        sl = sorted(nums1)
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            idx = bisect.bisect_left(sl, nums2[i])
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, abs(sl[idx-1] - nums2[i]) - diff)
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total

        # sum = 0
        # list = []
        # list1 = []
        # print('nums1',len(nums1))
        # print('nums2',len(nums2))
        # for i in range(len(nums1)):
        #     diff = abs(nums1[i]-nums2[i])
        #     list.append(diff)
        #     sum += diff
        # print('list1',list)
        # print(max(list))
        # index = list.index(max(list))
        # print('index',index)
        # sum -= max(list)
        # for i in range(len(nums1)):
        #     diff = abs(nums1[i]-nums2[index])
        #     list1.append(diff)
        # print('list2',list1)
        # # index = list.index(min(list))
        # # print(index)
        # # print(nums1[index])
        # # diff = abs(nums1[index]-nums2[index])
        # sum += min(list1)
        # return sum


# @lc code=end

