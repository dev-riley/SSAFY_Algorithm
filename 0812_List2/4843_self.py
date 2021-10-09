import sys
sys.stdin = open('4843_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(10):
        idx = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if data[idx] < data[j]:
                    idx = j
                data[idx], data[j] = data[j], data[idx]
        else:
            for j in range(i + 1, N):
                if data[idx] > data[j]:
                    idx = j
                data[idx], data[j] = data[j], data[idx]
