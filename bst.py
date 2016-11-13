class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _find(self, data):
        current = self.root
        parent = None
        while current:
            if data == current.data:
                return current, parent
            elif data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
        return None, parent

    def put(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current, parent = self._find(data)
            if current:
                print("중복추가")
            else:
                if data < parent.data:
                    parent.left = Node(data)
                else:
                    parent.right = Node(data)

    def remove(self, data):
        current, parent = self._find(data)
        if current:  # 탐색성공
            children_count = self.children_count(current)
            if children_count == 0:
                if current is parent.left:
                    parent.left = None
                else:
                    parent.right = None
                del current

            elif children_count == 1:
                if current.left:
                    node = current.left
                else:
                    node = current.right
                if current == parent.left:
                    parent.left = node
                else:
                    parent.right = node
                del current

            else:  # 삭제할 노드의 왼쪽 자식중 가장 큰값으로 대체
                successor = current.left
                while successor.right:
                    parent = successor
                    successor = successor.right
                current.data = successor.data
                if successor == parent.left:
                    parent.left = successor.right
                else:
                    parent.right = successor.left

    def children_count(self, current):
        cnt = 0
        if current.left:
            cnt += 1
        if current.right:
            cnt += 1
        return cnt


def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


def showTree(node, depth=0):
    if node:
        showTree(node.right, depth + 1)
        print(("   " * depth) + str(node.data))
        showTree(node.left, depth + 1)