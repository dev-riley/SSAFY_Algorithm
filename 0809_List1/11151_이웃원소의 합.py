TC = int(input())
for tc in range(TC):
    N = int(input())
    data = list(map(int, input().split()))
    num_list = []
    for n in range(1, N):
        a = data[n - 1] + data[n]
        num_list.append(a)

    max_val = num_list[0]
    for num in num_list:
        if max_val < num:
            max_val = num
    print('#{} {}'.format(tc + 1, max_val))
