# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            # iterate both
            slow = slow.next
            fast = fast.next.next

            # if they are the same there is a match
            if slow == fast:
                return True

        return False

        