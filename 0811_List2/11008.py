import sys
sys.stdin = open('11008_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    sum_list = []
    for c in range(N):
        sum = 0
        for r in range(N):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

            if 0 <= nr < N  and 0 <= nc < N:
                sum += arr[nr][nc]
            sum_list.append(sum)

        sum_max = sum_list[0]
        idx = 0
        for i in range(len(sum_list)):
            if sum_max < sum_list[i]:
                sum_max = sum_list[i]
                idx = i
        r_idx = idx // N
        c_idx = idx % N
        