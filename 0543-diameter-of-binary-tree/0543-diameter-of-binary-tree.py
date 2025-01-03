# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            diameter = left_height + right_height
            self.res = max(self.res, diameter)

            return 1 + max(left_height,right_height)
        dfs(root)
        return self.res