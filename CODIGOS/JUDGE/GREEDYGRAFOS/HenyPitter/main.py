'''
Henry Pitter
'''
from collections import deque

dx = [0, 1, 0, -1, 0]
dy = [1, 0, -1, 0, 0]

class position():

    def __init__(self, x, y, turno):
        self.x = x
        self.y = y
        self.turno = turno

def copa(tablero, n, m, visited):

    current = position(0, 0, 1)
    q = deque()
    q.append(current)
    cont, turno = 1, 1
    found = False

    while q and not found:
        current = q.popleft()
        turno = current.turno

        for i in range(5):
            newX = current.x + dx[i]
            newY = current.y + dy[i]

            if newX >= 0 and newX <= n and newY >= 0 and newY <= m and (turno % 2 != 0 or tablero[newX][newY] != -1) and not visited[newX][newY]:
                visited[newX][newY] = True
                q.append(position(newX, newY, turno+1))

                if tablero[newX][newY] == 2:
                    found = True

    return turno

if __name__ == "__main__":

    N, M = map(int, input().strip().split())

    tablero = []
    for _ in range(N):
        tablero.append(list(map(int, input().strip().split())))

    visited = []
    for _ in range(N):
        visited.append([False] * M)

print(copa(tablero, N, M, visited))