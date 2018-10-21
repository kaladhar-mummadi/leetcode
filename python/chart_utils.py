import random
from graphviz import render

def _get_dot(root):
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


def _get_dot_func(parent, child):
    yield "%s -> %s".format(parent, child)



def create_graph(filename):

    # lines = get_dot(root).split("\n")
    # lines[0] = "digraph "+filename+" {"
    # lines = "\n".join(lines)
    # f = open("charts/"+filename+".txt", 'w')
    # f.write(lines)
    # f.close()
    render("dot", "svg", 'charts/'+filename+'.txt')

create_graph("tree")