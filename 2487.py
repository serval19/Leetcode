# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head
        
        while curr:
          
            while stack and curr.val > stack[-1].val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        dummy = ListNode()
        current = dummy
        for node in stack:
            current.next = node
            current = current.next
        return dummy.next
