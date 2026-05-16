# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ant, atu = None, head

        while atu:
            prox = atu.next
            atu.next = ant
            ant = atu
            atu = prox
        return ant