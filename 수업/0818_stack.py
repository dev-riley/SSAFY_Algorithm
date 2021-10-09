arr = [0] * 10
def printHello(i, n):
    if i == n:
        print(arr)
    else:
        arr[i] = i + 1
        printHello(i + 1, n)
        arr[i] = 0

printHello(0, 3)
print(arr)