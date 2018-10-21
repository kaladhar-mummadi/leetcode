# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root is None:
            return "null"
        return str(root.val) + "," + self.serialize(root.left) + ","+ self.serialize(root.right)

    def deserialize(self, data):

        def deserialize_util(data, i):
            if len(data) == 0 or data[i] == "null":
                return [None, i + 1]

            temp = TreeNode(data[i])
            temp.left, j = deserialize_util(data, i + 1)
            temp.right, j = deserialize_util(data, j)
            return [temp, j]



        return deserialize_util(data.split(","), 0)[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
from tree_utils import get_binary_tree_from_arr, print_in_order
root = get_binary_tree_from_arr([1,2,3,4,5])
sol = Codec()
str_bst = sol.serialize(root)
print(sol.serialize(sol.deserialize(str_bst)))
# print_in_order(root)