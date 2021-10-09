import sys
sys.stdin = open('2805.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    middle = (N-1)//2
    rev = j = 0

    for i in range(middle + 1):
        start = middle - i
        end = middle + i + 1
        rev += sum(arr[j][start:end])
        j += 1

    for i in range(middle, 0, -1):
        start = middle - i + 1
        end = middle + i
        rev += sum(arr[j][start:end])
        j += 1

    print('#{} {}'.format(tc, rev))