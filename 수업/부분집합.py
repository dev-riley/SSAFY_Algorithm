# arr = [10, 20, 30, 40]

# val = 10
# print(bin(val)) # 2진수로 바꿔줌
#
# val = 0b1010 # 10진수로 바로 바꿔줌
# print(val)

val = 10
print(10 << 1) # 오른쪽으로 한 칸씩 옮길때마다 *2(2진수 생각하면 됨)

print(10 & 8)
print(10 & 4)
print(10 & 2)
print(10 & 1)

arr = [10, 20, 30, 40]
N = len(arr)

# 모든 부분집합에 대응하는 2진수 = 0 ~2^n -1
for subset in range(0, 1 << N):
    # subset의 N개의 bit를 조사
    S = 0
    for i in range(N):  # N => 0 ~ 3
        if subset & (1 << i):
            print(arr[i], end = ' ')
            S += arr[i]
    print('=>', S)