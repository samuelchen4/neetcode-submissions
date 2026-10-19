from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        # bfs, queue
        queue = deque()

        # initialize
        if root:
            queue.append(root)
        while queue:
            cur = []
            level_size = len(queue)

            for _ in range(level_size):
                # deque
                cur_node = queue.popleft()
                # add to cur
                cur.append(cur_node.val)
                # append children to queue
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            if cur:
                result.append(cur)
                cur = []

        return result

         