# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def traverse(root):
    if root is None:
        return

    nodes.append(root)
    traverse(root.left)
    traverse(root.right)
    traverse(p)
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)  
        )  
p = [1,2,3]
q = [1,2,3]  
s1=Solution()
print(s1.isSameTree(p, q))
      