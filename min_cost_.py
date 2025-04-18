def min_cost(arr): # in this case we don't have to sort the array 
    n=len(arr)
    if n==0:
        return None
    
    x=min(arr)
    return((n-1)*x) 


arr=[1,2,3]
n=len(arr)
print(min_cost(arr))


     


