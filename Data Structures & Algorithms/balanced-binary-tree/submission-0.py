# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, depth):
            if not node:
                return 0
            

            # iterative case
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            if left_depth < 0 or right_depth < 0:
                return -1

            # check if balanced
            if abs(left_depth - right_depth) > 1:
                return -1

            # return largest depth
            # need to add 1 to account for itself
            return max(left_depth, right_depth) + 1

        return True if dfs(root, 0) >= 0 else False
        