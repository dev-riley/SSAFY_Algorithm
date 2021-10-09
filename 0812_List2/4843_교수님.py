import sys
sys.stdin = open('4843_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, N - 1):
        idx = i
        for j in range(i + 1, N):
            if arr[idx] < arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    print(f'#{tc}', end = ' ')
    for i in range(5):
        print(arr[i], end = ' ')
        print(arr[N - 1 - i], end = ' ')
    print()