# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return  False

        if not subRoot:
            return True    

        if root.val == subRoot.val and self.check(root,subRoot):
                return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot))   

                


    def check(self, root, subroot) -> bool:

        if not subroot and not root:
            return True

        if root and subroot and root.val == subroot.val:
            return (self.check(root.left,subroot.left) and self.check(root.right,subroot.right))
        

        return False        
