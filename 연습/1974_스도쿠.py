import sys
sys.stdin = open('1974.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    # 가로 체크
    for r in range(9):
        r_list = [0] * 10
        for c in range(9):
            r_list[arr[r][c]] += 1
            if r_list[arr[r][c]] == 2:
                ans = 0
                break

    # 세로 체크
    for r in range(9):
        c_list = [0] * 10
        for c in range(9):
            c_list[arr[c][r]] += 1
            if c_list[arr[c][r]] == 2:
                ans = 0
                break
    # 작은 격자 체크

    print('#{} {}'.format(tc, ans))