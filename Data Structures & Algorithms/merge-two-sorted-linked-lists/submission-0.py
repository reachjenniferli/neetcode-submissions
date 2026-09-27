# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        head = ListNode()
        current = head

        while ptr1 or ptr2:
            if ptr1 == None:
                while ptr2:
                    current.next = ListNode(ptr2.val)
                    ptr2 = ptr2.next
                    current = current.next
                    print("1")
            elif ptr2 == None:
                while ptr1:
                    current.next = ListNode(ptr1.val)
                    ptr1 = ptr1.next
                    current = current.next
                    print("2")
            elif ptr1.val <= ptr2.val:
                current.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
                current = current.next
                print("3")
            elif ptr2.val < ptr1.val:
                current.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
                current = current.next
                print("4")

        

        return head.next
