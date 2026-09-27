# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subroot):
            def same(node, subroot):
                if not node and not subroot:#ot,
                    return True
                elif not node or not subroot:
                    return False
                if node.val!=subroot.val:
                    return False
                return same(node.left, subroot.left) and same(node.right, subroot.right)# else: return True              
            if not node: return False
          #  if node.val==subroot.val:
        #        return same(node.left, subroot.left) and same(node.right, subroot.right)    
           # else:
                
            return same(node, subroot) or dfs(node.left, subroot) or dfs(node.right, subroot)    
               # return dfs(node.left, subroot) or dfs(node.right, subroot)    
              #  dfs(node.right, subroot)
        return dfs(root, subRoot)    


