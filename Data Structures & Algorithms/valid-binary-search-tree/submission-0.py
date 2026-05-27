# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def dfs(root, curMin, curMax):
            curr = root

            if not curr:
                return True

            if curr.val >= curMax or curr.val <= curMin:
                return False

            return (dfs(curr.left, curMin, curr.val) and dfs(curr.right, curr.val, curMax))

        return dfs(root, float('-inf'), float('inf'))


