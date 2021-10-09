import sys
sys.stdin = open('4839_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    l, r = 1, P
    cnt_a = cnt_b = 0

    while l <= r:
        cnt_a += 1
        c = (l + r) // 2
        if c == Pa:
            break
        elif c < Pa:
            l = c
        else:
            r = c

    l, r = 1, P
    while l <= r:
        cnt_b += 1
        c = (l + r) // 2
        if c == Pb:
            break
        elif c < Pb:
            l = c
        else:
            r = c

    if cnt_a > cnt_b:
        print(f'#{tc} B')
    elif cnt_b > cnt_a:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')