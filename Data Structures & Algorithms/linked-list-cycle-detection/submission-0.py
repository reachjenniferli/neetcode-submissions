# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.val = 'a'
        
        curr = head

        while curr:
            nxt = curr.next 

            if curr.next == None: 
                return False
            elif curr.next == 'a':
                return True

            curr.next = 'a'
            curr = nxt



