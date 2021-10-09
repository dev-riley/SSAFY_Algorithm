import sys
sys.stdin = open('sum_input.txt', 'r')

for tc in range(1, int(input())+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))

    total = 0
    for i in range(M):
        total += arr[i]

    max_val = min_val = total

    for e in range(M,N):
        total = total + arr[e] - arr[e-M]