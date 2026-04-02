# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        if not root:
            return res

        def dfs(node, curr):
            nonlocal res

            if not node:
                return
            curr += 1
            res = max(curr, res)
            
            dfs(node.left, curr)
            dfs(node.right, curr)
        
        dfs(root, 0)
        return res
            

            
