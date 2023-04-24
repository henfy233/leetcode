# -*- encoding: utf-8 -*-
'''
@File    :   15. 三数之和.py
@Time    :   2023/04/23 19:26:20
@Author  :   henfy
@Diffi   :   Middle
@Method  :   排序 + 双指针
@Question:   https://leetcode.cn/problems/3sum/
@Answer  :   https://leetcode.cn/problems/3sum/solutions/39722/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
'''


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      # NOTE 继续练习
      # 排序 + 双指针
      res = []
      n = len(nums)
      if not nums or n<3:
        return []
      nums.sort()
      # print(nums)
      for i in range(n):
        # 如果遍历的起始元素大于0，就直接退出
        # 原因，此时数组为有序的数组，最小的数都大于0了，三数之和肯定大于0
        if nums[i]>0 :
          return res
          # 去重，当起始的值等于前一个元素，那么得到的结果将会和前一次相同
        if i>0 and nums[i]==nums[i-1]:
          continue
        l = i+1
        r = n-1
        # 当 l 不等于 r时就继续遍历
        while l<r:
          # print(i, l ,r)
          # 将三数进行相加
          sum = nums[i] + nums[l] + nums[r]
          if sum == 0:
            # 将三数的结果集加入到结果集中
            res.append([nums[i], nums[l], nums[r]])
            # 在将左指针和右指针移动的时候，先对左右指针的值，进行判断
            # 如果重复，直接跳过
            # 去重，因为 i 不变，当此时 l取的数的值与前一个数相同，所以不用在计算，直接跳
            while l<r and nums[l]==nums[l+1]:
              l+=1
            # 去重，因为 i不变，当此时 r 取的数的值与前一个相同，所以不用在计算
            while l<r and nums[r]==nums[r-1]:
              r-=1
              # 将 左指针右移，将右指针左移
            l+=1
            r-=1
            # 如果结果大于0，将右指针左移
          elif sum > 0:
            r -= 1
            # 如果结果小于0，将左指针右移
          else:
            l += 1
      return res


if __name__ == '__main__':
   s = Solution()
   test_list = [
       ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
       ([0,1,1], []),
       ([0,0,0], [[0,0,0]])
   ]

   for test_index, test_case in enumerate(test_list, start=1):
       *test, result = test_case
       test_result = s.threeSum(*test)
       if test_result != result:
           raise ValueError("\n testcase %d error:\n expect: %s \n actually %s" % (test_index, result, test_result))
       print("test_case %d succeed." % test_index)
