# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, cur_max):
            # need this bc reassigning outer scoped variable
            nonlocal result
            # base case:
            if not node:
                # maybe return cur_max?
                return

            # update result
            if node.val >= cur_max:
                result += 1
            
            # update cur_max
            cur_max = max(cur_max, node.val)

            # iterative case
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        dfs(root, -101)
        return result
            
