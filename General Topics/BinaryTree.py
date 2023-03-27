class Node():
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def add_node(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.l:  
                        current = current.l
                    else:
                        current.l = Node(val)
                        break    
                elif val > current.val:
                    if current.r:  
                        current = current.r
                    else:
                        current.r = Node(val)
                        break       
                else:
                    break

def preorder(root):

    if root:
        print(root.val, end=" ")
        preorder(root.l)
        preorder(root.r)


def main():
    nodes = [1,2,5,3,4,6]
    btree = BinaryTree()

    for i in nodes:
        btree.add_node(i)
    
    preorder(btree.root)

if __name__ == "__main__":
    main()