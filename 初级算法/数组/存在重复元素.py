class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 哈希表
        # d = dict()
        # for i in range(len(nums)):
        #     # print(i, nums[i])
        #     # print('d.get(nums[i])',d.get(nums[i]))
        #     if d.get(nums[i]):
        #         return True
        #     d[nums[i]] = i+1
        # # print(d)
        # return False

        # 排序
        # nums = sorted(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # 长度
        if len(nums) != len(set(nums)):
            return True
        return False
