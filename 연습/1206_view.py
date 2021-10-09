import sys
sys.stdin = open('1206.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))

    lmax = rmax = max = ans = 0
    for i in range(2, N -2):
        if data[i-1] > data[i-2]:
            lmax = data[i-1]
        else:
            lmax = data[i-2]
        if data[i+1] > data[i+2]:
            rmax = data[i+1]
        else:
            rmax = data[i+2]
        if lmax > rmax:
            max = lmax
        else:
            max = rmax
        if data[i] > max:
            ans += data[i] - max
    print('#{} {}'.format(tc, ans))