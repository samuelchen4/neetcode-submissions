from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # setup queue 
        queue = deque()
        results = []

        # initialize values in queue
        if root:
            queue.append(root)
        while queue:
            # get level size
            level_size = len(queue)

            while level_size:
                # dequeue
                cur_node = queue.popleft()

                # enqueue if valid
                # left MUST go first
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

                # reduce level_size
                level_size -= 1

                # on last node in level
                if level_size <= 0:
                    results.append(cur_node.val)
            

        return results

                


    
        