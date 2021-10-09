import sys
sys.stdin = open('4843_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(10):
        idx = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if arr[idx] < arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
        else:
            for j in range(i + 1, N):
                if arr[idx] > arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]

    print(f'#{tc+1}', end = ' ')
    for i in range(10):
        print(arr[i], end = ' ')
    print()