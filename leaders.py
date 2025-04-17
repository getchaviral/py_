arr = [1,2,3,4,5,5,6,6,7,8]
n = len(arr)
result = []

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            break
    else:
        result.append(arr[i])

print("Leaders in array:")
print(" ".join(map(str, result)))
