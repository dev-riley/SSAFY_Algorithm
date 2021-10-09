import sys
sys.stdin = open('1220.txt', 'r')

def solve(arr, N):
    cnt = 0
    for c in range(N):
        flag = 0    # N극을 못 찾음
        for r in range(N):
            if flag == 0 and arr[r][c] == 1: # N극을 찾음
                flag = 1    # N극 찾아서 표시
            elif flag == 1 and arr[r][c] == 2: # N극을 찾은 상태에서 S극을 찾음
                cnt += 1
                flag = 0
    return cnt

for tc in range(1, 11):
    N = int(input())
    arr = [[list(map(int, input().split()))] for _ in range(N)]

    print('#{} {}'.format(tc, solve(arr, N)))