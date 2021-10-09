arr = [64, 25, 10, 22, 11]
N = len(arr)
#(0 ~N -1) 최솟값 찾기
# min_idx = 0
# for j in range(1, N):
#     if arr[min_idx] > arr[j]:
#         min_idx = j
# arr[0], arr[min_idx] = arr[min_idx], arr[0]
# print(arr)
#
# #(1 ~ N - 1) 최솟값 찾기
# min_idx = 1
# for j in range(2, N):
#     if arr[min_idx] > arr[j]:
#         min_idx = j
# arr[1], arr[min_idx] = arr[min_idx], arr[1]
# print(arr)
#
# #(2 ~ N - 1) 최솟값 찾기
# min_idx = 2
# for j in range(3, N):
#     if arr[min_idx] > arr[j]:
#         min_idx = j
# arr[2], arr[min_idx] = arr[min_idx], arr[2]
# print(arr)

for i in range(0, N - 2 + 1):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)