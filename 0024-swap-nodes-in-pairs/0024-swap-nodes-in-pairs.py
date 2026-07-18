# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if temp is None:
            return None
        if temp.next is None:
            return temp
        first = temp
        sec = temp.next
        rest=sec.next
        sec.next=first
        first.next=self.swapPairs(rest)
        return sec
        