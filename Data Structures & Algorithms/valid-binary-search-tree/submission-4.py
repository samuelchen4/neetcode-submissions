# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, cur_min, cur_max):
            # base case:
            if not node:
                # we dont need anything from the child
                return True
            
            if node.val <= cur_min or node.val >= cur_max:
                return False

            # iterative cases:
            check_left = dfs(node.left, cur_min, node.val)
            check_right = dfs(node.right, node.val, cur_max)

            return check_left and check_right
            
        return dfs(root, float('-inf'), float('inf'))