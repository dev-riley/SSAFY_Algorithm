import sys
sys.stdin = open('1210_input.txt', 'r')

for tc in range(1, 11):
    tc_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    #도착점을 찾는다.
    r = c = 0  # r = 열, c = 행
    for i in range(100):
        if ladder[99][i] == 2:
            r, c = 99, i
            break

    while r > 0:
        # 왼쪽
        if 0 <= c - 1 and ladder[r][c - 1]:
            c -= 1
        # 오른쪽
        if c + 1 < 100 and ladder[r][c + 1]:
        # 위
            pass