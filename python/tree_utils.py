# Definition for a binary tree node.
from graphviz import Digraph, render
import random
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree_util(nums, root, i, level):
    if i >= len(nums) or root is None:
        return
    left = None
    right = None
    left_ind = (i*level) + 1
    if left_ind < len(nums) and nums[left_ind] is not None:
        left = TreeNode(nums[left_ind])
    root.left = left
    right_ind = (i * level) + 2
    if right_ind < len(nums) and nums[right_ind] is not None:
        right = TreeNode(nums[right_ind])

    root.right = right

    create_tree_util(nums, root.left, left_ind, level+1)
    create_tree_util(nums, root.right, right_ind, level + 1)


def get_binary_tree_from_arr(nums):
    if len(nums) == 0 or nums[0] is None:
        return None

    root = TreeNode(nums[0])
    create_tree_util(nums, root, 0, 1)

    return root

def in_order_helper(root, arr):
    if root is None:
        return


    in_order_helper(root.left, arr)
    arr.append(root.val)
    in_order_helper(root.right, arr)


def print_in_order(root):
    arr = []
    in_order_helper(root, arr)
    for i in arr:
        print(i)


def get_dot(root):
    """return the tree with root 'self' as a dot graph for visualization"""
    return "digraph G{\n%s}" % ("" if root.val is None else (
        "\t%s;\n%s\n" % (
        root.val,
            "\n".join(_get_dot(root))
        )
    ))

def _get_dot(root):
    """recursively prepare a dot graph entry for this node."""
    if root.left is not None:
        yield "\t%s -> %s;" % (root.val, root.left.val)
        for i in _get_dot(root.left):
            yield i
    elif root.right is not None:
        r = random.randint(0, 1e9)
        yield "\tnull%s [shape=point];" % r
        yield "\t%s -> null%s;" % (root.val, r)
    if root.right is not None:
        yield "\t%s -> %s;" % (root.val, root.right.val)
        for i in _get_dot(root.right):
            yield i
    elif root.left is not None:
        r = random.randint(0, 1e9)
        yield "\tnull%s [shape=point];" % r
        yield "\t%s -> null%s;" % (root.val, r)

def create_graph(root, filename):

    lines = get_dot(root).split("\n")
    lines[0] = "digraph "+filename+" {"
    lines = "\n".join(lines)
    f = open("charts/"+filename+".txt", 'w')
    f.write(lines)
    f.close()
    render("dot", "svg", 'charts/'+filename+'.txt')

#
#
# create_graph(french_count(), "french_count")
# create_graph(letters_to_numbers(), "letter_to_numbers")
# create_graph(add_zero_padding(), "add_zero_padding")
# create_graph(truncate_to_three_digits(), "truncate_to_three_digits")


root = get_binary_tree_from_arr([1,2,3,4,5])
create_graph(root, "tree")
