# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(root):
            if root is None:
                return root
            if root.left is None and root.right is None:
                return root
            lefttree=swap(root.left)
            righttree=swap(root.right)
            root.left=righttree
            root.right=lefttree
            return root
        return swap(root)
        
