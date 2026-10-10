from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # Breadth first seems like it makes the most sense
    #     if not root:
    #         return None

    #     # setup queue
    #     queue = deque([root])

    #     # iterate through each layer
    #     while queue:
    #         # get current node
    #         cur = queue.popleft()

    #         # pop both left and right nodes into the queue
    #         if cur.left:
    #             queue.append(cur.left)
    #         if cur.right:
    #             queue.append(cur.right)

    #         # swap
    #         # save the left node
    #         left_node = cur.left
    #         # change left to the right node
    #         cur.left = cur.right
    #         # change right to the saved left node
    #         cur.right = left_node

    #     return root

    # DFS resursive solution
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case return nothing
        if not root:
            return None
    
        # resursive case
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # actual swap
        left_node = root.left
        root.left = root.right
        root.right = left_node

        return root







