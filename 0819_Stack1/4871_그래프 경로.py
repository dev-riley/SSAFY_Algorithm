import sys
sys.stdin = open('4871.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # V는 노드 갯수, E는 간선 갯수
    Q = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
    visited = [0] * (V + 1)

    # 간선 갯수 만큼 반복
    for _ in range(E):
        u, v = map(int, input().split()) # 간선 정보
        Q[u][v] = 1

    S, G = map(int, input().split()) # S는 출발 노드, G는 도착 노드

    visited[S] = 1
    S_list = [S] # while문에 들어가려면 빈 리스트면 안됨. []는 false
    ans = 0
    while S_list:
        if S == G:
            ans = 1
            break
        # 2) 정점 v에 인접한 정점 중에서
        # 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고
        # 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.
        for w in range(1, V + 1):
            if Q[S][w] == 1 and visited[w] == 0:
                S_list.append(S)
                visited[w] = 1  # 방문 표시
                S = w
                break
        else:
            # 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서
            # 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
            S = S_list.pop()
    print(f'#{tc} {ans}' )

