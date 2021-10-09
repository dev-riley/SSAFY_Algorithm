import sys
sys.stdin = open('1860.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N: 자격을 얻은 N명의 사람 M : M초의 시간을 들이면 K : K개의 붕어빵
    N, M, K = map(int, input().split())
    data = list(map(int,input().split()))
    data.sort()

    ans = 'Possible'
    for i in range(N):
        tmp = (data[i] // M) * K # 붕어빵 갯수
        if tmp - 1 - i < 0: # -1은 현재 손님꺼, -i는 이전 손님들이 가져간 수
            ans = 'Impossible'
            break

    print('#{} {}'.format(tc, ans))


