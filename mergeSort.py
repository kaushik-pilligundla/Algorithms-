def mergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursion

        mergeSort(left_arr)
        mergeSort(right_arr)

        #merging

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


nums = [4, 5, 6, 7, 2, 1, 4, 4, 6, 9, 3, 11, 15, 14, 12]
print(mergeSort(nums))
