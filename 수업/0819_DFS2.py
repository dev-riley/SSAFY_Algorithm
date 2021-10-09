import sys
sys.stdin = open('0819_DFS_실습문제3.txt', 'r')

V, E = map(int, input().split())
# 인접 리스트
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V + 1):
    print(i, '-->', G[i])