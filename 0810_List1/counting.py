K = 4   # 최댓값
A = [0, 4, 1, 3, 1, 2, 4, 1] #원본 자료
B = [0] * len(A)             # 정렬된 자료를 저장
C = [0] *(K + 1)             # 카운팅 저장

for val in A:                # 빈도수 계산
    C[val] += 1

for i in range(1, K + 1):     # 누적 빈도수 계산
    C[i] = C[i - 1] + C[i]

# 원본 자료들을 하나씩 옮긴다.
# A에서 하나씩 가져와서 C의 내용을 보고 B로 옮긴다.
for i in range(len(A) - 1, -1, -1):
    # A[i] --> B[C를 내용을 참고] = A[i]
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]

    print(B)