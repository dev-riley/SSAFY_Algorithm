import sys
sys.stdin = open('12383.txt', 'r')

N = int(input())
for tc in range(N):
    T = int(input())
    data = list(map(int, input().split()))
    ans = 0  # 최대 낙차값을 저장하는 변수
    for i in range(T):
        # i위치에서 바닥까지 거리 = total - 1 - i
        dist = T - 1 - i
        # data[i]상자의 바닥에 깔리는 상자의 수는 오른쪽편 크거나 같은 수의 개수
        for j in range(i + 1, T):
            if data[i] <= data[j]:
                dist -= 1
        if ans < dist:
           ans = dist
    print(f'#{tc+1} {ans}')