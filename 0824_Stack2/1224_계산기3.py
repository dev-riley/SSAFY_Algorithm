import sys
sys.stdin = open('1224.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    p = input()
    icp = {'(' : 3, '+': 1, '*': 2, ')': 3}
    isp = {'(' : 0, '+': 1, '*': 2}
    S = []
    postfix = []
    ans = []

    for i in p:
        if i in icp: # 연산자일 경우
            if i == ')':
                while S[-1] != '(':
                    postfix.append(S.pop())
                S.pop()
            else:
                while S and icp[i] <= isp[S[-1]]:
                    postfix.append(S.pop())
                S.append(i)
        else: # 피연산자일 경우
            postfix.append(i)
    while S:
        postfix.append(S.pop())

    for i in postfix:
        if '0' <= i[0] <= '9':
            ans.append(int(i))
        elif i == '+':
            ans.append(ans.pop() + ans.pop())
        elif i == '*':
            ans.append(ans.pop() * ans.pop())
    print(f'#{tc} {ans[0]}')
