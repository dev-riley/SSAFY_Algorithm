import sys
sys.stdin = open('3143.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    t, p = input().split() # t는 전체 문장, p는 미리 저장한 문장
    n, m = len(t), len(p)
    s = cnt = 0
    while s < n - m + 1: # s = 시작점, 시작점으로 가능한 만큼 반복문을 돌림
        # 패턴의 길이 만큼 한 문자씩 비교
        i = 0
        for i in range(m):
            if t[s + i] != p[i]:
                break
        else:
            cnt += 1
            s = s + m - 1 # 패턴을 찾았으니 시작점을 패턴의 길이 만큼(즉, m 만큼) 더해주고 다시 시작
        s += 1
    print(n- (cnt * m) + cnt)