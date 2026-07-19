# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        
        def fractree(p,q):
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if q is None and p is not None:
                return False
            if p.val!=q.val:
                return False
            outer = fractree(p.left,q.right)
            inner = fractree(p.right,q.left)
            if outer and inner:
                return True
            else:
                return False
        return fractree(p,q)

        











        # if p is None and q is None:
        #     return True
        # if p is None and q is not None:
        #     return False
        # if q is None and p is not None:
        #     return False
        # if p.val == q.val:
        #     return True
        
        # left2left=isSymmetric(p.left)
        # right2left=isSymmetric(q.left)
        # left2right=isSymmetric(p.right)
        # right2right=isSymmetric(q.right)
        # if left2left and right2right:
        #     leftside = True
        # else :
        #     leftside=False
        # if left2right and right2left:
        #     rightside=True
        # else:
        #     rightside=False
        # if leftside and rightside:
        #     return True
        # else:
        #     return False

