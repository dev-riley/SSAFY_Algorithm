import sys
sys.stdin = open('11315.txt', 'r')

def check(x, y):
    for i in range(8):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
            cnt += 1
            nx = nx + dx[i]
            ny = ny + dy[i]
        if cnt > 4:
            return True
    return False

dx = [-1,1,0,0,-1,1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]
ans = ['NO', 'YES']
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    flag = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o': # 돌이 있는지 체크
                if check(r, c):
                    flag = 1
                    break
        if ans:
            break
    print('#{} {}'.format(tc, ans[flag]))