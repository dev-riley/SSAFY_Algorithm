# 지그재그 풀이

arr = [[1, 2, 3, 4, 5],
       [10, 9, 8, 7, 6],
       [11, 12, 13, 14, 15],
       [20, 19, 18, 17, 16],
       [21, 22, 23, 24, 25]]

N,M = len(arr), len(arr[0])
for i in range(N):
    if i % 2 ==0:
        for j in range(M):
            print(arr[i][j])
    else:
        for j in range(M -1, -1, -1):
            print(arr[i][j])