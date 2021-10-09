dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = 5
arr = [[0] *N for _ in range(N)]
dir = 0         # 진행 방향
r, c = 0, -1    # 시작 위치
cnt = 1
while cnt <= N*N:
    r += dr[dir]
    c += dc[dir]
    # 경계 체크 and 빈 곳인지 체크
    if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
        arr[r][c] = cnt
        cnt+= 1
    else:
        r -= dr[dir]
        c -= dc[dir]
        dir = (dir + 1) % 4

for lst in arr:
    print(*lst)