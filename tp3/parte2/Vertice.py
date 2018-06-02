class Vertice:
    x = 0

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x

    def __hash__(self):
        return hash(self.x)

    def __lt__(self, other):
        return self.x < other.x

    def mostrar(self):
        return str(self.x)

def make_vertice(numero):
    vertice = Vertice(x)
    return vertice