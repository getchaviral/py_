def leaders(arr):        
        n= len(arr)
        res=[]
        
        for i in range(n):
            
            for j in range(i+1,n):
                if arr[i] < arr[j]:
                  break
            else:   
                res.append(arr[i])
                    
        return res
arr=[1,2,3,4,5,4,3,2,2]
n= len(arr)
print(leaders(arr))  
