class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {} #val -> (parent, how to get from par)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parents[node.left.val] = (node.val, 'L')
            if node.right:
                stack.append(node.right)
                parents[node.right.val] = (node.val, 'R')
        def path(val):
            res = []
            while val != root.val:
                p, d = parents[val]
                val = p
                res.append(d)
            return res[::-1]
        s = path(startValue)
        d = path(destValue)
        i = 0
        while i < len(s) and i < len(d) and s[i] == d[i]:
            i += 1
        return 'U' * (len(s) - i) + ''.join(d[i:])
