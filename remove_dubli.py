def removeDupli(arr):
    n = len(arr)
    if n <= 1:
        return n
    idx = 1  
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx
arr = [2, 2, 3, 4, 4, 5, 5, 6, 7, 7]  # Your input array
arr_without_dupli = removeDupli(arr)

# Output the result
print("Array without dupli:", arr_without_dupli)
