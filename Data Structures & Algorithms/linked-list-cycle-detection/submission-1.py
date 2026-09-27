# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.val = 'a'
        
        #curr = head

        while head:
            nxt = head.next 

            if head.next == None: 
                return False
            elif head.next == 'a':
                return True

            head.next = 'a'
            head = nxt



