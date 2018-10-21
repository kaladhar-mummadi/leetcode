# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    max_height = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rec(root, -1, 0)
        return self.max_height
    def rec(self, root, prev_num, temp_height):
        if root == None:
            return temp_height

        temp_height_lft = self.rec(root.left, root.val, temp_height)

        temp_height_right = self.rec(root.right, root.val, temp_height)

        # temp_height = max(temp_height_lft, temp_height_right)
        if root.val == prev_num:
            temp_height = max(temp_height_lft, temp_height_right) + 1

        if self.max_height < temp_height:
            self.max_height = temp_height
        if self.max_height < (temp_height_lft +temp_height_right):
            self.max_height = temp_height_right+temp_height_lft
        return temp_height

sol = Solution()