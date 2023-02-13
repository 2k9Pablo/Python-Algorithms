num = float('inf')
def contar(sandia):

    global num
    if len(sandia) <= int(n // (2 ** c)):
        res = sum([sum(x) for x in sandia])
        if res < num:
            num = res

        return

    half = int(len(sandia) // 2)
    c1, c2, c3, c4 = cortes(sandia, half)
    contar(c1)
    contar(c2)
    contar(c3)
    contar(c4)

def cortes(sandia, mid):

    c1, c2, c3, c4 = [], [], [], []
    up = sandia[:mid]
    down = sandia[mid:]
    for i in range(mid):
        c1.append(list(up[i][:mid]))
        c2.append(list(up[i][mid:]))
        c3.append(list(down[i][:mid]))
        c4.append(list(down[i][mid:]))

    return c1, c2, c3, c4


if __name__ == "__main__":
    n, c = map(int, input().strip().split())
    sandia = []
    for _ in range(n):
        sandia.append(list(map(int, input().strip().split())))

    contar(sandia)
    print(num)