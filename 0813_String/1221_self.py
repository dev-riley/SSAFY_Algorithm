import sys
sys.stdin = open('1221.txt', 'r')

T = int(input())
num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, T + 1):
    t, M = input().split()
    data = input().split()
    cnt_list = [0] * 10
    cnt = 0
    for i in range(len(data)):
        for j in range(len(num_list)):
            if data[i] == num_list[j]:
                cnt_list[j] += 1
    print(f'#{tc}')

    for k in range(10):
        print((num_list[k] + ' ') * cnt_list[k], end = ' ')
    print()