class Node:

    def __init__(self):
        return

    def evaluate(self):
        return


class Node1Param(Node):

    def __init__(self, content):
        super().__init__()
        self.content = content


class Node2Param(Node):

    def __init__(self, left, right):
        super().__init__()
        self.right = right
        self.left = left


class IntegerNode(Node1Param):

    def __init__(self, content):
        super().__init__(content)

    def evaluate(self):
        return int(self.content)


class MultiplicationNode(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


class DivisionNode(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()


class AdditionNode(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


class SubtractionNode(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()


class AbsoluteNode(Node1Param):

    def __init__(self, content):
        super().__init__(content)

    def evaluate(self):
        return abs(self.content.evaluate())


class FactorialNode(Node1Param):

    def __init__(self, content):
        super().__init__(content)

    def evaluate(self):
        from math import factorial
        return factorial(self.content.evaluate())


class PowerNode(Node2Param):

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return pow(self.left.evaluate(), self.right.evaluate())