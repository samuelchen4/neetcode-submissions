# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # recursively see if theres a subtree
        def dfs_compare(node_1, node_2) -> bool:
            if not node_1 and not node_2:
                return True
            
            if not node_1 or not node_2:
                return False

            if node_1.val != node_2.val:
                return False
            
            return dfs_compare(node_1.left, node_2.left) and dfs_compare(node_1.right, node_2.right)
        

        # find subroot node
        def dfs(node):
            if not node:
                return False

            if dfs_compare(node, subRoot):
                return True

            # traverse root tree
            # this is or because if we find the subtree in either side, it contains it
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

