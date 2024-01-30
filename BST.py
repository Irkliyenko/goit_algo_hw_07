# Define a class representing a binary tree node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0):
        # String representation of the tree with indentation
        ret = "\\t" * level + str(self.val)
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

# Function to insert a key into the binary tree


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Function to search for a key in the binary tree


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Function to delete a key from the binary tree


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Function to find the node with the minimum value in a given binary tree


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Function to find the node with the maximum value in a given binary tree


def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

# Function to calculate the sum of all values in the binary tree


def sum_values(root):
    if not root:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)


# Main function to demonstrate the usage of the binary tree functions
if __name__ == '__main__':
    # Creating a binary tree
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    # Printing results
    print("Minimum Value Node:", min_value_node(root))
    print("Maximum Value Node:", max_value_node(root))
    print("Sum of All Values:", sum_values(root))
