import sys
sys.stdin = open('1954_input.txt','r')

# 델타를 이용한 2차 배열 검색

i = [0, 1, 0, -1]
j = [1, 0, -1, 0]

T = int(input())

for tc in range(T):
    r, c = 0, -1
    dir = 0
    cnt = 1
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    while cnt <= N*N:
        r = r + i[dir]
        c = c + j[dir]
        if 0 <= r < N and 0 <= c < N and arr[r][c] == 0:
            arr[r][c] = cnt
            cnt += 1
        else:
            r = r - i[dir]
            c = c - j[dir]
            dir = (dir + 1) % 4

    print(f'#{tc + 1}')
    for lst in arr:
        print(*lst)