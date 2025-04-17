def arraysortedornot(arr,n):

    if(n==0 or n==1):
        return True
    
    return(arr[n-1]>= arr[n-2] and arraysortedornot(arr,n-1))

arr=[1,2,3,4,5,5,57]
n=len(arr)

if (arraysortedornot(arr, n)):
    print("Yes")
else:
    print("No")
