import sys
sys.stdin = open('1221.txt', 'r')

T = int(input())
num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, T + 1):
    t , N = input().split()
    arr = input().split()
    count = [0] * 10
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(num_list)):
            if num_list[j] == arr[i]:
                 count[j] +=1
    print(f'#{tc}')

    for k in range(len(num_list)):
        print((num_list[k] +' ')* count[k], end = '')
    print()