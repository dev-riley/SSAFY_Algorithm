import sys
sys.stdin = open('4866.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    p = input()
    stack = []
    ans = 1
    for i in range(len(p)):
        if p[i] == '(' or p[i] == '{':
            stack.append(p[i])

        elif p[i] == ')':
            if len(stack) == 0 or stack[-1] != '(':
                ans = 0
                break
            stack.pop()

        elif p[i] == '}':
            if len(stack) == 0 or stack[-1] != '{':
                ans = 0
                break
            stack.pop()

    if len(stack) != 0:
        ans = 0
    print(f'#{tc} {ans}')

######### 오답노트 ##########
# 계속 Runtime ERROR가 떠서 팀원들에게 물어봤다.
# 총 2가지를 고쳤다.
# 1) elif에서 ans = 0 밑에 break를 추가해주었고,
# 2) 처음에 마지막 if에서 len(stack) == 0을 입력했는데, 위의 조건들에도 같은 조건으로 작성해서
# 충돌이 있었을 것 같다고 초기 ans = 0을 1로 바꿔주었고, 마지막 if의 조건을 위와 같이 변경해주었다.
# 그랬더니 pass!!
# elif > if에서 조건을 충족하지 않으면 break를 해줘서 계산을 빠르게 하는 것과
# 같은 조건이 계속 쓰이면 혹시 모를 충돌이 있을 수도 있다는 것을 배웠다.