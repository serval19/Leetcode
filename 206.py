# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevnode=None
        currentnode=nextnode=head
        while(nextnode!=None):
            nextnode=nextnode.next
            currentnode.next=prevnode
            prevnode=currentnode
            currentnode=nextnode
        head=prevnode
        return head


        
