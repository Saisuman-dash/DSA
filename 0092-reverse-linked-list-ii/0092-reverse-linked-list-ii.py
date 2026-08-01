# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nulli=ListNode(0)
        nulli.next=head
        temp=head
        prev=None
        stop=None
        start=None
        tempu=None
        nexttempu=None
        nexti=None
        count=0
        while temp is not None:
            count+=1
            if count==left:
                start=temp
            if count==right:
                stop=temp
            temp=temp.next
        temp=nulli
        while temp is not None:
            if temp.next==start:
                prev=temp
                break
            temp=temp.next
        nexti=stop.next
        endi=stop.next
        tempu=start
        while tempu != endi:
            nexttempu=tempu.next
            tempu.next=nexti
            nexti=tempu
            tempu=nexttempu
        prev.next=nexti
        return nulli.next

       