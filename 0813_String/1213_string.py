import sys
sys.stdin = open('1213.txt', 'r', encoding='utf-8')

for tc in range(1, 11):
    n = int(input())  # n번째 테스트 케이스
    w = input(); W = len(w) # 찾을 문자열
    p = input(); P = len(p)  # 검색할 문자열

    cnt = 0
    for i in range(P - W + 1):
        if p[i] == w[0]:
            flag = True
            for j in range(1, W):
                if p[i + j] != w[j]:
                    flag = False
                    break
            if flag == True:
                cnt += 1
                i += W - 1 # 찾을 문자열을 건너뜀




