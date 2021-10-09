import sys
sys.stdin = open('4875.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def maze(r,c):
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nc < N and 0 <= nr < N and arr[r][c] != '1' and visit[nr][nc] == 0:
            maze(nr, nc)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    sr = sc = er = ec = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                sr, sc = i, j
            if arr[i][j] == '3':
                er, ec = i, j
    maze(sr, sc)
    print(f'#{tc} {visit[er][ec]}')