# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # the idea is that the operation is just merging two lists
        # where the first half of the list is the same
        # and the 2nd half is reversed

        # step 1) finding the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow will be the middle point
        # where first half = [0, slow]

        # reuse fast as second half
        fast = slow.next
        slow.next = None

        # now we have two lists
        # reverse the second half list
        prev = None
        while fast:
            next_node = fast.next

            # overwrite current next now
            fast.next = prev
            prev = fast
            fast = next_node

        # now we have a reversed second half of the linked list
        # merge starting with first half
        fast = prev
        slow = head
        while slow and fast:
            slow_next = slow.next
            fast_next = fast.next

            slow.next = fast
            fast.next = slow_next      

            slow = slow_next
            fast = fast_next









