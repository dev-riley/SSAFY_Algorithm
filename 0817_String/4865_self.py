import sys
sys.stdin = open('4865.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    cnt_list = [0] * len(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt_list[i] += 1

    max_str = cnt_list[0]
    for k in range(len(cnt_list)):
        if max_str < cnt_list[k]:
            max_str = cnt_list[k]

    print(f'#{tc} {max_str}')
