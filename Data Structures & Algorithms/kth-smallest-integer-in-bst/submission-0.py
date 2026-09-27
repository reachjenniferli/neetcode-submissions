# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: 
            return

        def size(root):
            if not root:
                return
            left = 0
            right = 0
            if root.left:
                left = (1 + size(root.left))
            if root.right:
                right = (1 + size(root.right))
            return left + right
        
        leftsize = size(root.left)+1 if root.left else 0

        if (leftsize + 1) > k:
            return self.kthSmallest(root.left, k)
        elif (leftsize + 1) == k:
            return root.val
        else:
            return self.kthSmallest(root.right, k-leftsize-1)