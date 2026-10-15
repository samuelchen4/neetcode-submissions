# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        # helper method
        # recursively gets maximum depth
        def dfs(node, depth):
            nonlocal result
            # base case... hit leaf node
            if not node:
                return 0
            
            # iterative case
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            # for this node, calculate its max_diameter
            diameter = left_depth + right_depth
            # set new max_diameter
            result = max(result, diameter)

            # return the maximum depth
            return max(left_depth, right_depth) + 1

        dfs(root, 0)
        return result
            
        