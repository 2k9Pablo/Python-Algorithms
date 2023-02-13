def isValid(n, laberinto, x, y):

    if x >= 0 and y >= 0 and x < n and y < n and laberinto[x][y] == 0:
        return True

    return False

def isSolved(laberinto, n, x, y):

    return sum([sum(l) for l in laberinto]) == (-1) * n**2 and x == n-1 and y == n-1

def solvePath(n, laberinto, x, y):

    move_x = [1, -1, 0, 0]
    move_y = [0, 0, -1, 1]

    for i in range(4):

        new_x = x + move_x[i]
        new_y = y + move_y[i]

        if isValid(n, laberinto, new_x, new_y):
            laberinto[new_x][new_y] = -1
            if solvePath(n, laberinto, new_x, new_y):
                return True

            if isSolved(laberinto, n, new_x, new_y):
                return True
            laberinto[new_x][new_y] = 0

    return False

if __name__ == "__main__":

    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))

    matrix[0][0] = -1

    if solvePath(n, matrix, 0, 0):
        print("SI")
    else:
        print("NO")
