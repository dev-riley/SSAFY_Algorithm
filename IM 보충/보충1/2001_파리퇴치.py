import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_lst = []
    for r in range(0, N - M + 1): # 시작점
        for c in range(0, N - M + 1):
            cnt = sum = 0
            for i in range(r, r + M):
                for j in range(c, c + M):
                    sum += arr[i][j]
            sum_lst.append(sum)
    max = sum_lst[0]
    for k in range(len(sum_lst)):
        if max < sum_lst[k]:
            max = sum_lst[k]
    print(f'#{tc} {max}')