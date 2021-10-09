import sys
sys.stdin = open('1989.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = list(input())
    N = len(L)
    for i in range(N//2):
        if L[i] == L [N - 1 - i]:
            ans = 1
        else:
            ans = 0
    print(f'#{tc} {ans}')
