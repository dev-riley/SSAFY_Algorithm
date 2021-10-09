# 스스로 다시 해보고 다른 방법을 시도하려고 했으나 실패..

import sys
sys.stdin = open('4861.txt', 'r')

def find(arr):
    # 길이 N인 한 행에 대해서 길이 M인 회문 찾기
    ans = ''
    for row in range(N): # 한 행마다 살펴보기
        for s in range(N - M + 1): # N과 M이 다를 경우 시작점
            e = s + M -1  # 시작점 s에 따른 e값 설정을 먼저 해줌.
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e-i]:
                    break
            else:
                for i in range(s, e + 1):
                    ans += arr[row][i]
                return ans
    # 모든 열에 대해서
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


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {find(arr)}')







