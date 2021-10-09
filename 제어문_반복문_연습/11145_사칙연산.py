import sys
sys.stdin = open('11145.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    A, B, C = input().split()
    A, B = int(A), int(B)
    ans = 0
    if C == '+':
        ans = A + B
    elif C == '-':
        ans = A - B
    elif C == '*':
        ans = A * B
    elif C == '/':
        ans = A // B

    print(f'#{tc} {ans}')