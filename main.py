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
        self.children = []
        for index in range(len(collection)):
            item = collection[index]
            if int(item) == self.index:
                self.children.append(index)


# Function for creating new child-node
def createNode(parent, collection):
    newNode = Node(index=None, value=None, parent=parent.index, level=parent.level+1)
    newNode.index = parent.children[-1]
    newNode.value = collection[4]
    return newNode


# Recursive function
def IN_depth (currentNode, collection, depth):

    currentNode.search(collection=collection)
    # print('node: ',{'index ': currentNode.index, 'value ': currentNode.value, 'parent ': currentNode.parent, 'level ': currentNode.level, 'children ': currentNode.children })
    # there is at least one descedant
    while currentNode.children != []:
        childNode = createNode(currentNode, collection=collection)
        currentNode.children.pop()
        depth = IN_depth(childNode, collection=collection, depth=depth)

    # base case
    depth = max(depth, currentNode.level)
    print(depth)
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

    # compute
    depth = IN_depth(root, collection, 1)
    print('fin: ', depth)







