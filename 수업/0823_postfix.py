icp = {'(' : 3, '*': 2, '/': 2, '+': 1, '-': 1, ')': 3} # 읽어 온 요소의 우선순위
isp = {'(' : 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택에 있을 때 우선순위

infix = '6+5*(2-8)/2'
postfix = []
S = []

for ch in infix:
    #연산자인지 피연산자인지 구분
    if ch in icp: # 연산자
        if ch == ')':
            while S[-1] != '(':
                postfix.append(S.pop())
            S.pop()
        else:
            while S and icp[ch] <= isp[S[-1]]:
                postfix.append(S.pop())
            S.append(ch)
    else:
        postfix.append(ch)
while S:
    postfix.append(S.pop())
print(''.join(postfix))