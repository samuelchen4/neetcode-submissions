# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_indexes = {}
        for i in range(len(inorder)):
            inorder_indexes[inorder[i]] = i

        preorder_index = 0


        # make a helper recursive method
        def dfs(left_bound, right_bound):
            nonlocal preorder_index
            if left_bound > right_bound:
                return None

            node_val = preorder[preorder_index]
            preorder_index += 1
            # split inorder
            inorder_root_index = inorder_indexes[node_val]            

            # recurse
            node = TreeNode(node_val)
            node.left = dfs(left_bound, inorder_root_index - 1)
            node.right = dfs(inorder_root_index + 1, right_bound)

            return node

        return dfs(0,len(inorder) - 1)
    
