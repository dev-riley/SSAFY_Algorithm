import sys
sys.stdin = open('1219.txt', 'r')

# for _ in range(10):
#     T, S = map(int, input().split()) # T = 테스트케이스 번호, E = 길의 총 개수
#     N = list(map(int, input().split()))

    # 간선 정보
    # for i in range(S):
    #     s = N[2*i]
    #     e = N[2*i+1]
    # print(s, e)

    #######
    # 저장 방법
    # 1. ch1, ch2
    # ch1 = [0] * 100
    # ch2 = [0] * 100
    #
    # for i in range(S):
    #     if ch1[N[2*i]] == 0:
    #         ch1[N[2*i]] = N[2*i+1]
    #     else:
    #         ch2[N[2*i]] = N[2*i+1]
    #
    # # 2. 인접행렬 방식
    # adj_arr = [[0] * 100 for _ in range(100)]
    # for i in range(S):
    #     adj_arr[N[2*i]][[2*i+1]] = 1
    #
    # # 3. 인접리스트 방식
    # adj_list = [[] for _ in range(100)]
    # for i in range(N):
    #     adj_list[N[2*i]].append(N[2*i+1])

    ###########################################
    # 반복구조로 만들어 보자!
for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])

    visited = [0] * 100
    ans = 0
    stack = [0]
    while stack:
        curr = stack.pop()

        if curr == 99:
            ans = 1
            break
        #방문하지 않으면

        #방문을 했으면 건너가~
        if visited[curr]: continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    print(f'#{tc} {ans}')