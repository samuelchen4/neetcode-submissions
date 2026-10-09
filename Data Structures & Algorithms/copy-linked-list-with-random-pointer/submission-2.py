"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        if not head:
            return None

        # append the copy in the list: A -> A^1 -> B -> B^1
        while cur:
            next_original = cur.next
            deep_copy = Node(cur.val, next_original, cur.random)

            cur.next = deep_copy
            cur = next_original

        deep_cur = head.next
        # update the random pointers for the copies
        while deep_cur:
            # the copy is always original_node.next, therefore
            deep_cur.random = deep_cur.random.next if deep_cur.random else None
            deep_cur = deep_cur.next.next if deep_cur.next else None

        # lastly, separate into two lists and return head of copies
        deep_head = head.next
        deep_cur = deep_head
        cur = head
        while cur:
            next_original = cur.next.next if cur.next else None

            # update original to point to original
            # update copy to point to copy
            deep_cur.next = next_original.next if next_original else None
            cur.next = next_original

            # move cur
            cur = next_original
            deep_cur = deep_cur.next

        return deep_head




        


