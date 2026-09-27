# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(node, heap):
            if not node: 
                return 

            if len(heap) < k:
                heapq.heappush_max(heap, node.val)
            elif node.val < heap[0]:
                heapq.heapreplace_max(heap, node.val)

            left = dfs(node.left, heap)
            right = dfs(node.right, heap)

        dfs(root, heap)

        return heapq.heappop_max(heap)
