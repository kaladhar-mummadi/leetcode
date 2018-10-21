# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def in_order_helper(self, root, arr):
        if root is None:
            return


        self.in_order_helper(root.left, arr)
        arr.append(root.val)
        self.in_order_helper(root.right, arr)


    def inorderTraversal(self, root):
        arr = []
        self.in_order_helper(root, arr)
        return arr
