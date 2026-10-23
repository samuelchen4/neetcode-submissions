# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        # in order traversal always visits in ascending order for a BST
        def dfs(node):
            nonlocal count, result
            if not node:
                return
            
            left_check = dfs(node.left)
            
            # do check in order
            count += 1
            if count == k:
                result = node.val

            right_check = dfs(node.right)

            return result

        return dfs(root)

