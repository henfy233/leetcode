#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#
import random
# @lc code=start


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 暴力解法，冒泡排序，返回下标k-1 自己写的
        # for i in range(len(nums)):
        #     for j in range(len(nums)-i-1):
        #         if nums[j+1] < nums[j]:
        #             tmp = nums[j+1]
        #             nums[j+1] = nums[j]
        #             nums[j] = tmp
        # return nums[-k]

        # 暴力解法
        # https: // leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
        # size = len(nums)
        # nums.sort()
        # return nums[size-k]

        # 维护一个堆，建立容量为k的最小值堆
        # 模式识别：维护动态数据的最大最小值，可以考虑堆
        # python没试过堆的数据结构

        # https: // leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcode-/
        # 快速选择
        # 关键字：第K个
        # 模式识别：确定数据量的情况下寻找第k大的数，可以利用快速选择算法
        # 快速选择算法：快速排序算法中的轴值计算
        size = len(nums)
        target = size - k
        left = 0
        right = size - 1
        while(True):
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1

    def __partition(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left
        for i in range(left+1, right+1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

# @lc code=end
