import sys
sys.stdin = open('4836_색칠하기_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    ans = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 사각영역 색칠하기
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if arr[r][c] == 0:
                    arr[r][c] = color
                else:
                    # 겹치는 영역
                    ans += 1

    print(ans)