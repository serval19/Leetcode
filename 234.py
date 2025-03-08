# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        l1=[]
        while temp!=None:
            l1.append(temp.val)
            temp=temp.next
        return l1==l1[::-1]
