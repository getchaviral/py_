def min_of_arr(arr,n):
    n=len(arr)
    if n==0:
         return None
    
    min_val = arr[0]
    for i in range(n):
        if arr[i]<min_val:
         min_val = arr[i]
    return min_val 

arr=[2,3,4,0]
n=len(arr)
print(min_of_arr(arr,n))



     


    


    
