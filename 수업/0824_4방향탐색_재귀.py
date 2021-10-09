
dr = [0, 1, 0, -1] # 우하좌상 순서대로 탐색
dc = [1, 0, -1, 0]
N = 5
arr = [[0] * N for _ in range(N)]
print(arr)
cnt = 1
def dfs(r, c):
    global cnt
    arr[r][c] = cnt; cnt += 1

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            dfs(nr, nc)

dfs(0, 0)

# for lst in arr:
#     print(*lst)