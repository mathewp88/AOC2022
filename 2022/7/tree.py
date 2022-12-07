class Node:
    def __init__(self, name, parent, size=0):
        self.name: str = name
        self.parent: Node = parent
        self.children: list[Node] = []
        self.size: int = size

    def __le__(self, other: int):
        return self.size <= other

    def __lt__(self, other: int):
        return self.size < other

    def __radd__(self, other: int):
        return self.size + other

    def __ge__(self, other: int):
        return self.size >= other

    def __gt__(self, other: int):
        return self.size >= other

    def __str__(self):
        return str(self.size)

class Tree:
    def __init__(self):
        self.root: Node = Node("/", None)
        self.pwd: Node = self.root
        self.dirs: list[Node] = []

    def add_node(self, name, size=0):
        if size == 0:
            node = Node(name, self.pwd)
            self.pwd.children.append(node)
            self.dirs.append(node)
            self.pwd = node
        else:
            node = Node(name, self.pwd, size)
            self.pwd.children.append(node)

    def up(self):
        self.pwd = self.pwd.parent

    def update_size(self):
        for child in self.root.children:
            self.root.size += self.update_size_helper(child)

    def update_size_helper(self, node):
        for child in node.children:
            node.size += self.update_size_helper(child)
        return node.size

    def give_size(self, node):
        return node.size