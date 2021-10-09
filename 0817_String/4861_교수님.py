import sys
sys.stdin = open('4861.txt', 'r')


def find(arr):
    # 길이 N인 한 행에 대해서 길이 M인 회문 찾기
    ans = ''
    for row in range(N):
        for s in range(N - M + 1):
            e = s + M -1
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

    print(find(arr))