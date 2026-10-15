# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # how do we traverse a variable accross recursive calls
        # have a helper method that has node and depth

        def dfs(node, depth):
            # base case
            if not node:
                return depth

            # iterative case 
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            return max(left, right)
        
        return dfs(root, 0)





