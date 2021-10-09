import sys
sys.stdin = open('1206.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 테스트 케이스의 길이
    arr = list(map(int, input().split()))

    lmax = 0
    rmax = 0
    max = 0
    ans = 0
    for i in range(2, N - 2):
        if arr[i - 2] > arr[i - 1]:
            lmax = arr[i-2]
        else:
            lmax = arr[i-1]

        if arr[i + 2] > arr[i + 1]:
            rmax = arr[i + 2]
        else:
            rmax = arr[i + 1]

        if lmax > rmax:
            max = lmax
        else:
            max = rmax

        if arr[i] > max:
            ans += arr[i] - max
    print(f'#{tc} {ans}')