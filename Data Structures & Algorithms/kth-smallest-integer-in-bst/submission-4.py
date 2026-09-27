# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap=[]
        self.k=k
        def dfs(node):
            if not node:
                return
            dfs(node.left)    
            #dfs(node.right)#(:)
            if len(self.heap)<self.k:
                heapq.heappush(self.heap, -(node.val))
            else:
                return
            dfs(node.right)    
        dfs(root)
        print(self.heap)
        return -(self.heap[0])