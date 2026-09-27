# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            if not p and not q: 
                return True
            elif not p or not q: 
                return False
            if p.val != q.val:
                return False
            
            left = same(p.left, q.left)
            right = same(p.right, q.right)

            return left and right

        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right or same(node, subRoot)

        return dfs(root)
