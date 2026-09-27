# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, maximum):#:, ):
            if not node:
                return 
            if node.val>=maximum:#<=maximum:
                self.res+=1
            maximum=max(node.val, maximum)       
            dfs(node.left, maximum)#, res) 
            dfs(node.right, maximum)#, res)
            return 
       # return 
        dfs(root, root.val)#, 0)#root,-, 0)    
        return self.res