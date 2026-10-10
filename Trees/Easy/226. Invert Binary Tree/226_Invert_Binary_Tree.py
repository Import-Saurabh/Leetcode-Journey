# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        def invert(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)

        invert(root)
        return root