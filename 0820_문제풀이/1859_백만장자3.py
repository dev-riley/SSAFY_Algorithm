import sys
sys.stdin = open('1859.txt', 'r')

# 3. 반대로 생각
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    max_cost = cost[-1]

    for i in range(N-2, -1, -1): # N-1은 이미 max_cost에 저장되어 있기도 하고 어차피 사거나 팔지도 않을거라 N-2 로 적어줌
        # 내가 가진 값보다 보고 있는 값이 작을 때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]

    print(f'#{tc} {ans}')