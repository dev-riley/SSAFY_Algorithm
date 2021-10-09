import sys
sys.stdin = open('12386.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input()))

    max = numbers[0]
    for i in range(N):
        if max < numbers[i]:
            max = numbers[i]

    cnt = [0] * (max+1)
    for num in numbers:
        cnt[num] += 1

    idx = 0
    cnt_max = cnt[0]
    for i in range(max+1):
        if cnt_max <= cnt[i]:
            cnt_max = cnt[i]
            idx = i

    print('#{} {} {}'.format(tc+1, idx, cnt_max))