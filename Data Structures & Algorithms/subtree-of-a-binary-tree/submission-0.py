# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        q = deque([root])

        while q:
            node = q.pop()

            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False


    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False
