# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # save next node
        if head:
            node = head.next
        else:
            return head
        prev = head

        # point curr node to prev
        head.next = None

        while node != None:
            # save next node
                next_node = node.next
            # point curr node to prev
                node.next = prev
            # update save 
                prev = node
                node = next_node

        return prev
