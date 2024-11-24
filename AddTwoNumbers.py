# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        result = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1 != None:
                total += l1.val
                l1 = l1.next
            
            if l2 != None:
                total += l2.val
                l2 = l2.next

            value = total % 10
            carry = total // 10

            node = ListNode(value)

            dummy.next = node
            dummy = dummy.next
        
        return result.next
        # [2] -> [4] -> [3]
        # [5] -> [6] -> [4] + 1
   #[] -> [7] -> [0] -> [8]