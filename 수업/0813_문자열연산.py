# 문자열 뒤집기
arr = 'algorithm'
print(arr[::-1])

rev_arr=''
for i in range(len(arr) -1, -1, -1):
    rev_arr += arr[i]
print(rev_arr)

arr1 = list('algorithm')
#교환을 통해 뒤집기
N = len(arr1)
for i in range(N//2):
    arr1[i], arr1[N-1-i] = arr1[N - 1 -i], arr1[i]
print(arr1)
# 문자열 뒤집기를 응용해서 회문검사에 적용할 수 있다.

# 정수 --> 문자열
# 123 --> '123'
num = 123
arr2 = ''
while num > 0:
    arr2 += (chr(ord('0') + (num % 10)))
    num //= 10
print(arr2[::-1])

# 문자열 --> 정수
# '123' --> 123
arr3 = '123'
zero = ord('0')
num = 0
for ch in arr3:
    num = num * 10 + ord(ch) - zero     # '1' --> 1
print(num)

arr4 = [1, 2, 3]
num = 0
for n in arr4:
    num = num * 10 + n
print(num)