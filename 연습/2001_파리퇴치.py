import sys
sys.stdin = open('2001.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_list = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum=0
            for i in range(r, r +M):
                for j in range(c, c+M):
                    sum += arr[i][j]
            sum_list.append(sum)
    print('#{} {}'.format(tc, max(sum_list)))