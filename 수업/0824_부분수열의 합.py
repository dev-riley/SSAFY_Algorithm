# bits = [0] *3
# for i in range(2):
#     bits[0] = i
#     for j in range(2):
#         bits[i] = j
#         for k in range(2):
#             bits[2] = k
#             print(bits)
#
# 위의 식 재귀호출로 똑같이 구현
# arr = [1, 2, 1, 2]
# N , K = 4, 3
# bits = [0] * N
# def subset(k, n, cur_sum): # k: 함수호출의 깊이, 노드의 높이, for문의 중첩횟수
#     if k == n:    # cur_sum: 현재까지 선택한 요소의 합
#         print(bits, end = ' ')
#         S = 0
#         for i in range(n):
#             if bits[i]:
#                 print(arr[i], end=' ')
#                 S += arr[i]
#         print(' ==> ', S, cur_sum )
#     else:
#         # for i in range(2): # i = 0 or 1
#         #     bits[k] = i
#         #     subset(k + 1, n)
#         bits[k] = 0 # k번 요소를 포함하지 않음
#         subset(k + 1, n, cur_sum)
#         bits[k] = 1 # k번 요소를 포함.
#         subset(k + 1, n, cur_sum + arr[k])
#
# subset(0, N, 0)

# 5번째
arr = [1, 2, 1, 2]
N , K = 4, 3
cnt = 0
def subset(k, n, cur_sum): # k: 함수호출의 깊이, 노드의 높이, for문의 중첩횟수
    if k == n:    # cur_sum: 현재까지 선택한 요소의 합
        global cnt
        if cur_sum == k:
            cnt += 1

    else:
        subset(k + 1, n, cur_sum)
        subset(k + 1, n, cur_sum + arr[k])

subset(0, N, 0)
