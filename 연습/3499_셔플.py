import sys
sys.stdin = open('3499.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = input().split()
    s_list = []

    if N % 2 == 0:
        for i in range(N // 2):
            s_list.append(data[i])
            s_list.append(data[i+(N//2)])

    if N % 2 == 1:
        mid = N//2 + 1
        for j in range(N//2):
            s_list.append(data[j])
            s_list.append(data[j+mid])
        s_list.append(data[mid-1])
    print('#{} {}'.format(tc, ' '.join(s_list)))