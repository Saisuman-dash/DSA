# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def addleft(root,isleft):
            net=0
            if root is None:
                return 0
            if root.left is None and root.right is None and isleft:
                net+=root.val
            if root.left is None and root.right is None:
                net+=0
            leftsum=addleft(root.left,True)
            rightsum=addleft(root.right,False)
            return leftsum+rightsum+net
        return addleft(root,False)
            