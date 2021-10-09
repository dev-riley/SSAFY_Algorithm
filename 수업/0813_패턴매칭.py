# burute-force

 p = input() # pattern
 t = input() # text
 m,n = len(p), len(t)

 ans = 0
 # 패턴이 있을 수 있는 모든 가능한 시작 위치
 for i in range(0, n-m+1):
     # 패턴 길이 m만큼 비교
    j = 0
    while j < m:
        if p[j] != t[i + j]:
            break
        j += 1
    if j == m: # 찾음
        ans = 1
        break