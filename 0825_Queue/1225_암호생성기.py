import sys
sys.stdin = open('1225.txt', 'r')


# 원형 Q
qsize = 9
Q = [0] * qsize
f = r = 0

def isEmpty():
    return f == r
def isFull():
    return f == (r + 1) % qsize
def push(item):
    global r
    r = (r + 1) % qsize
    Q[r] = item
def pop():
    global f
    f = (f + 1) % qsize
    return Q[f]

arr = [9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]
for val in arr:
    push(val)

cnt = 1
while Q[r]:
    val = pop() - cnt
    cnt += 1
    if cnt == 6:
        cnt = 1
    # val가 0보다 작은지
    if val < 0: val = 0
    push(val)

while not isEmpty():
    print(pop(), end=' ')
print()