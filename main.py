def binarySearch(arr, start, end, value):
    if start <= end:
        middle = (start + end) // 2

        if arr[middle] == value:
            return middle
        elif value < arr[middle]:
            return binarySearch(arr, start, middle -1, value)
        else:
            return binarySearch(arr, middle + 1, end, value)
    else:
        return -1
    
nums = [2,4,23,43,54,63,78,84,89,98]

print(binarySearch(nums, 0, len(nums)-1, 98))