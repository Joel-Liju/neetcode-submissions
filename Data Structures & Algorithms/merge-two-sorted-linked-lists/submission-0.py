# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        solution = None
        ptr3 = solution
        ptr1 = list1
        ptr2 = list2

        while ptr1 != None and ptr2!= None:
            
            # print(ptr1.val, ptr2.val)
            if ptr1.val <= ptr2.val:
                addValue = ptr1.val 
                ptr1 = ptr1.next
            else:
                addValue = ptr2.val
                ptr2 = ptr2.next

            if solution is None:
                solution = ListNode(addValue, None)
                ptr3 = solution
            else:
                ptr3.next = ListNode(addValue, None)
                ptr3 = ptr3.next
            # print("addedValue : ", ptr3.val)
        
        while ptr1 != None:
            addValue = ptr1.val
            if solution is None:
                solution = ListNode(addValue, None)
                ptr3 = solution
            else:
                ptr3.next = ListNode(addValue, None)
                ptr3 = ptr3.next
            ptr1 = ptr1.next

        while ptr2 != None:
            addValue = ptr2.val
            if solution is None:
                solution = ListNode(addValue, None)
                ptr3 = solution
            else:
                ptr3.next = ListNode(addValue, None)
                ptr3 = ptr3.next 
            ptr2 = ptr2.next
        return solution