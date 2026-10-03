class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        
        return check(root, root)