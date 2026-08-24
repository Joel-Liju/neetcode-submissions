# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    sol = None
    def reverseListHelper(self, ptrB, ptrF):
        if ptrF.next == None:
            global sol
            ptrF.next = ptrB
            sol = ptrF
            return
        self.reverseListHelper(ptrF, ptrF.next)

        ptrF.next = ptrB

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        self.reverseListHelper(None, head)
        return sol