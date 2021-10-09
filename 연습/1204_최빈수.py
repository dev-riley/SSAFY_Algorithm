import sys
sys.stdin = open('1204.txt', 'r')

T = int(input()) # 총 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input()) # 테스트 케이스 번호
    data = list(map(int, input().split()))

    num_list = [0] * 101
    for i in range(1000):
        num_list[data[i]] += 1

    max_idx = 0
    num_max = num_list[0]
    for j in range(100):
        if num_max < num_list[j]:
            num_max = num_list[j]
            max_idx = j

    print('#{} {}'.format(tc, max_idx))
