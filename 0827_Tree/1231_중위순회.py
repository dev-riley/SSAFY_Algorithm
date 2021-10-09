import sys
sys.stdin = open('1231.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    data = [[0]] + [list(input().split()) for _ in range(N)]

    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)

    for i in range(1, N + 1):
        p, c = int(data[i][0]), data[i][1]
        if len(data[i]) == 3:
            L[p] = int(data[i][2])
        elif len(data[i]) == 4:
            L[p] = int(data[i][2])
            R[p] = int(data[i][3])

    def inorder(n):
        if n != 0: # 공백 노드(자식이 없는 노드)일때는 끊어주려고
            inorder(L[n])
            print(data[n][1], end = '') # 입력으로 들어오는 노드의 1 ~N, 실제 데이터는 인덱스 그대로 저장이 되서 0부터 저장되어있다.
            inorder(R[n])
    print(f'#{tc} ', end = '')
    inorder(1)
    print()