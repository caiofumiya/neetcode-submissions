# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        max_depR = self.dfs(root.right)
        max_depL = self.dfs(root.left)

        print(max_depL, max_depR)

        if abs(max_depL - max_depR) > 1:
            return False
        return True

    def dfs(self,curr) -> int:
            if not curr:
                return 0
            
            left = self.dfs(curr.left)
            right = self.dfs(curr.right)

            return 1 + max(left, right)