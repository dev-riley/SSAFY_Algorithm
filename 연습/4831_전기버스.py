import sys
sys.stdin = open('12385.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split())) # K : 한번에 갈 수 있는 정류장 수 N: 종점 번호 M: 충전기 설치된 정류장 수
    station = [0] + list(map(int, input().split())) + [N] # 충전기가 있는 정류소 번호
    cur = 0 # 현재 위치
    cnt = 0 # 충전 횟수
    for i in range(1, M + 2):
        # 충전 불가능 한 경우
        if station[i] - station[i - 1] > K:
           cnt = 0
           break
        # 충전 해야하는 경우
        if cur + K < station[i]:
            cur = station[i - 1]
            cnt += 1
    print(cnt)