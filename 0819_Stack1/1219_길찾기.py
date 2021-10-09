import sys
sys.stdin = open('1219.txt', 'r')

for _ in range(10):
    T, N = map(int, input().split())
    road = list(map(int, input().split()))

    road_list = [[] for _ in range(100)]
    for i in range(N): # 간선 정보를 저장
        road_list[road[2*i]].append(road[2*i+1])

    visited = [0] * 100
    ans = 0
    S = [0] # stack을 만들어줌

    while S:
        # 만약 값이 99가 나오면 ans = 1하고 끝내기
        curr = S.pop() # 먼저 빼주고 반복문 시작

        if curr == 99:
            ans = 1
            break

        for w in range(N):
            if visited[curr]: continue # 방문한적 있으면 넘어가고
            visited[curr] = 1

            for w in road_list[curr]:
                if not visited[w]: # 방문한적 없으면 stack에 추가
                    S.append(w)

    print(f'#{T} {ans}')