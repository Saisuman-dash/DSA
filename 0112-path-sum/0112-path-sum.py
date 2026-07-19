# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root is None:
        #     return 0
        # if root.left is None and root.right is None :
        #     return root.val
        tlsl,tlsr=0,0
        if root is None:
            return False
        
        def addpath(root,targetSum):
            # if root is None and targetSum==0:
            #     return True
            # if root is None and targetSum!=0:
            #     return False
            if root is None:
                return False
            if root.left is None and root.right is None :
                if root.val==targetSum:
                    return True
                else:
                    return False
            targetSumd=targetSum-root.val
            tlsl=addpath(root.left,targetSumd)
            tlsr=addpath(root.right,targetSumd)
            return tlsl or tlsr
            # if tlsl or tlsr:
            #     return True
            # else:
            #     print(tlsl)
            #     print(tlsr)
            #     return False
        return addpath(root,targetSum)