import sys
sys.stdin = open('11150.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N + 1):
        print(' ' * (N - i) + '*' * i)
