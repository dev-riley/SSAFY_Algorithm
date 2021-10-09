import sys
sys.stdin = open('1216.txt', 'r')

    ### 아이디어 ###
    # 각 행마다 조사
    # s, e 각각 for문으로 반복해서 s~e가 회문인 것을 찾는다.
    # s 인덱스 i, e 인덱스 j해서 max값은 j-i로 저장
    # 같은 값이 연속으로 나올때..? 회문인지 체크
    # s ~ e값을 어떻게 구해야 할지 모르겠음...ㅜㅠ
    # 이게 맞는 방법인지 모르겠음..

    ### 풀이 ###
    # 길이가 긴것부터 짧은 것까지 즉, 100부터 한줄씩 줄여가면서 회문인지 아닌지 체크
    # 앞에 푼 4861_회문이랑 거의 유사함

def search(arr):
    # 길이 N인 한 행에 대해서 길이 M인 회문 찾기
    for M in range(100, 1, -1):
        for row in range(N):
            for s in range(N - M + 1):
                e = s + M -1
                for i in range(M // 2): # 모든 행에 대해서 회문인지 체크
                    if arr[row][s + i] != arr[row][e-i]:
                        break
                else:
                    return M
                for i in range(M // 2):  # 모든 열에 대해서 회문인지 체크
                    if arr[s + i][row] != arr[e - i][row]:
                        break
                else:
                    return M

for tc in range(1, 11):
    tc_num = input()
    N = 100
    arr = [input() for _ in range(N)]

    print(search(arr))