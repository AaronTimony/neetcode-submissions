# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Need to track height, and if there is another node
        
        def dfs(root):
            if not root:
                return (True, 0)

            left, l_h = dfs(root.left)
            right, r_h = dfs(root.right)

            balanced = left and right and abs(r_h - l_h) <= 1

            height = 1 + max(l_h, r_h)

            return (balanced, height)

        return dfs(root)[0]
