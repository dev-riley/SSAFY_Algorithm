# 각 테스트 케이스의 첫 번째 줄에는 세 자연수 N, M, K(1 ≤ N, M, K ≤ 100)가
# 공백으로 구분되어 주어진다.

import sys
sys.stdin = open('1860.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N : 사람수 M : M초 걸림 K : k개 만듬
    N, M, K = map(int, input().split())
    # 0초 이후에 손님들이 언제 도착하는지 주어지면
    arr = list(map(int, input().split()))
    # 손님이 들어오는 순서를 정렬하자.
    arr.sort()

    ans = 'Possible'
    for i in range(N):
        tmp = (arr[i] // M) * K
        if tmp - 1 - i < 0:# -1은 현재 손님꺼, i는 이전 손님들이 가져간 수
            ans = 'Impossible'
            break
    print('#{} {}'.format(tc, ans))