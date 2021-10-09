import sys
sys.stdin = open('1208.txt', 'r')

for tc in range(1, 11):
    N = int(input()) # 덤프 횟수
    data = list(map(int, input().split()))


    max_idx = 0
    min_idx = 0
    for j in range(N):
        for i in range(len(data)):
            if data[max_idx] < data[i]:
                max_idx = i
            if data[min_idx] > data[i]:
                min_idx = i
        data[max_idx] -= 1
        data[min_idx] += 1
    data[max_idx] -= 1
    data[min_idx] += 1

    ans = data[max_idx] - data[min_idx]
    print(f'#{tc} {ans}')