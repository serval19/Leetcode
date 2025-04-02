# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(node,list1):
            if node==None:
                return
            helper(node.left,list1)
            list1.append(node.val)
            helper(node.right,list1)
            return list1
        l1=[]
        helper(root,l1)
        return l1
        
        