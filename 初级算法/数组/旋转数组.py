# https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # for i in range(1, n+1):
        #     # print(i)
        #     if (k + i) % n == 0:
        #         break
        # for i in range(i):
        #     tmp = nums[0]
        #     nums.pop(0)
        #     nums.append(tmp)
        # # print(nums)
        # return nums

        # 使用临时数组
        # n = len(nums)
        # tmp = [0]*n
        # for i in range(n):
        #     tmp[i] = nums[i]
        # for i in range(n):
        #     nums[(i + k) % n] = tmp[i]
        # return nums

        # 多次反转
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)
        return nums

        # k %= len(nums)
        # nums[:] = nums[-k:]+nums[:-k]
        # return nums
