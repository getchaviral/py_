def removeDuplicates(arr):
     arr = [1, 2, 2, 3, 4, 5, 5]

    
     if not arr:
        return []

     result = [arr[0]]  

     for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  
            result.append(arr[i])

     return result


