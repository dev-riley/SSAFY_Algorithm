import sys; sys.stdin = open('1209_input.txt', 'r')

for tc in range(1,11):
    tc_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = 0 # 최대합 저장
    d1 = d2 = 0
    for i in range(100):
        d1 += arr[i][i]
        d2 += arr[i][99-i]
    # 행들의 합 & 열들의 합
        rsum = csum = 0       # 변수 초기화
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        if ans < rsum: ans = rsum
        if ans < csum: ans = csum
    if ans < d1: ans = d1
    if ans < d2: ans = d2

    print('#{} {}'.format(tc, ans))