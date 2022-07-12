

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
        print('start')
        self.children = []
        for index in collection:
            print(index, collection[index], self.index, (collection[index])==str(self.index))
            if collection[index] == str(self.index):
                self.children.append(index)




# Function for creating new child-node
def createNode(parent, collection):
    newNode = Node(index=None, value=None, parent=parent.index, level=parent.level+1)
    newNode.index = parent.children[-1]
    newNode.value = collection[newNode.index]

    return newNode


# Recursive function
def IN_depth (currentNode, collection, depth):

    # search for currentnode's children indexes
    currentNode.search(collection=collection)

    #print node
    print('node: ',{'index ': currentNode.index, 'value ': currentNode.value, 'parent ': currentNode.parent,
                    'level ': currentNode.level, 'children ': currentNode.children })
    # there is at least one descedant
    while currentNode.children != []:
        childNode = createNode(currentNode, collection=collection)
        currentNode.children.pop()
        depth = IN_depth(childNode, collection=collection, depth=depth)

    # base case
    depth = max(depth, currentNode.level)
    print(collection)
    return depth



if __name__ == "__main__":

    # Data input:
    depth = 0
    n = int(input())
    inp = input().split(sep=' ')
    collection = {}
    for i in range(0, n):
        collection[i] = inp[i]
    inp.clear()
    # Create a root-node
    root = Node(value=-1, parent=None, level=1, index=None)
    for item in collection:
        if collection[item] == '-1':
            root.index = item
    # compute
    depth = IN_depth(root, collection, 1)
    print(depth)







