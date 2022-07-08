# Create a class for node of tree
class Node (object):

    # Self description
    def __init__(self, index, value, parent_index, level):
        self.index = index
        self.value = value
        self.parent_index = parent_index
        self.level = level

def findIndex (parent, collection):
    for collection_item in collection:
        if collection_item == parent.index:
            return collection.index(collection_item)

if __name__ == "__main__":

    # Data input:
    n = input()
    collection = tuple(input().split(sep=','))

    # Create a root-node
    root = Node(value=-1, parent_index=None, level=1)
    for collection_item in collection:
        if collection_item == -1:
            root.index = collection.index(collection_item)




