import sys; sys.stdin = open("4843_input.txt", "r")

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(10): # 10번만 반복: 10개만 출력하면 되니깐!
        idx = i     # 인덱스 저장
        if i % 2 == 0:  # 짝수 인덱스에 큰 숫자들이 차례대로 와야 하니깐
            for j in range(i + 1, N):
                if arr[idx] < arr[j]:   # 이해가 잘 안감...
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
        else:
            for j in range(i + 1, N):
                if arr[idx] > arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
    # 앞에서 10개를 출력
    # print('#{} {}'.format(tc, ' '.join(map(str, arr[:10]))))
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()
