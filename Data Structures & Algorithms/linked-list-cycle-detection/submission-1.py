# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            turtle = head.next
            hare = head.next.next
            while turtle != hare:
                turtle = turtle.next
                hare = hare.next.next
            return True
        except:
            return False