# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid=True
        def dfs(node, low, high):
            if not node or self.valid==False:
                return
           # if node.left and node.val <= node.left.val:#>= node.left.val:# or node.val<=node.right.val:
               # self.valid=False
               # return    
           # elif node.right and node.val>=node.right.val:
           #     self.valid =False   
            if node.val<=low or node.val>=high:
                self.valid=False
                return
            dfs(node.left, low, node.val)    
            dfs(node.right, node.val, high)
        dfs(root, float('-inf'), float('inf'))    
        return self.valid
