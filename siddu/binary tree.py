class Node: 
 def __init__(self,value): 
 self.data = value 
 self.left = None 
 self.right =None 
class BinarySearchTree: 
 def __init__(self): 
 self.root=None 
 def insert(self,value): 
 newNode=Node(value) 
 if self.root is None: 
 self.root = newNode 
 else: 
 curNode = self.root 
 while curNode is not None: 
 if value < curNode.data: 
 if curNode.left is None: 
 curNode.left=newNode 
 break 
 else: 
 curNode = curNode.left 
 else: 
 if curNode.right is None: 
 curNode.right=newNode 
 break 
 else: 
 curNode=curNode.right 
 def preorder(self, rt): 
 print(rt.data, end="") 
 if rt.left is not None: 
 self.preorder(rt.left) 
 if rt.right is not None: 
 self.preorder(rt.right) 
 def postorder(self, rt): 
 if rt.left is not None: 
 self.postorder(rt.left) 
 if rt.right is not None:
self.postorder(rt.right) 
 print(rt.data, end="") 
 def inorder(self, rt): 
 if rt.left is not None: 
 self.inorder(rt.left) 
 print(rt.data, end="") 
 if rt.right is not None: 
 self.inorder(rt.right) 
bst = BinarySearchTree() 
ls = [25,10,35,20,65,45,24] 
for i in ls: 
 bst.insert(i) 
print("\nPre-order traversal is:") 
bst.preorder(bst.root) 
print("\nPost-order traversal is:") 
bst.postorder(bst.root) 
print("\nIn-order traversal is:") 
bst.inorder(bst.root) 
