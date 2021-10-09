import sys
sys.stdin = open('4875.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    visit[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1' and visit[nr][nc] == 0:
            dfs(nr, nc)

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    sr = sc = er = ec = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                sr, sc = i, j
            elif maze[i][j] == '3':
                er, ec = i, j
    dfs(sr, sc)
    print(visit[er][ec])