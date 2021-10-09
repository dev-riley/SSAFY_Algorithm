import sys
sys.stdin = open('2005.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    pascal = [[0]*10 for _ in range(10)] # 큰 틀을 만들기
    for i in range(n):
        pascal[i][0] = 1 # 첫번째 줄은 무조건 1
        pascal[i][i] = 1 # 각 줄 맨 처음과 맨 끝은 1
        for j in range(1, n-1): # 인접해있는 윗줄 두 숫자를 더함
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    for k in range(10): # 리스트에 있는 0 없애주기
        while 0 in pascal[k]:
            pascal[k].remove(0)

    print(f'#{tc}')
    for h in range(n):
        print(' '.join(map(str, pascal[h])))