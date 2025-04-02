# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(node,list1):
            if node==None:
                return
            helper(node.left,list1)
            helper(node.right,list1)
            list1.append(node.val)
        l1=[]
        helper(root,l1)
        return l1
        