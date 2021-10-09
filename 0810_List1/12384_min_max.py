import sys
sys.stdin = open('min_max_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max = numbers[0]
    for i in range(N):
        if max < numbers[i]:
            max = numbers[i]
    min = numbers[0]
    for i in range(N):
        if min >= numbers[i]:
            min = numbers[i]

    print('#{} {}'.format(tc + 1, max-min))