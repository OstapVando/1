tree = {}
depth = 0

# Create a class for node of tree
class Node (object):

    # Self description
    def __init__(self,index, value, parent, level, children=[]):
        self.index = index
        self.value = value
        self.parent = parent
        self.level = level
        self.children = children # list of indexes of children nodes

    # search for children in collection method
    def search(self, collection):
        for value in collection:
            if value == self.index:
                self.children.append(collection.index(value))

# Find index of node
def findIndex(node, collection):
    return collection.index(node)

# Function for creating new child-node
def createNode(parent, collection):
    newNode = Node(level=parent.level+1)
    tree[parent.children[-1]] = newNode
    newNode.value = collection[parent.children[-1]]
    return newNode


# Recursive function
def IN_depth (currentNode, collection, depth):

    currentNode.search(collection=collection)
    print('node: ',{'index ': currentNode.index, 'value ': currentNode.value, 'parent ': currentNode.parent, 'level ': currentNode.level, 'children ': currentNode.children })
    # there is at least one descedant
    while currentNode.children != []:
        childNode = createNode(currentNode, collection=collection)
        currentNode.children.pop()
        IN_depth(childNode, collection=collection)

    # base case
    depth = max(depth, currentNode.level)
    return depth



if __name__ == "__main__":

    # Data input:
    n = input()
    collection = input().split(sep=' ')

    # Create a root-node
    root = Node(value=-1, parent=None, level=1, index=None)
    for item in collection:
        if item == '-1':
            root.index = collection.index(str(item))
            print('yeah')
    print('root: ', root.index)
    # Start our tree with a root-node
    tree[-1] = root
    tree[-1].search(collection)

    # Recursive function to traverse a tree
    depth = IN_depth(root, collection, 1)
    print(depth)







