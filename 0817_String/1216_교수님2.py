import sys
sys.stdin = open('1216.txt', 'r')

def find_palindrome(arr):
    ans = 0
    for i in range(100): # 행 / 열의 인덱스
        for j in range(100): # 기준 위치
            # 짝수인 경우
            l, r, cnt = j, j + 1, 0 # 행에 대해서 조사
            while 0 <= l and r < 100 and arr[i][l]== arr[i][r]:
                cnt, l, r = cnt + 2, l - 1, r + 1
            ans = max(ans, cnt)
            l, r, cnt = j, j + 1, 0 # 열에 대해서 조사
            while 0 <= l and r < 100 and arr[l][i] == arr[r][i]:
                cnt, l, r = cnt + 2, l - 1, r + 1
            ans = max(ans, cnt)

            # 홀수인 경우
            l, r, cnt = j - 1, j + 1, 1 # 행에 대해서 조사
            while 0 <= l and r < 100 and arr[i][l] == arr[i][r]:
                cnt, l, r = cnt + 2, l - 1, r + 1
            ans = max(ans, cnt)
            l, r, cnt = j - 1, j + 1, 1 # 열에 대해서 조사
            while 0 <= l and r < 100 and arr[l][i] == arr[r][i]:
                cnt, l, r = cnt + 2, l - 1, r + 1
            ans = max(ans, cnt)
    return ans

for tc in range(1, 11):
    tc_num = input()
    N = 100
    arr = [input() for _ in range(N)]

    print(find_palindrome(arr))