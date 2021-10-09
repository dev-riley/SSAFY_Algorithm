import sys
sys.stdin = open('4837_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N : 부분집합 원소의 수 K : 부분 집합의 합
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    n = len(arr)

    ans = 0
    for subset in range(1 << 12):
        S = cnt = 0
        for i in range(12):
            if subset & (1 << i):
                cnt += 1
                S += arr[i]
        if cnt == N and S == K:
            ans += 1
    print(f'#{tc} {ans}')

