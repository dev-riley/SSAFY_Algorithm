import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_list = list(map(int, input().split()))

    for i in range(len(n_list) - 1):
        if n_list[i] < n_list[i + 1]:
            pass
        for j in range(i, len(n_list)):
            if n_list[i] > n_list[j]:
                n_list[i], n_list[j] = n_list[j], n_list[i]

    print(n_list)