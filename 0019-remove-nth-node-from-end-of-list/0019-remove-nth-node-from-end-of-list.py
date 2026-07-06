# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        count = 0
        while temp is not None:
            length+=1
            temp = temp.next
        temp = head
        if length == n:
            head = head.next
        deln = length - n
        while temp is not None:
            count += 1
            if count == deln:
                temp.next = temp.next.next
                temp = temp.next
            else:
                temp = temp.next
        return head

