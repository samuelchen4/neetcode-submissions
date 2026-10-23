# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # inorder: all elements left of the root node index is in the left subtree
        # preorder: based on the left_size from inorder all values directly after the root node up to the left_size index 
        # is in the left subtree

        # base case: leaf node
        
        # build a map that stores the index for each value in inorder
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
            inorder_left_size = inorder_indexes[node_val]            

            # recurse
            node = TreeNode(node_val)
            node.left = dfs(left_bound, inorder_left_size - 1)
            node.right = dfs(inorder_left_size + 1, right_bound)

            return node

        return dfs(0,len(inorder) - 1)
    
