# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        # in order traversal always visits in ascending order for a BST
        def dfs(node):
            nonlocal count
            if not node:
                return
            
            left_check = dfs(node.left)
            if left_check is not None:
                return left_check
            
            # do check in order
            count += 1
            if count == k:
                return node.val

            right_check = dfs(node.right)
            if right_check is not None:
                return right_check

        return dfs(root)

