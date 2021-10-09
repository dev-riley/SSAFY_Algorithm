import sys
sys.stdin = open('11404.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split()) # H : 행, 가로 W : 열, 세로

    print(f'#{tc}')
    for i in range(1, H * W + 1):
        if i % W == 1 and i != 1:
            print(end='\n')
        print(i, end=" ")
    print()
