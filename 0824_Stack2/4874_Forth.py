import sys
sys.stdin = open('4874.txt', 'r')

T = int(input())
ans = ''
for tc in range(1, T + 1):
    P = input().split()
    S = [] # Stack

    for w in P:
        if '0' <= w[0] <= '9': # 피연산자 S에 저장
            S.append(int(w))
        else: # 연산자인 경우
            if w == '.':
                if len(S) >= 2: # 2개 이상 들어있을 때
                    ans = 'error'
                    break
                else:
                    ans = S.pop()
                    break
            else:
                if len(S) < 2:  # 연산이 불가능한 경우
                    ans = 'error'
                    break
                y = S.pop() # 순서 바뀜
                x = S.pop()
                if w == '+':
                    S.append(x + y)
                elif w == '*':
                    S.append(x * y)
                elif w == '-':
                    S.append(x - y)
                elif w == '/':
                    S.append(x // y) # 소수점 없애기 위해

    print(f'#{tc} {ans}')