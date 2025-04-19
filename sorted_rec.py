def arraysortedornot(arr,n):

    if(n==0 or n==1):
        return True
    
    for i in range(1, n):

        if (arr[i-1] < arr[i]):
            return True

    return False

arr=[1,2,3,4,5,5]
n=len(arr)
print(arraysortedornot(arr,n))  
