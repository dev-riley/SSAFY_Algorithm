import sys
sys.stdin = open('12385.txt', 'r')

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    station = [0] + list(map(int, input().split())) + [N]
    cur = 0         # 현재 위치
    cnt = 0         # 충전 횟수

    for i in range(1, M+2):
        # 충전 불가능한 경우
        if station[i] - station[i-1] > K:
            cnt = 0
            break
        # 충전 해야하는 경우
        if cur + K < station[i]:
            cur = station[i - 1]
            cnt += 1
    print(cnt)