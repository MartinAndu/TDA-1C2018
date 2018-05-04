class Nodo:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash('a' + str(self.x) + 'b' + str(self.y))

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def mostrar(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def distancia_euclidea(self, nodo1):
        return ((self.x - nodo1.x) ** 2 + (self.y - nodo1.y) ** 2) ** (.5)

    def distancia(self, nodo1):
        return 1


def make_nodo(x, y):
    nodo = Nodo(x, y)
    return nodo