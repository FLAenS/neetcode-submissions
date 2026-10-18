# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            left_good = dfs(node.left, low, node.val)
            right_good = dfs(node.right, node.val, high)
            return left_good and right_good
        return dfs(root, float('-inf'), float('inf'))