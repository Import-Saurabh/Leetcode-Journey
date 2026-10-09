class TreeNode:
    def __init___(self,left=0,right=None):
        self.val=0
        self.left=left
        self.right=right
class Solution:
    def preorderTraversal(self,root:TreeNode|None)-> list[int]:
        result=[]
        if root is None:
            return None
        def preorder(node):
            result.append(node.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return result
                    