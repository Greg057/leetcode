class TreeNode:
    """
    Representing a tree node consisting of
    - datum: the datum stored at the node
    - left: reference to the left child node
    - right: reference to the right child node
    """   
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.datum)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.datum)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.datum)

tree = BinaryTree(TreeNode('A', TreeNode('B', TreeNode('D'), TreeNode('E', TreeNode("I"), TreeNode("J"))), 
                TreeNode('C', TreeNode('F', TreeNode('K'), TreeNode('L')), TreeNode('H', TreeNode('M')))))
print("Inorder Traversal:")
tree.inorder(tree.root)
print("\nPreorder Traversal:")
tree.preorder(tree.root)
print("\nPostorder Traversal:")
tree.postorder(tree.root)