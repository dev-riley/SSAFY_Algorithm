# arr = [1, 2, 3]
# N = len(arr)
# order = [0] * N
# for i in range(N):
#     order[0] = arr[i ]# 첫번째 요소 선택
#     for j in range(N):
#         order[1] = arr[j] # 두번째 요소 선택
#         for k in range(N):
#             order[2] = arr[k] # 세번째 요소 선택
#             print(order)
#
#
# def perm(k,n):
#     if k == n :
#         print(order)
#     else:
#         for i in range(N):
#             order[k] = arr[i]
#             perm(k + 1, n)
#
# perm(0, N)

arr = [1, 2, 3]
N = len(arr)
visit = [0] * N # 요소의 선택 여부 저장
order = [0] * N # 실제 순연의 순서를 저장

for i in range(N):
    order[0] = arr[i]; visit[i] = 1
    #========================================
    for j in range(N):
        if visit[j]: continue # continue는 넘어가라는 의미
        order[1] = arr[j]; visit[j] = 1
        #======================================
        for k in range(N):
            if visit[k]: continue
            order[2] = arr[k]; visit[k] = 1
            print(order)
            visit[k] = 0
        visit[j] = 0
    visit[i] = 0