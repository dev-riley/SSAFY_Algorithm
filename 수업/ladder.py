import sys
sys.stdin = open('1210_ladder.txt', 'r')

def search(start): # 도착지에서 위로 올라가는 함수
    i = 99 # 현재 출발 위치 행
    j = start # 현재 출발 위치 열
    while i > 0: # 맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1 # 위로 한 칸 이동
        if j >0 and ladder[i][j-1] == 1: # 왼쪽 칸이 있고 1이면
            while j > 0 and ladder[i][j-1] == 1:     # 0을 만날 때까지 이동 & 사다리를 벗어나는 상황을 없앰
                j -= 1
        # 오른쪽 칸이 1이면
        elif j<99 and ladder[i][j+1] == 1: # 오른쪽 칸이 있고 1이면
            while j<99 and ladder[i][j+1] == 1:
                j += 1
        # 좌우가 0이면 위로(출발지) 리턴
    return j # 0번 행에 도착했을 때의 열(출발지) 리턴

T = 10 # 10개 테스트케이스 고정
for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    #도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print(f'#{tc} {ans}')