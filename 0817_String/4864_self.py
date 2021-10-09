import sys
sys.stdin = open('4864.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    i = j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            i -= 1
        i += 1
        j += 1

    if i == len(str1):
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
