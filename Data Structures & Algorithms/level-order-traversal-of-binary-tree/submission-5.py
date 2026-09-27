# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node, level, res):
            if not node:
                return res
            if len(res) <= level:
                res.append([])   
            res[level].append(node.val)#res{}    
                #res[level].append(node.val)
            if node.left:
                bfs(node.left, level+1, res)    
            if node.right:
                bfs(node.right, level+1, res)
            return res
        return bfs(root, 0, [])