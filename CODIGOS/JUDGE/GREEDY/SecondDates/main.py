'''
Second Dates
'''
class Item():
    def __init__(self, name, edad):
        self.name = name
        self.edad = edad

def greedy(participantes, n):

    media = 0
    for i in participantes:
        media += i.edad
    media = media / len(participantes)

    jovenes = []
    viejos = []

    for participante in participantes:
        if participante.edad < media:
            jovenes.append(participante)
        else:
            viejos.append(participante)

    length_joven = len(jovenes)
    length_viejos = len(viejos)

    i = 0
    if length_joven > n:

        while i < length_joven:

            j = 0
            while j < n and i != length_joven:
                print(jovenes[i].name, end=" ")
                j += 1
                i += 1

            print()


    else:
        for i in range(length_joven):
            print(jovenes[i].name, end=" ")

        print()

    i = 0

    if length_viejos > n:

        while i < length_viejos:

            j = 0
            while j < n and i != length_viejos:
                print(viejos[i].name, end=" ")
                j += 1
                i += 1

            print()

    else:
        for i in range(length_viejos):
            print(viejos[i].name, end=" ")

        print()

if __name__ == "__main__":

    N, M = map(int, input().strip().split())
    participantes = []


    for i in range(N):
        name, edad = map(str, input().strip().split())

        p = Item(name, int(edad))
        participantes.append(p)

    greedy(participantes, M)