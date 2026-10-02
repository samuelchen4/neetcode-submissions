# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        # save the value we are going to get rid of as prev

        head = None
        cur = None

        if list1 is None:
            return list2
        if list2 is None:
            return list1


        while list1 and list2:

            if list1.val <= list2.val:
                # save list1 because we will remove it
                next_node = list1
                list1 = list1.next

            else:
                next_node = list2
                list2 = list2.next


            if head is None:
                head = next_node
                cur = next_node
            else:
                cur.next = next_node
                cur = cur.next

        
        if list1 is None:
            cur.next = list2
        else:
            cur.next = list1


        return head

        
    



        