import sys
sys.stdin = open('1979.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # N : 2차원리스트의 크기, K : 내가 찾고 싶은 길이
    N, K = map(int, input().split())

    # 띠를 만들자
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0]*(N+1))
    ans = 0

    for i in range(N):
        # 행을 검사
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] == 1:  # 흰색 부분
                cnt_r += 1
            else:
                # 벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0

        # 열을 검사
        cnt_c = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

    print(f'#{tc} {ans}')
