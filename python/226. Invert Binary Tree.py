# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root != None):
            self.inverTreeRec(root.left, root.right, root)
        return root

    def inverTreeRec(self, lNode, rNode, parent):

        if (lNode == None and rNode == None):
            return
        # print(lNode.val, rNode.val)
        if lNode != None:
            self.inverTreeRec(lNode.left, lNode.right, lNode)
        if rNode != None:
            self.inverTreeRec(rNode.left, rNode.right, rNode)
        temp = lNode
        parent.left = rNode
        parent.right = lNode
