# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs_compare(node_1, node_2):
            # this is None
            if not node_1 and not node_2:
                return True
            # first we check if the nodes.vals are the same 
            if not node_1 and node_2:
                return False
            
            if node_1 and not node_2:
                return False

            if node_1.val != node_2.val:
                return False
            
            
            # then we resursively call dfs_compare again
            left_check = dfs_compare(node_1.left, node_2.left)
            right_check = dfs_compare(node_1.right, node_2.right)

            if left_check and right_check:
                return True
            else:
                return False
        
        return dfs_compare(p, q)
            
            



        