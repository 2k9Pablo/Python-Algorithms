'''
CuraCovid
'''
if __name__ == "__main__":
    n = int(input())

    current = str(input())

    for _ in range(n-1):
        cadena = str(input())
        i = 0
        while i < len(cadena) and i < len(current) and cadena[i] == current[i]:
            i += 1

        current = current[:i]

    print(current)