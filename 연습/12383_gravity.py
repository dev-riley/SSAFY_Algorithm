import sys
sys.stdin = open('12383.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        dist = N - 1 - i
        for j in range(i + 1, N):
            if data[i] <= data[j]:
                dist -= 1
        if ans < dist:
            ans = dist
    print('#{} {}'.format(tc, ans))