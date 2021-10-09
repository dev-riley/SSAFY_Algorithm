import sys
sys.stdin = open('1979.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N : 가로, 세로 길이 K : 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 행을 검사
    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] == 1: # 흰색 부분
                cnt_r += 1
            else: # 벽이 나타나
                if cnt_r == K:
                    ans += 1
                cnt_r = 0 # 초기화

        if cnt_r == K:
            ans += 1

    # 열을 검사
    for i in range(N):
        cnt_c = 0
        for j in range(N):
            if puzzle[j][i] == 1:  # 흰색 부분
                cnt_c += 1
            else:  # 벽이 나타나
                if cnt_c == K:
                    ans += 1
                cnt_c = 0  # 초기화

        if cnt_c == K:
            ans += 1
    print(f'#{tc} {ans}')