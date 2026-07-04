# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = []
        temp = head
        while temp != None:
            if temp not in freq:
                freq.append(temp)
                temp = temp.next
            else:
                return temp
        return None
        


        