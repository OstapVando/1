# Create a class for node of tree
class Node (object):

    # Self description
    def __init__(self, value, parent, level, children=[]):
        self.value = value
        self.parent = parent
        self.level = level
        self.children = children # list of indexes of children nodes

    # search for children in collection method
    def search(self, collection):
        for item in collection:
            if item == self.index:
                self.children.append(item)





if __name__ == "__main__":

    # Data input:
    n = input()
    collection = input().split(sep=',')
    tree = {}
    depth = 0

    # Create a root-node
    root = Node(value=-1, parent=None, level=1)
    for item in collection:
        if item == -1:
            root.index = collection.index(item)

    # Start our tree with a root-node
    tree[-1] = root

    tree[-1].search(collection=collection)
    





