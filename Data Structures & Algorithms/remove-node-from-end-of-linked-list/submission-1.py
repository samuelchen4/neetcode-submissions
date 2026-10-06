# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use fast and slow pointer but have them reference the same thing so we can have a fixed index gap between the two pointers

        # initialize cur, future, prev, and k
        prev = None
        cur = head
        future = head
        k = n

        # set the gap beteen future and cur
        while k > 0:
            future = future.next
            k -= 1
        
        # edge case, if future is at the end, head is what we want to delete
        if future is None:
            head = cur.next
            return head
    
        # future not at end, traverse list
        while future:
            prev = cur
            cur = cur.next
            future = future.next

        prev.next = cur.next
        return head



        