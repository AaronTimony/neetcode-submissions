# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The furthest left node will have the smallest value, then you can
        # just climb up by one each time.

        count = 0
        ans = None

        def dfs(root):
            nonlocal count
            nonlocal ans

            if not root or ans is not None:
                return
            
            dfs(root.left)

            count += 1
            if count == k:
                ans = root.val
                return

            dfs(root.right)

        dfs(root)
        return ans
