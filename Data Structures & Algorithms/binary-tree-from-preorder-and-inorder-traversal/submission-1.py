# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {}
        for i in range(len(inorder)):
            pos[inorder[i]] = i

        pre = 0
        def dfs(l, r):
            nonlocal pre
            if l > r:
                return None
            val = preorder[pre]
            root = TreeNode(val)
            mid = pos[val]
            pre += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)

        