# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # We want to find the max depth on left and right, then add them
        maxLeft = self.maxHeight(root.left)
        maxRight = self.maxHeight(root.right)
        throughRoot = maxLeft + maxRight
        leftWay = self.diameterOfBinaryTree(root.left)
        rightWay = self.diameterOfBinaryTree(root.right)
        return max(throughRoot, leftWay, rightWay)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        