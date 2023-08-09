

class BinaryNode:
    def __init__(self, value=''):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return " ".join(f"""
        {self.value}:
        {self.left_child.value if self.left_child else 'None'}
        {self.right_child.value if self.right_child else 'None'}
        """.split())

    def add_left(self, child):
        self.left_child = child

    def add_right(self, child):
        self.right_child = child


class NaryNode:
    def __init__(self, value=''):
        self.value = value
        self.children = []

    def __str__(self):
        return f"{self.value}: {' '.join([child.value for child in self.children])}"

    def add_child(self, child):
        self.children.append(child)

