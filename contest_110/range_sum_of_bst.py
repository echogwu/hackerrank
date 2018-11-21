# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        s = 0
        if root is None:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        elif L <= root.val <= R:
            s += root.val
            s += self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        return s


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(3)
e = TreeNode(7)
f = TreeNode(18)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
s = Solution()
print(s.rangeSumBST(a, 7, 15))
