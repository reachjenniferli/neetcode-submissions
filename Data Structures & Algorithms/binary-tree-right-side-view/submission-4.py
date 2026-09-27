# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level, res):# 
            if not node:
                return res
            if len(res)==level:#<level:
                res.append(node.val)#,    
            #if node.right:
                #return dfs(node.right, level+1, res)    
           # else: 
                #return dfs(node.left, level+1, res)    
           # returin 
            dfs(node.right, level+1, res)
          #  return 
            dfs(node.left, level+1, res)   
            return res 
        return dfs(root, 0, [])#-, [])    