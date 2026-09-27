# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 1
        max_cap = 1

        def bfs(root):
            queue = []
            result = []

            if not root:
                return []
            
            queue.append(root)
            result.append([root.val])

            while queue:
                current = []
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                        current.append(node.left.val)
                    if node.right:
                        queue.append(node.right)
                        current.append(node.right.val)
                if len(current) > 0:
                    result.append(current)

            return result

        return bfs(root)
            


                