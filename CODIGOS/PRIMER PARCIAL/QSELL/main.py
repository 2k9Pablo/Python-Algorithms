'''
Que se enciendan las luces
'''
class concursante():

    def __init__(self, nombre, belleza, inteligencia, amabilidad, tiempo):
        self.nombre = nombre
        self.belleza = belleza
        self.inteligencia = inteligencia
        self.amabilidad = amabilidad
        self.tiempo = tiempo

class Knapsack():

    def __init__(self, max, caracteristica):
        self.max = max
        self.items = []
        self.caracteristica = caracteristica

    def addConcursante(self, concursante):
        self.items.append(concursante)

    def greedy(self):

        timeLeft = self.max

        selected = []
        total = 0
        self.sort()

        for concursante in self.items:
            if timeLeft - concursante.tiempo > 0:
                timeLeft -= concursante.tiempo

                if self.caracteristica == "kindness":
                    total += concursante.amabilidad
                elif self.caracteristica == "beauty":
                    total += concursante.belleza
                elif self.caracteristica == "intelligence":
                    total += concursante.inteligencia

                selected.append(concursante)

            elif timeLeft > 0:

                if self.caracteristica == "kindness":
                    total += (timeLeft * concursante.amabilidad) / concursante.tiempo
                elif self.caracteristica == "beauty":
                    total += (timeLeft * concursante.belleza) / concursante.tiempo
                elif self.caracteristica == "intelligence":
                    total += (timeLeft * concursante.inteligencia) / concursante.tiempo

                selected.append(concursante)
                timeLeft -= concursante.tiempo


        for i in range(len(selected)):
            print(selected[i].nombre, end=" ")
        print()
        print(total)

    def sort(self):
        if self.caracteristica == "kindness":
            self.items.sort(key = lambda x: (x.amabilidad / x.tiempo), reverse= True)
        elif self.caracteristica == "intelligence":
            self.items.sort(key = lambda x: (x.inteligencia / x.tiempo), reverse= True)
        elif self.caracteristica == "beaty":
            self.items.sort(key = lambda x: (x.belleza / x.tiempo), reverse= True)


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        c = str(input())
        m = int(input())
        T = int(input())
        K = Knapsack(m, c)
        for _ in range(T):
            o, b, i, k, t = map(str, input().strip().split())
            a = concursante(o, int(b), int(i), int(k), int(t))
            K.addConcursante(a)
        K.greedy()