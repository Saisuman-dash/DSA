# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # i = 1
        # freq = {}
        # while curr!=None:
        #     freq[i]=curr
        #     curr = curr.next
        #     i += 1
        # return freq[((i-1)//2)+1]
        fast = head
        slow = head 
        while fast!= None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        return slow
