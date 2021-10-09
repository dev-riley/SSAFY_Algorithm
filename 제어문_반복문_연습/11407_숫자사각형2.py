import sys
sys.stdin = open('11407.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split()) # H : 행, 가로 W : 열, 세로

    print(f'#{tc}')
    for i in range(1, H * W + 1):
        for j in range(W):
            pass