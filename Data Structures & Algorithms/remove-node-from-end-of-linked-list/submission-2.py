# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        remove = head
        prev = None
        tail = head
        index = 0 

        while tail:
            tail = tail.next
            index += 1
        
        for i in range(index-n):
            prev = remove
            remove = remove.next

        if index == 1 or index == 0:
            return
        if index == n:
            return head.next

        prev.next = remove.next

        return head