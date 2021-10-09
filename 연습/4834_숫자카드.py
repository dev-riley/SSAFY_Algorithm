import sys
sys.stdin = open('4834.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input()))
    d_list = [0] * 10

    max_idx = 0
    for i in range(N):
        d_list[data[i]] += 1
        d_max = max(d_list)
        for j in range(len(d_list)):
            if d_max == d_list[j]:
                max_idx = j

    print('#{} {} {}'.format(tc, max_idx, d_max))

