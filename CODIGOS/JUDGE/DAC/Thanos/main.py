'''
Thanos
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
    habitantes = list(map(int, input().strip().split()))

    m = int(input())
    amochados = list(map(int, input().strip().split()))
    amochados.sort()

    p = int(input())
    busqueda = list(map(int, input().strip().split()))


    for i in range(p):
        aux = -1
        aux1 = -1

        aux = search(busqueda[i], habitantes, 0, len(habitantes)-1)
        aux1 = search(busqueda[i], amochados, 0, len(amochados)-1)

        if aux > -1 and aux1 > -1:
            print(":_(")
        else:
            print(":)")