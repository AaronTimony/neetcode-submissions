# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        stack = [root]
        if root.val == p.val or root.val == q.val:
            return root

        while stack:
            node = stack.pop()
            if min(q.val, p.val) <= node.val <= max(p.val, q.val):
                return node

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)