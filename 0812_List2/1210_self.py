import sys
sys.stdin = open('1210_input.txt', 'r')

def search(start): # 도착지에서 위로 올라가는 함수
    i = 99 # 현재 출발 위치 행
    j = start # 현재 출발 위치 열
    while i > 0: # 행이 0이 될때까지 이동
        i -= 1
        if j > 0 and ladder[i][j - 1] == 1: # 만약 현재 위치의 왼쪽이 1이면
            while j > 0 and ladder[i][j - 1] == 1: # 0을 만날때까지 이동 & 사다리를 벗어나는 상황을 없앰
                j -= 1
        elif j < 99 and ladder[i][j + 1] == 1: # 현재 위치의 오른쪽이 1이면
            while j < 99 and ladder[i][j + 1] == 1: # 0을 만날때까지 이동 & 사다리를 벗어나는 상황을 없앰
                j += 1
    return j # 0번 행에 도착했을 때의 열 리턴

for tc in range(1, 11):
    T = int(input())
    ladder = [[0] * 100 for _ in range(100)]

    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print(f'#{tc} {ans}')