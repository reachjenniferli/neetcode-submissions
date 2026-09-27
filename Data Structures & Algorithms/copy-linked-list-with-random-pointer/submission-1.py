"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        
        copymap = {}

        curr = head

        while curr:
            currCopy = Node(curr.val)
            copymap[curr] = currCopy
            curr = curr.next

        curr = head

        while curr:
            if curr.next:
                copymap[curr].next = copymap[curr.next]
            if curr.random:
                copymap[curr].random = copymap[curr.random]
            curr = curr.next

        return copymap[head]
        

        
