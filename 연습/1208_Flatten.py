import sys
sys.stdin = open('1208.txt', 'r')

for tc in range(1, 11):
    dump = int(input())
    data = list(map(int, input().split()))

    for i in range(dump):
        max_idx = min_idx = 0
        for j in range(len(data)):
            if data[max_idx] < data[j]:
                max_idx = j
            if data[min_idx] > data[j]:
                min_idx = j
        data[max_idx] -= 1
        data[min_idx] += 1

    max_idx = min_idx = 0
    for j in range(len(data)):
        if data[max_idx] < data[j]:
            max_idx = j
        if data[min_idx] > data[j]:
            min_idx = j

    ans = data[max_idx] - data[min_idx]
    print(ans)
