# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []

        result = []
        size = 1
        queue = deque([root])

        while queue:
            level = []
            
            for i in range(len(queue)):
                if queue:
                    node = queue.popleft()
                if node:
                    level.append(node.val)
                else: continue
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
        