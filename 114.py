# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        arr=[]
        def preorder(root):
            if root==None:
                return
            arr.append(root)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        for i in range(len(arr)-1):
            arr[i].right=arr[i+1]
            arr[i].left=None
        
