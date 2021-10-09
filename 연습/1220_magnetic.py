import sys
sys.stdin = open('1220.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            pass
    print('#{} {}'.format(tc, solve(arr, N)))