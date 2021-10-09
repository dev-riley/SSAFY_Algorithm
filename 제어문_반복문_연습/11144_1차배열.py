import sys
sys.stdin = open('11144.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = list(map(int, input().split()))

    print(f'#{tc} {len(N)} {N[-1]}')