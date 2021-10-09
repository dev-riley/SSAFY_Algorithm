import sys
sys.stdin = open('11633.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int,input().split()))
    data = list(map(int, input().split()))

    sum_list = []
    for i in range(N - M + 1): # 시작점
        sum = 0
        for j in range(i, i + M):
            sum += data[j]
        sum_list.append(sum)
    ans = max(sum_list)-min(sum_list)
    print('#{} {}'.format(tc, ans))