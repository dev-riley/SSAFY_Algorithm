import sys
sys.stdin = open('4861.txt', 'r')

def find(arr):
    # 모든 행에 대해 조사
    ans = ' '
    for row in range(N):
        for s in range(N - M + 1): # 가능한 시작점 하나씩 조사
            e = s + M - 1 # 마지막
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e-i]:
                    break
            else:
                for i in range(s, e + 1):
                    ans += arr[row][i]
                return ans
    # 모든 열에 대해 조사
    for col in range(N):
        for s in range(N - M + 1):
            e = s + M -1
            for i in range(M // 2):
                if arr[s + i][col] != arr[e-i][col]:
                    break
            else:
                for i in range(s, e + 1):
                    ans += arr[i][col]
                return ans

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {find(arr)}')