import sys
sys.stdin = open('2817_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = int(input().split())
    numbers = map(int, input().split())
    cnt = 0
    for i in range(1, N+1):
        # 값 하나가 K랑 같을 때
        if numbers[i] == K:
            cnt +=1
        # 2개 이상 더해야 할 때
        else:
            pass
