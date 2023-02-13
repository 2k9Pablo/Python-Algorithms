'''
MasterChof
'''
class alimento():

    def __init__(self, nombre, tam, val):
        self.nombre = nombre
        if tam < 1:
            self.peso = 0,5
        else:
            self.peso = tam
        self.valor = val

class knapsack():

    def __init__(self, max):
        self.max = max
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def greedy(self):
        self.items.sort(key = lambda x: (x.valor / x.peso), reverse = True)
        total = 0
        freeSpace = self.max
        for item in self.items:
            if freeSpace - item.peso > 0:
                total += item.valor
                freeSpace -= item.peso
            elif freeSpace > 0:
                total += (freeSpace * item.valor) / item.peso
                freeSpace -= item.peso

        return total

if __name__ == "__main__":
    n, c = map(int, input().strip().split())
    k = knapsack(c)
    for _ in range(n):
        n, t, v = map(str, input().strip().split())
        a = alimento(n, int(t), int(v))
        k.addItem(a)

    print(str.format('{0:.6f}', k.greedy()))