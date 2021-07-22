# https: // qingfengpython.cn/  # /markdown/Algorithm/%E9%93%BE%E8%A1%A8/%E5%89%91%E6%8C%87Offer52.%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%85%AC%E5%85%B1%E8%8A%82%E7%82%B9

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 哈希集合
        # d = {}
        # while headA:
        #     d[headA] = headA
        #     headA = headA.next
        # while headB:
        #     if d.get(headB):
        #         return headB
        #     headB = headB.next
        # return None

        # 双指针
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
