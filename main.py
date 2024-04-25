def find_biggest(arr, low, high):
    if high < low:
        return arr[0]
    if (high == low):
        return arr[low]
    mid = (low + high) // 2
    if arr[mid + 1] < arr[mid]:
        return arr[mid]
    
            
array = [4, 9, 3, 2, 12, 2, 4]
print(find_biggest(array, array[len(array)-1], len(array)-1))
