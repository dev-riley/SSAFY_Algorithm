import sys
sys.stdin = open('1209.txt', 'r')

for tc in range(1,11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    m_list = []
    # 각 행의 합
    r_max = 0
    for r in range(100):
        sum = 0
        for c in range(100):
            sum += arr[r][c]
        if r_max < sum:
            r_max = sum
    m_list.append(r_max)
    # 각 열의 합
    c_max = 0
    for r in range(100):
        sum = 0
        for c in range(100):
            sum += arr[c][r]
        if c_max < sum:
            c_max = sum
    m_list.append(c_max)
    # 대각선의 합
    d_max = 0
    sum1 = 0
    for r in range(100):
        for c in range(100):
            if r == c:
                sum1 += arr[r][c]
    sum2 = 0
    for r in range(99, 0, -1):
        for c in range(99, 0, -1):
            if r == c:
                sum2 += arr[r][c]

    d_max=sum1 if sum1>sum2 else sum2
    m_list.append(d_max)

    print('#{} {}'.format(T, max(m_list)))

