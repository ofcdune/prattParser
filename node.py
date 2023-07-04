class Node:

    def __init__(self):
        return


class Node1Param(Node):

    def __init__(self, content):
        super().__init__()
        self.content = content


class Node2Param(Node):

    def __init__(self, left, right):
        super().__init__()
        self.right = left
        self.left = right


class Integer(Node1Param):

    def __init__(self, content):
        super().__init__(content)

    def evaluate(self):
        return int(self.content)


class Multiplication(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


class Division(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()


class Addition(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


class Subtraction(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()


class Absolute(Node1Param):

    def __init__(self, content):
        super().__init__(content)

    def evaluate(self):
        return abs(self.content.evaluate())


class Factorial(Node1Param):

    def __init__(self, content):
        super().__init__(content)

    def evaluate(self):
        from math import factorial
        return factorial(self.content.evaluate())