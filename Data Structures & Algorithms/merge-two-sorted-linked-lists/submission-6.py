# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            if not list1 and not list2:
                return
            elif not list1:
                return list2
            elif not list2:
                return list1

        if list1.val < list2.val: 
            curr, other = list1, list2
        else: 
            curr, other = list2, list1
        head, nxt = curr, curr.next
        
        while list1 and list2:
            if nxt == None:
                curr.next = other
                break

            if nxt.val < other.val:
                curr = nxt
                #nxt = nxt.next
            elif nxt.val >= other.val:
                curr.next = other
                curr = other
                #nxt = other.next
                other = nxt
            
            nxt = curr.next
        
        return head