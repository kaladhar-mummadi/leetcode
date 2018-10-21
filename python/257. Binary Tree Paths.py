# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        path = []
        self.parseRec(root, res, path)
        return res

    def parseRec(self, root, res, pathArr):

        if root == None:
            return
        if root.left == None and root.right == None:
            pathArr.append(str(root.val))
            res.append("->".join(pathArr))
            pathArr.pop()
            return

        pathArr.append(str(root.val))
        self.parseRec(root.left, res, pathArr)
        self.parseRec(root.right, res, pathArr)
        pathArr.pop()

