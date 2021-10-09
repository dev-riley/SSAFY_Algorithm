import sys
sys.stdin = open('4864.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    w = list(map(str,input()))
    p = list(map(str,input()))

    i = j = 0 # w와 p의 인덱스
    while i < len(w) and j < len(p):
        if w[i] != p[j]:
            i = -1
        i += 1
        j += 1

    if i == len(w):
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
