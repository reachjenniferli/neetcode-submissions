class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        node = head
        length = 0

        while node.next != None:
            length += 1
            node = node.next

        node = head
        
        for i in range(length // 2):
            node = node.next

        first_half_end = node
        prev = None
        node = node.next
        first_half_end.next = None

        while node != None:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        
        h1, h2 = head, prev
        while h2:
            nxt1 = h1.next
            nxt2 = h2.next
            h1.next = h2
            h2.next = nxt1
            h1 = nxt1
            h2 = nxt2