'''
Almendra Simon
'''
class almendra():

    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

class knapsack():

    def __init__(self):
        self.max = 0
        self.items = []

    def additem(self, almendra):
        self.items.append(almendra)

    def greedy(self):
        self.items.sort(key = lambda x: (x.valor / x.peso), reverse= True)
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

    def setMax(self, max):
        self.max = max
if __name__ == "__main__":
    n, m = map(int, input().strip().split())


    K = knapsack()

    for _ in range(n):
        v, p = map(int, input().strip().split())
        K.additem(almendra(v, p))

    for _ in range(m):
        mv, mp = map(int, input().strip().split())
        K.setMax(mp)
        if K.greedy() >= mv:
            print("PUEDE")
        else:
            print("TOS")