import sys
sys.stdin = open('0826_BFS_input.txt', 'r')

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

v = 1 # 시작점
visit = [0] * (V + 1) # 방문 표시
Q = [v]
visit[v] = 1          # 시작점을 방문하고, Q에 삽입

while Q:              # 빈 Q가 아닐동안 반복
    v = Q.pop(0)
    # 방문하지 않은 인접 정점을 찾는다.
    for w in G[v]: # v에 인접 정점을 G[v]에 있으니깐
        if not visit[w]:
            visit[w] = 1
            Q.append(w)
