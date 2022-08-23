def search(arr, target, l, r):
    if l > r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == target:
        return mid
    if target > arr[mid]:
        return search(arr, target, mid + 1, r)
    return search(arr, target, l, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
l = 0
r = len(arr) - 1

print(search(arr, target, l, r))
