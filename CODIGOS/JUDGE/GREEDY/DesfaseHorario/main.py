'''
Desfase Horario
'''
class tarea():

    def __init__(self, nombre, start, end):
        self.nombre = nombre
        self.start = start
        self.end = end

def overlapping(array):

    array.sort(key = lambda x: x.end)
    bestFinish = array[0].end
    count = 1
    for item in array:
        if item.start > bestFinish:
            count += 1
            bestFinish = item.end

    print(count)

if __name__ == "__main__":
    n = int(input())
    array = []

    for _ in range(n):
        nombre, start, end = map(str, input().strip().split())
        aux = tarea(nombre, int(start), int(end))
        array.append(aux)

    overlapping(array)