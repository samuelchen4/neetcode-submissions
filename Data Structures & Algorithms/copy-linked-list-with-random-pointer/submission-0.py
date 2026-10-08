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
        # we will have a hash map where key is the original node ref and value is the deep copy
        # iterate once to populate the map and create deep copies
        # iterate through the new deep copies and update the references based on the map

        hash_map = { None: None }
        cur = head

        while cur:
            deep_copy_node = Node(cur.val, cur.next, cur.random)
            hash_map[cur] = deep_copy_node

            # no need to store in advance because we aren't overwriting
            cur = cur.next
        
        # reset cur
        cur = head
        # iterate through deep_copies
        deep_head = hash_map[head]

        while cur:
            # iterate through original, but attach the references to the deep copies
            deep_cur = hash_map[cur]
            deep_cur.next = hash_map[cur.next]
            deep_cur.random = hash_map[cur.random]

            cur = cur.next

        return deep_head

