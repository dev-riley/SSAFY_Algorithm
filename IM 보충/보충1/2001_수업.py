import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += arr[x+i][y+j]
            if max_value < total:
                max_value = total
    print(f'#{tc} {max_value}')