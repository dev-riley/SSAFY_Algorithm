import sys
sys.stdin = open('0819_DFS_실습문제3.txt', 'r')

V, E = map(int, input().split()) # 정점수, 간선수
G = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬

#간선수만큼 입력 처리
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = 1  # 무향 그래프일 때는 양쪽에 다 1이라고 표시해줘야함
    G[v][u] = 1 # 유향 그래프일 때는 한쪽에만 표시해주면 됨.

for lst in G[1:]:
    print(*lst[1:])