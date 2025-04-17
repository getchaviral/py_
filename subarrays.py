def generate_subarrays(arr):
    subarrays = []
    n = len(arr)

    for i in range(n):
        
        for j in range(i + 1, n + 1):
            subarrays.append(arr[i:j]) 
    return subarrays


arr = [1, 2, 3]
subarrays = generate_subarrays(arr)
print("All subarrays:")
for subarray in subarrays:
    print(subarray)
