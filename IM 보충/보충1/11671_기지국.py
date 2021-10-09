import sys
sys.stdin = open('11671.txt', 'r')

def check(x, y):
    for i in range(4): # 4방향 돌려서 H -> X로 바꾸기
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 체크, H일 때 X로 바꾸기 (인덱스 체크를 먼저해야함!!)
        # 16진수 (A~F) ord(arr[i]) - ord('A') + 1
        for j in range(ord(arr[x][y]) - ord('A') + 1):
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                arr[nx][ny] = 'X'
                nx = nx + dx[i]
                ny = ny + dy[i]

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 기지국 찾기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'A' or arr[r][c] == 'B' or arr[r][c] == 'C':
                check(r, c)
    # 커버 안되는 H 세기
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1
    print('#{} {}'.format(tc, ans))