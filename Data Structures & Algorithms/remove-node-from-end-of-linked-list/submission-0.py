# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        ptrA = head

        while ptrA != None:
            length += 1
            ptrA = ptrA.next
        
        removePos = length - n # 0 would mean first, 1 second and so on.

        if removePos == 0:
            return head.next
        # print(length)
        i = 1

        ptrA = head.next
        ptrB = head

        while i != removePos:
            i += 1
            ptrB = ptrA
            ptrA = ptrA.next
        
        ptrB.next = ptrA.next
        ptrA.next = None
        
        return head