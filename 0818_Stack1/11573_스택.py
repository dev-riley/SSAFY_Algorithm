import sys
sys.stdin = open('11573.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    Stack = []

    for i in range(len(arr)):
        if arr[i] != 0:
            Stack.append(arr[i])
        else:
            Stack.pop(-1)
    sum = 0
    for j in range(len(Stack)):
        sum += Stack[j]
        
    print(f'#{tc} {sum}')
