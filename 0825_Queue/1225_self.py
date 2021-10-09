import sys
sys.stdin = open('1225.txt', 'r')

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

for tc in range(1, 11):
    TC = int(input())
    data = list(map(int, input().split()))

    for val in data:
        push(val)

    cnt = 1
    while Q[r]:
        val = pop() -cnt
        cnt += 1
        if cnt == 6:
            cnt = 1
        if val < 0:
            val = 0
        push(val)

    print(f'#{tc}', end = ' ')
    while not isEmpty():
        print(pop(), end=' ')
    print()