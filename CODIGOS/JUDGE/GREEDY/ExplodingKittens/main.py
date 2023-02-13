'''
Exploding Kittens
'''
class carta():

    def __init__(self, nombre, riesgo, beneficio):
        self.nombre = nombre
        self.riesgo = riesgo
        self.beneficio = beneficio

class knapsack():

    def __init__(self, max):
        self.max = max
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def greedy(self):
        self.items.sort(key = lambda x: (x.beneficio / x.riesgo), reverse= True)
        freeRisk = self.max
        selected = []
        for item in self.items:
            if freeRisk - item.riesgo > 0:
                selected.append(item.nombre)
                freeRisk -= item.riesgo
            elif freeRisk > 0:
                selected.append(item.nombre)
                freeRisk -= item.riesgo

        print(*selected)
if __name__ == "__main__":

    n, m = map(int, input().strip().split())
    K = knapsack(m)

    for _ in range(n):
        n, r, b = map(str, input().strip().split())
        a = carta(n, int(r), int(b))
        K.addItem(a)

    K.greedy()