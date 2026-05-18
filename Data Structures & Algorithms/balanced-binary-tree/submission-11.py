class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root) != -1

    def dfs(self, curr) -> int:
        if not curr:
            return 0
        
        left = self.dfs(curr.left)
        if left == -1:
            return -1
            
        right = self.dfs(curr.right)
        if right == -1:
            return -1
            
        if abs(left - right) > 1:
            return -1
            
        return 1 + max(left, right)