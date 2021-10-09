import sys
sys.stdin = open('5432.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    p = input()

    stack = []

    for i in range(p):
        if p[i] == '(':
            stack.append(p[i])
        elif p[i] == ')':
            pass