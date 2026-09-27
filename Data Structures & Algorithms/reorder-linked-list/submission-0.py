# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        tail = head
        prev = None
        second = head

        index = 1

        #count indexes and find last element
        while tail.next: 
            tail = tail.next
            index += 1
        
        #get to second half
        for i in range(index//2):
            second = second.next

        #reverse second half
        while second:
            print(second.val)
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        curr = head
        print(curr.val)
        other = tail
        print(other.val)

        while curr:
            nxt = curr.next
            curr.next = other
            curr = other
            other = nxt

        return 