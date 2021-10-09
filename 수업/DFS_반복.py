import sys
sys.stdin = open('0819_DFS_실습문제3.txt', 'r')

V, E = map(int, input().split()) # 정점수, 간선수
G = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
visited = [0] * (V + 1)

#간선수만큼 입력 처리
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = 1  # 무향 그래프일 때는 양쪽에 다 1이라고 표시해줘야함
    G[v][u] = 1 # 유향 그래프일 때는 한쪽에만 표시해주면 됨.

# 1) 시작 정점 v를 결정하여 방문한다.
v = 1
S = [v]
visited[v] = 1
while S:
    # 2) 정점 v에 인접한 정점 중에서
    # 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고
    # 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.
    for w in range(1, V + 1):
        if G[v][w] == 1 and visited[w] == 0:
            S.append(v)
            visited[w] = 1 # 방문 표시
            v = w
            break
    else:
        # 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서
        # 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
        v = S.pop()