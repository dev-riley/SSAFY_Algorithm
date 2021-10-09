import sys
sys.stdin = open('12386.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int,input()))

    max = data[0] # 가장 큰 숫자 저장
    for i in range(N):
        if max < data[i]:
            max = data[i]

    cnt = [0] * (max + 1) # 갯수 저장
    for num in data:
        cnt[num] += 1

    idx = 0
    cnt_max = cnt[0]
    for j in range(max + 1):
        if cnt_max <= cnt[j]:
            cnt_max = cnt[j]
            idx = j

    print(f'#{tc} {idx} {cnt_max}')
