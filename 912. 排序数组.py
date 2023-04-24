# -*- encoding: utf-8 -*-
'''
@File    :   912. 排序数组.py
@Time    :   2023/04/19 13:46:52
@Author  :   henfy
@Diffi   :   Middle
@Method  :   快排、堆排、归并排序
@Question:   https://leetcode.cn/problems/sort-an-array/
@Answer  :   https://leetcode.cn/problems/sort-an-array/solutions/178305/pai-xu-shu-zu-by-leetcode-solution/
'''

from typing import List
import random

# TODO 不会，记得做

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
      # 作弊写法
      # nums.sort()
      # return nums

# 1.快速排序
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#       self.randomizedQuicksort(nums, 0, len(nums) - 1)
#       return nums

#     def randomizedQuicksort(self, nums, l, r):
#       if l < r:
#           pos = self.randomizedPartition(nums, l, r)
#           self.randomizedQuicksort(nums, l, pos - 1)
#           self.randomizedQuicksort(nums, pos + 1, r)

#     def randomizedQuicksort(self, nums, l, r):
#         i = random.randint(0, r - l + 1) + l # 随机选一个作为我们的主元
#         nums[r], nums[i] = nums[i], nums[r]
#         # swap(nums, r, i)
#         return self.partition(nums, l, r)

#     def partition(self, nums, l, r):
#         pivot = nums[r]
#         i = l - 1
#         for j in range(l,r-1):
#         # (int j = l; j <= r - 1; ++j) :
#             if nums[j] <= pivot:
#                 i = i + 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[r], nums[i+1] = nums[i+1], nums[r]
#         # swap(nums, i + 1, r);
#         return i + 1

# 2.堆排序
# 先将待排序的序列建成大根堆，使得每个父节点的元素大于等于它的子节点。
class Solution:
    def heap_sort(self, nums):
      # self.build_heap(nums)
      for i in range(len(nums)-1, -1, -1):
        print(i)
        nums[i], nums[0] = nums[0], nums[i]


    def sortArray(self, nums: List[int]) -> List[int]:
      self.heap_sort(nums)
      return nums



if __name__ == '__main__':
   s = Solution()
   test_list = [
       ([5,2,3,1], [1,2,3,5]),
       ([5,1,1,2,0,0], [0,0,1,1,2,5])
   ]

   for test_index, test_case in enumerate(test_list, start=1):
       *test, result = test_case
       test_result = s.sortArray(*test)
       if test_result != result:
           raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (test_index, result, test_result))
       print("test_case %d succeed." % test_index)
