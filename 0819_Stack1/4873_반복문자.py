import sys
sys.stdin = open('4873.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    C = input()

    S = []
    ans = 1
    for w in range(len(C)):
        S.append(C[w])

        if len(S) == 0 and S[-1] !=


