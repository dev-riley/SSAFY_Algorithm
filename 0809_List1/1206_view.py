import sys
sys.stdin = open('1206.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))
    # 조망권 층수률 계산
    ans = 0
    for i in range(2, N - 2):
        # i-2, i-1, i+1, i+2 위치의 값들 중에 최대 값을 찾는다.
        # max_h = max(H[i-2], H[i-1], H[i+1], H[i+2])
        lmax = H[i-2] if H[i-2] > H[i-1] else H[i-1]
        rmax = H[i + 2] if H[i + 2] > H[i + 1] else H[i + 1]
        maxh = lmax if lmax > rmax else rmax

        if H[i] > maxh:
            ans += H[i] - maxh
    print('#{} {}'.format(tc, ans))