import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            pass
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print('#{} {}'.format(tc, ' '.join(map(str,arr))))

