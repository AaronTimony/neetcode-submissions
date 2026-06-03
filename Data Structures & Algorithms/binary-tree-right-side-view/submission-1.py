# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q= deque()
        q.append(root)
        res = []
        if not root:
            return []

        while q:
            original_stack_length = len(q)
            for i in range(len(q)):
                node = q.popleft()
                
                if i == original_stack_length - 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return res
