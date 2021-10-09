# arr = [67, 39, 16, 49, 60, 28, 8, 85, 89, 11]
# arr.sort() # 반드시 정렬 해야함.
# print(arr)

arr = [8, 11, 16, 28, 39, 49, 60, 67, 85, 89]

def binary_search(arr, lo, hi, key):
    # 중간 위치 선택
    while lo <= hi:
        mid = (lo + hi) //2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1

binary_search(arr, 0, len(arr),-1,67)