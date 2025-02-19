# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        num1=""
        num2=""
        while(temp1!=None):
            num1=num1+str(temp1.val)
            temp1=temp1.next
        num1=int(num1[::-1])
        while(temp2!=None):
            num2=num2+str(temp2.val)
            temp2=temp2.next
        num2=int(num2[::-1])
        num3=num1+num2
        if num3==0:
            return ListNode(0)
        list1=str(num3)
        list2=[]
        for i in list1:
            list2.append(int(i))
        list2.reverse()
        head1=ListNode(list2[0])
        current=head1
        for i in list2[1:]:
            current.next=ListNode(i)
            current=current.next
        return head1
        
        

        

        
