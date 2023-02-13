'''
Leap Day
'''

if __name__ == "__main__":

    n, m = map(int, input().strip().split())

    board = []

    #Suelo = 0, Pared = 1, Trampa = 2, Inicio = 3, Final = 4

    for _ in range(n):
        board.append(list(map(int, input().strip().split())))

