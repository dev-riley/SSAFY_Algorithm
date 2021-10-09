import sys
sys.stdin = open('1223.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    data = input()
    icp = {'*' : 2, '+' : 1}
    postfix = [] # 후위 표기식
    S = [] # Stack
    ans = []

    for ch in data:
        if ch in icp:# 연산자 구별
            while S and icp[ch] <= icp[S[-1]]: # 스택에 top에 들어있는 값의 우선순위가 ch보다 높으면
                postfix.append(S.pop()) # top에 들어있는 걸 빼서 후위 표기식에 넣고
            S.append(ch) # 우선순위 낮은 연산자는 스택으로
        else:
            postfix.append(ch) # 피연산자는 바로 후위표기식으로
    while S:
        postfix.append(S.pop())
    for i in postfix:
        if '0' <= i <= '9':
            ans.append(int(i)) # 피연산자는 일단 ans에 집어넣는다.
        elif i == '+':
            ans.append(ans.pop() + ans.pop()) # + 만나면 앞에 두 피연산자 + 계산
        elif i == '*':
            ans.append(ans.pop() * ans.pop()) # * 만나면 앞에 두 피연산자 * 계산
    print(f'#{tc} {ans[0]}')