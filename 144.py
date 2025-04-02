# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(node,l1):
            if node==None:
                return
            l1.append(node.val)
            helper(node.left,l1)
            helper(node.right,l1)
        l1=[]
        helper(root,l1)
        return l1