# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptrA = head
        ptrB = head.next
        try:
            while ptrB.next != None:
                ptrC = ptrB
                ptrD = ptrB.next

                while ptrD.next != None:
                    ptrC = ptrD
                    ptrD = ptrD.next
                
                ptrA.next = ptrD
                ptrD.next = ptrB
                ptrC.next = None
                ptrA = ptrB
                ptrB = ptrB.next
        except:
            pass