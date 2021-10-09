import sys
sys.stdin = open('12385.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # K : 이동 가능 수, N: 종점 번호, M : 충전기 설치된 정류장 번호
    K, N, M = map(int, input().split())
    station = [0] + list(map(int, input().split())) + [N]
    cur = 0
    cnt = 0

    for i in range(1, M + 2):
        # 충전 불가능한 경우
        if station[i] - station[i - 1] > K:
            cnt = 0
            break
        # 충전 해야하는 경우
        if cur + K < station[i]:
            cur = station[i - 1]
            cnt += 1

    print(f'#{tc} {cnt}')