import sys
sys.stdin = open('1209_input.txt', 'r')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    # 각 열의 합
    is_list = js_list = []
    for i in range(len(arr)):
        sum_i= 0
        for j in range(len(arr[i])):
            sum_i += arr[i][j]
        is_list.append(sum_i)

        max_i = is_list[0]
    for k in range(len(is_list)):
        if max_i < is_list[k]:
            max_i = is_list[k]

    # 각 행의 합
    for j in range(len(arr[i])):
        sum_j = 0
        for i in range(len(arr)):
            sum_j += arr[i][j]
        js_list.append(sum_j)
        max_j = js_list[0]
    for k in range(len(js_list)):
        if max_j < js_list[k]:
            max_j = js_list[k]

    # 대각선의 합
    sum_d = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_d += arr[i][j]

    if max_i <= max_j and sum_d <= max_j:
        ans = max_j
    if max_j <= max_i and sum_d <= max_i:
        ans = max_i
    if max_i <= sum_d and max_j <= sum_d:
        ans = sum_d
    print(ans)