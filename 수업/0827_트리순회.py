import sys
sys.stdin = open('0827_트리.txt', 'r')

V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1) # 왼쪽 노드 저장
R = [0] * (V + 1) # 오른쪽 노드 저장
P = [0] * (V + 1) # 부모 노드 저장

for i in range(0, E*2, 2):
    p, c = arr[i], arr[i+1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

def inorder(v):
    if v == 0: return
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])

inorder(1)