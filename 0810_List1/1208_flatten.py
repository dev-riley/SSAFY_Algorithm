import sys
sys.stdin = open('1208.txt', 'r')

for tc in range(1, 11):
    dump = int(input())
    d_num = list(map(int, input().split()))


    for j in range(dump):
        max_idx = 0
        min_idx = 0
        for i in range(len(d_num)):
            if d_num[max_idx] < d_num[i]:
                max_idx = i
            if d_num[min_idx] > d_num[i]:
                min_idx = i
        d_num[max_idx] -= 1
        d_num[min_idx] += 1

    max_idx = 0
    min_idx = 0
    for i in range(len(d_num)):
        if d_num[max_idx] < d_num[i]:
            max_idx = i
        if d_num[min_idx] > d_num[i]:
            min_idx = i

    print('#{} {}'.format(tc, d_num[max_idx]-d_num[min_idx]))
