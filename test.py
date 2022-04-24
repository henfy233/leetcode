st = []
st.append(1)
st.append(4)
st.pop()
st.pop()


# hashmap = dict()

# hashmap[1] = 'b'

# hashmap.values

# print(hashmap)
# hashmap.pop(0)

# map1 = list()
# map1.insert(1, 'opo')
# print(map1)
# map1.index()


# def findKthLargest(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     # inf = int(1e9)
#     # maxnum = -inf
#     # print(nums)
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j+1] < nums[j]:
#                 tmp = nums[j+1]
#                 nums[j+1] = nums[j]
#                 nums[j] = tmp
#     # print(nums)
#     return nums[-k]


# if __name__ = '__main__':
# nums = [3, 2, 1, 5, 6, 4]
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# print(findKthLargest(nums, 4))


# if __name__ == '__main__':
#     d = {'a': 1, 'b': 2}
#     print(d.has_key('a'))
