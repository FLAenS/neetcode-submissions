# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, cur_max):
            if not node:
                return 0
            nonlocal cnt
            if node.val >= cur_max:
                cnt += 1
            new_max = max(cur_max, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        dfs(root, root.val)
        return cnt
                

        