import sys
sys.stdin = open('sum_input.txt', 'r')

for tc in range(1, int(input())+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_val = 0
    min_val = 1000000

    for s in range(0, N-M+1):
        total = 0
        # for i in range(M):
        #     total += arr[s + i]
        for i in range(s, s + M):
            total += arr[i]

        if max_val < total: max_val = total
        if min_val > total: min_val = total

    print('#{} {}'.format(tc+1,max_val-min_val))