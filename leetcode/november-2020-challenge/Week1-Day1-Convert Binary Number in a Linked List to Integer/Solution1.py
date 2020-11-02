# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        temp = head
        while temp != None:
            temp = temp.next
            n += 1
        n -= 1
        
        res = 0
        while head != None:
            res += (int(2**(n)) * head.val)
            n -= 1
            head = head.next
        return res
