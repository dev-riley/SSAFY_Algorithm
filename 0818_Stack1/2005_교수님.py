import sys
sys.stdin = open('2005.txt', 'r')

memo = [[0] * 100 for _ in range(100)]
def comb(n, r):
    if memo[n][r]:
        return memo[n][r]

    if r == 0 or n == r:
        return 1
    else:
        memo[n][r] = comb(n - 1, r - 1) + comb(n - 1, r)
        return memo[n][r]