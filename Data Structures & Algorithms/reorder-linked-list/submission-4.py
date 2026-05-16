# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return

        fast = head.next
    
        slow = head

        while slow.next:

            temp_behind_fast = fast

            while fast.next:
                temp_behind_fast = fast
                fast = fast.next
            
            temp_slow = slow
            slow = slow.next
            
            if slow == fast:
                break

            temp_behind_fast.next = None

            temp_slow.next = fast

            fast.next = slow

            temp_slow = fast

            fast = slow.next


