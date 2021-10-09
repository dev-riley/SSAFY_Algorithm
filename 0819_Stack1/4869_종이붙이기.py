import sys
sys.stdin = open('4869.txt', 'r')

# 메모이제이션
# 문제의 크기가 최대 300 --> 1 ~ 30
# memo = [0] * (31)

# def paper(n): # 함수로만 하면 값이 커질경우 시간이 오래 걸린다. 그래서 메모이제이션 적용
#     memo = [0] * (101)
#     # 기저 사례
#     if n == 10: return 1
#     if n == 20: return 3
#     ## 이미 답을 구한 문제인가?
#     if memo[n] != 0:
#         return memo[n]
#     # 일반 사례
#     memo[n] = paper(n - 10) + paper(n - 20) * 2
#     return memo[n]
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#
#     print(f'#{tc} {paper(N)}')

def paper(n): # 함수로만 하면 값이 커질경우 시간이 오래 걸린다. 그래서 메모이제이션 적용
    memo = [0] * (100)
    memo[1] = 1; memo[2] = 3

    # 기저 사례
    for i in range(3, n + 1): # i --> 테이블 인덱스 / 문제 크기(식별값)
        memo[i] = memo[i - 1] + memo[i - 2] * 2
    return memo[n]

for tc in range(1, int(input()) + 1):
    N = int(input()) // 10

    print(f'#{tc} {paper(N)}')
