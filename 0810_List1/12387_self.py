import sys
sys.stdin = open('12387.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    ans = 0
    max_val = 0
    min_val = 1000000
    for s in range(0, N - M + 1):
        total = 0
        for i in range(s, s + M):
            total += data[i]

        if max_val < total: max_val = total
        if min_val > total: min_val = total

    ans = max_val - min_val
    print(f'#{tc} {ans}')



