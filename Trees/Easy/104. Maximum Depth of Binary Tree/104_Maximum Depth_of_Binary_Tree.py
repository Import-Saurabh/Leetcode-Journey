class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1