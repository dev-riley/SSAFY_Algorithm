import sys
sys.stdin = open('4881.txt', 'r')

# 열 인덱스의 순열을 생성

N = 3
arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
cols = [i for i in range(N)]

# 2단계
# def perm(k, cur_sum):
#     global ans
#     if k == N: # 여기에 오면 하나의 경우를 생성
#         S = 0
#         for i in range(N):
#             S += arr[i][cols[i]]
#         if ans > S:
#             ans = S
#         print(cols, S, cur_sum)
#     else:
#         for i in range(k, N):
#             cols[k], cols[i] = cols[i], cols[k]
#             perm(k + 1, cur_sum + arr[k][cols[k]])
#             cols[k], cols[i] = cols[i], cols[k]
# ans = 1000000
# perm(0, 0)
# print(ans)

# 3단계
def perm(k, cur_sum):
    global ans
    if cur_sum >= ans: return # 가지치기
    if k == N: # 여기에 오면 하나의 경우를 생성
        if ans > cur_sum:
            ans = cur_sum

    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k + 1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]
ans = 1000000
perm(0, 0)
print(ans)



