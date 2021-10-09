import sys
sys.stdin = open('11671.txt', 'r')

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        for j in range(ord(arr[x][y])- ord('A') + 1):
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'H':
                    arr[nx][ny] = 'X'
                nx = nx + dx[i]
                ny = ny + dy[i]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'A' or arr[r][c] == 'B' or arr[r][c] == 'C':
                check(r, c)

    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1
    print('#{} {}'.format(tc, ans))