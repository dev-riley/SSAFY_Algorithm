import sys
sys.stdin = open('0819_DFS_실습문제3.txt', 'r')
V, E = map(int, input().split())

G = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
print(G)
def dfs(v): # v = 방문할 정점 번호
    visited[v] = 1 # v를 방문한다.
    print(v, end=' ')
    # v의 인접 정점을 w를 찾는다.
    for w in G[v]:
        if not visited[w]:
            dfs(w)
dfs(1)