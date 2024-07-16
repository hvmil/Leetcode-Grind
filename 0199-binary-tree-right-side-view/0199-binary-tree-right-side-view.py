# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightmost_node = None
            q_length = len(q)

            for i in range(q_length):
                node = q.popleft()
                if node:
                    rightmost_node = node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost_node:
                res.append(rightmost_node.val)
        return res
        