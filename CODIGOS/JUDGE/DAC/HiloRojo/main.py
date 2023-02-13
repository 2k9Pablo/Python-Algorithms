'''
Hilo Rojo
'''
def search(x, array, ini, fin):

    if fin >= ini:
        mid = (ini + fin) // 2

        if x == array[mid]:
            return mid
        elif x < array[mid]:
            return search(x, array, ini, mid-1)
        elif x > array[mid]:
            return search(x, array, mid+1, fin)
    else:
        return -1

if __name__ == "__main__":
    n = int(input())
    g1 = list(map(int, input().strip().split()))

    m = int(input())
    g2 = list(map(int, input().strip().split()))

    c = int(input())
    for _ in range(c):
        a, b = map(int, input().strip().split())
        position1 = search(a, g1, 0, len(g1)-1)
        position2 = search(b, g2, 0, len(g2)-1)

        if position1 != -1 and position2 != -1:
            print(str(position1) + " " + str(position2))
        else:
            print("SIN DESTINO")