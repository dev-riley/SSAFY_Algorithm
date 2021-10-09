import sys
sys.stdin = open('11147.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{tc}', end=" ")
    for i in range(1, M + 1):
        ans = N * i
        if ans > M:
            break
        print(ans, end=" ")
    print()