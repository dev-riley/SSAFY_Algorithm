import sys
sys.stdin = open('11148.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0

    print(f'#{tc}', end=" ")
    for i in range(N, 0, -1):
        if N % i == 0:
            ans = i
            print(ans, end=" ")
    print()