# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        carry=0
        dummy=ListNode(0)
        curr=dummy
        sum=0
        while temp1 or temp2 or carry:
            x = temp1.val if temp1 else 0
            y = temp2.val if temp2 else 0
            sum=x+y+carry
            carry=sum//10
            sum=sum%10
            curr.next=ListNode(sum)
            curr=curr.next
            if temp1:
                temp1=temp1.next
            if temp2:
                temp2=temp2.next
            
        return dummy.next
        
                

            



        