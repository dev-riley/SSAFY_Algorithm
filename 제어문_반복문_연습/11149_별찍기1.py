import sys
sys.stdin = open('11149.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}', end=" ")
    for i in range(N + 1):
        print('*' * i)