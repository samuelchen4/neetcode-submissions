# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer 
        # overwrite a with the modulus

        prev1 = None
        cur1 = l1
        cur2 = l2
        carry = 0

        # iterate if either has nodes
        while cur1 or cur2:
            # vals could be None
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            # gets the first and second digit of the addition of values
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            # what happens when cur2 ends but cur1 still has values
                # this is fine we just add the results of val1 till the end
            # what happens when cur1 ends but cur2 still has values
                # this will lead to having no more nodes to add, so we need to change cur1 to cur2
            if not cur1:
                # actually point prev1 to cur2
                prev1.next = cur2
                cur1 = cur2
            
            # iterate pointers?

            # set cur1.val to digit
            cur1.val = digit


            prev1 = cur1
            cur1 = cur1.next
            cur2 = cur2.next if cur2 else None

        # iterated at the end of cur2
        if carry:
            prev1.next = ListNode(carry)
        
        return l1



        