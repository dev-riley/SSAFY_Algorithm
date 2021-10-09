import sys
sys.stdin = open('2817_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    #  N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수
    N, K = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0

    for j in range(N):
        if data[j] == K:
            cnt += 1

        if sum == K:
            cnt += 1
            break

    print(f'#{tc} {cnt}')