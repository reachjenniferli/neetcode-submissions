# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val != subRoot.val:
                return False
            
            left = same(root.left, subRoot.left)
            right = same(root.right, subRoot.right)

            return left and right

        def dfs(root, subRoot):
            if not root:
                return False
            if same(root, subRoot):
                return True
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

